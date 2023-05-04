import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
def genie_chart():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    url = 'https://www.genie.co.kr/chart/top200'
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text,'html.parser')
    trs = soup.select('tr.list')
    lines = []
    base_url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y'
    from datetime import datetime
    now = datetime.now()
    ymd = now.strftime('%Y%m%d') 
    hh = now.strftime('%H')
    for page in range(1,5):
        url = f'{base_url}&ymd={ymd}&hh={hh}&pg={page}'
        result = requests.get(url, headers=header)
        soup = BeautifulSoup(result.text,'html.parser')
        trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
        for tr in trs:
            rank = tr.select_one('.number').get_text().split('\n')[0].strip()
            img = 'https:' + tr.select_one('.cover > img')['src']
            try:
                title = tr.select_one('.title.ellipsis').get_text().strip()
            except:
                title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip()
            artist = tr.select_one('.artist.ellipsis').string.strip()
            album = tr.select_one('.albumtitle.ellipsis').text.strip()
            lines.append({'rank':rank,'img':img,'title':title,'artist':artist,'album':album})
    return lines