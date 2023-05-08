from flask import Flask, render_template, request
from weather_util import get_weather
import utils as ut
import os, random

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    global quote,quotes
    global addr
    filename = os.path.join(app.static_folder,'data/todayQuote.txt')
    with open(filename,encoding='utf-8') as f:
        quotes = f.readlines()
    quote = random.sample(quotes,1)[0]
    addr = '수원시 장안구'
@app.route('/change_quote')
def change_quote():
    global quote
    quote = random.sample(quotes,1)[0]
    return quote

@app.route('/change_addr')
def change_addr():
    global addr
    addr = request.args.get('addr')
    return addr

@app.route('/change_weather')
def weather():
    global addr
    addr = request.values['addr']
    lat_,lon_ = ut.get_coord(addr+'청')
    return get_weather(app,lat_,lon_)

@app.route('/change_profile',methods=['POST'])
def change_profile():
    file_image = request.files['image']
    filename = os.path.join(app.static_folder,f'upload/{file_image.filename}')
    file_image.save(filename)
    mtime = ut.change_profile(app,filename)
    return str(mtime)
    

@app.route('/')
def home():
    menu = {'ho':1,'us':0,'cr':0,'sc':0}
    return render_template('prototype/home.html',menu=menu, weather=get_weather(app),quote=quote,addr=addr)

@app.route('/schedule')
def schedule():
    menu = {'ho':0,'us':0,'cr':0,'sc':1}
    return render_template('prototype/02.schedule.html',menu=menu, weather=get_weather(app),quote=quote,addr=addr)

@app.route('/self_intr')
def self_intr():
    menu = {'ho':0,'us':1,'cr':0,'sc':0}
    return render_template('prototype/self_intr.html',menu=menu, weather=get_weather(app),quote=quote,addr=addr)

@app.route('/crawling/interpark',methods=['GET','POST'])
def interpark():
    menu = {'ho':0,'us':0,'cr':1,'sc':0}
    booklist = ut.in_bs()
    return render_template('prototype/interpark.html',menu=menu, weather=get_weather(app),booklist=booklist,quote=quote,addr=addr)

@app.route('/crawling/genie',methods=['GET','POST'])
def genie():
    menu = {'ho':0,'us':0,'cr':1,'sc':0}
    chart_list = ut.genie_chart()
    return render_template('prototype/genie.html',menu=menu, weather=get_weather(app),chart_list=chart_list,quote=quote,addr=addr)

@app.route('/crawling/siksin',methods=['GET','POST'])
def siksin():
    menu = {'ho':0,'us':0,'cr':1,'sc':0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html',menu=menu, weather=get_weather(app),quote=quote,addr=addr)
    else:
        place = request.form['place']
        siksin_list = ut.siksin_search(place)
        return render_template('prototype/siksin_res.html',menu=menu, weather=get_weather(app),siksin_list=siksin_list,quote=quote,addr=addr)





if __name__ == '__main__':
    app.run(debug=True)