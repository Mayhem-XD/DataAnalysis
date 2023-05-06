from flask import Flask, render_template, request
from weather_util import get_weather
import interpark_crawling as ic
import genie_util as gu
import siksin_util as su

app = Flask(__name__)

@app.route('/')
def home():
    menu = {'ho':1,'us':0,'cr':0,'sc':0}
    return render_template('prototype/home.html',menu=menu, weather=get_weather(app))

@app.route('/schedule')
def schedule():
    menu = {'ho':0,'us':0,'cr':0,'sc':1}
    return render_template('prototype/02.schedule.html',menu=menu, weather=get_weather(app))

@app.route('/self_intr')
def self_intr():
    menu = {'ho':0,'us':1,'cr':0,'sc':0}
    return render_template('prototype/self_intr.html',menu=menu, weather=get_weather(app))

@app.route('/crawling/interpark',methods=['GET','POST'])
def interpark():
    menu = {'ho':0,'us':0,'cr':1,'sc':0}
    booklist = ic.in_bs()
    return render_template('prototype/interpark.html',menu=menu, weather=get_weather(app),booklist=booklist)

@app.route('/crawling/genie',methods=['GET','POST'])
def genie():
    menu = {'ho':0,'us':0,'cr':1,'sc':0}
    chart_list = gu.genie_chart()
    return render_template('prototype/genie.html',menu=menu, weather=get_weather(app),chart_list=chart_list)

@app.route('/crawling/siksin',methods=['GET','POST'])
def siksin():
    menu = {'ho':0,'us':0,'cr':1,'sc':0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html',menu=menu, weather=get_weather(app))
    else:
        place = request.form['place']
        siksin_list = su.siksin_search(place)
        return render_template('prototype/siksin_res.html',menu=menu, weather=get_weather(app),siksin_list=siksin_list)


if __name__ == '__main__':
    app.run(debug=True)