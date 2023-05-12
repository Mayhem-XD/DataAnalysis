import requests, re
from urllib.parse import quote
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def rt_chart():
    url = 'https://www.melon.com/chart/'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text,'html.parser')
    trs = soup.select('tbody > tr')
    lines = []
    for tr in trs:
        try:
            rank = tr.select_one('#lst50 > td > div > span.rank').get_text()
            img = tr.select_one('#lst50 > td > div > a > img')['src']
        except:
            rank = tr.select_one('#lst100 > td > div > span.rank').get_text()
            img = tr.select_one('#lst100 > td > div > a > img')['src']
        title = tr.select_one('.ellipsis.rank01 > span > a').get_text().strip()
        artist = tr.select_one('.ellipsis.rank02 > a').get_text().strip()
        album = tr.select_one('.ellipsis.rank03 > a').get_text().strip()
        lines.append({'rank':rank,'img':img,'title':title,'artist':artist,'album':album})
    return lines

def rt_rank():
    url= 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text,'html.parser')
    lis = soup.select('form > table > tbody > tr')
    lines = []
    for i in range(1,11):
        url_base = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page='
        res = requests.get(url_base+str(i))
        soup = BeautifulSoup(res.text)
        for li in lis:
            rank = int(li.select_one('.rank').get_text().strip())
            category = li.select_one('.category').get_text().strip()
            channel = li.select_one('form > table > tbody > tr > td > h1 >a').get_text().replace('\t\r\n','').strip()
            subscriber_cnt = int(li.select_one('.subscriber_cnt').get_text()[:-1])
            view_cnt = li.select_one('.view_cnt').get_text()
            view_cnt = int(re.sub('[ㄱ-ㅎㅏ-ㅣ가-힣]','', view_cnt))
            video_cnt = li.select_one('.video_cnt').get_text()
            video_cnt = int(re.sub('[ㄱ-ㅎㅏ-ㅣ가-힣,]','', video_cnt))
            lines.append({'rank':rank,'category':category,'channel':channel,'subscriber_cnt':subscriber_cnt,'view_cnt':view_cnt,'video_cnt':video_cnt})
    return lines

def return_top20(lines):
    df = pd.DataFrame(lines)
    df1 = df.head(20).copy()
    return df1.values

def return_ctg(lines):
    df = pd.DataFrame(lines)
    df2 = df.pivot_table('channel', 'category', aggfunc='count').sort_values('channel', ascending=False).head(10).copy()
    return df2.values, df2.index
