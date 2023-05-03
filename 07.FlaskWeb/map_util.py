import folium,os
import pandas as pd
from urllib.parse import quote
import requests,json


def hot_places(places, app):
    # 도로명 주소 구하기
    with open('D:/Workspace/03.DataAnalysis/04.지도시각화/data/roadapikey.txt') as f:
        road_key = f.read()
    with open('../04.지도시각화/data/kakaoapikey.txt') as f_:
        kakao_key = f_.read()
    base_url = 'https://www.juso.go.kr/addrlink/addrLinkApiJsonp.do'
    params1 = f'confmKey={road_key}&currentPage=1&countPerPage=10'
    params2 = f"keyword={quote('')}&resultType=json"
    url = f'{base_url}?{params1}&{params2}'

    road_addr_list = []
    for plc in places:
        params2 = f"keyword={quote(plc)}&resultType=json"
        url = f'{base_url}?{params1}&{params2}'
        result = requests.get(url)
        if result.status_code == 200:
            res = json.loads(result.text[1:-1])
            road_addr_list.append(res['results']['juso'][0]['roadAddr'])
        else:
            print(result.status_code)

    # df = pd.DataFrame({'이름':list(map(lambda x:x.split()[-1],places)),'주소':road_addr_list})
    df = pd.DataFrame({'이름':places,'주소':road_addr_list})

    base_url = "https://dapi.kakao.com/v2/local/search/address.json"
    url = f'{base_url}?query={quote("")}'
    header = {'Authorization':f'KakaoAK {kakao_key}'}
    lat_list = []
    lng_list = []
    for i in df.index:
        url = f'{base_url}?query={quote(df.주소[i])}'
        result = requests.get(url, headers=header).json()
        lat_list.append(float(result['documents'][0]['y']))
        lng_list.append(float(result['documents'][0]['x']))
    df['위도'] = lat_list
    df['경도'] = lng_list

    places_map = folium.Map(location=[df.위도.mean(),df.경도.mean()],zoom_start=12)
    for i in df.index:
        folium.Marker(
        location=[df.위도[i], df.경도[i]],                     
        popup=folium.Popup(df.주소[i],max_width=200),
        tooltip=df.이름[i],
    ).add_to(places_map)
    filename = os.path.join(app.static_folder,'img/HotPlaces.html')
    places_map.save(filename)