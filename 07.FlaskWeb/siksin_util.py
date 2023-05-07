import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup

def siksin_search(place):
    base_url = 'https://www.siksinhot.com/search'
    url = f'{base_url}?keywords={quote(place)}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text,'html.parser')
    lis = soup.select('.localFood_list > li')
    temp_list = []
    for li in lis:
        a_tags = li.select('.cate > a')
        temp_dict = {
            'img':li.find('img')['src'],
            'title':li.select_one('.textBox > h2').get_text(),
            'score':li.select_one('.textBox > span').get_text(),
            'location':a_tags[0].get_text(),
            'menu':a_tags[1].get_text()
        }
        temp_list.append(temp_dict)
    return temp_list