import requests, os

def get_weather(app,lat_=37.295, lon_= 127.045):
    key_file = os.path.join(app.static_folder,'key/openweather.txt')
    with open(key_file) as f:
        weather_key = f.read()
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    lat, lon = lat_, lon_          # 수원 중심부 좌표
    url = f'{base_url}?lat={lat}&lon={lon}&appid={weather_key}&units=metric&lang=kr'
    result = requests.get(url).json()
    desc = result['weather'][0]['description']
    icon_code = result['weather'][0]['icon']
    icon_url = f'http://api.openweathermap.org/img/w/{icon_code}.png'
    temp_ = result['main']['temp']
    temp = round(float(temp_)+0.01,1)  
    return  f'''<img src="{icon_url}" height="32"><strong>{desc}</strong> 온도: <strong>{temp}</strong>&#8451'''