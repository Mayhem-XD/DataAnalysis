import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup

def in_bs():
    base_url='http://book.interpark.com'
    sub_url='/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028'
    url = base_url + sub_url
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    lis = soup.select('.rankBestContentList > ol > li')

    lines = []
    for li in lis:
        rank_data = li.select('.rankBtn_ctrl')
        if len(rank_data) == 1:
            rank = int(rank_data[0]['class'][-1][-1])
        else:
            rank = int(rank_data[0]['class'][-1][-1] + rank_data[1]['class'][-1][-1])
        img = li.select_one('.coverImage').find('img')['src']
        href = li.select_one('.coverImage> label > a')['href']
        title = li.select_one('.itemName').get_text().strip() 
        author = li.select_one('.author').get_text().strip()
        company = li.select_one('.company').get_text().strip()
        price = li.select_one('.price > em').get_text().strip()
        lines.append({'순위':rank,'이미지':img,'제목':title,'저자':author,'출판사':company,'가격':price, 'href':base_url + href})

    return lines
    # df = pd.DataFrame(lines)