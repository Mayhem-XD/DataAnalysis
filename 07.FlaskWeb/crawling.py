from flask import Blueprint , request, session, render_template, Flask
from weather_util import get_weather
import utils as ut

user_bp_c = Blueprint('user_bp_c',__name__)
app = Flask(__name__)


@user_bp_c.route('/interpark', methods=['GET','POST'])
def interpark():
    menu = {'ho':0,'us':0,'cr':1,'sc':0,'py':0}
    booklist = ut.in_bs()
    return render_template('prototype/crawling/interpark.html',menu=menu, weather=get_weather(app),booklist=booklist,quote=session['quote'],addr=session['addr'])

@user_bp_c.route('/genie',methods=['GET','POST'])
def genie():
    menu = {'ho':0,'us':0,'cr':1,'sc':0,'py':0}
    chart_list = ut.genie_chart()
    return render_template('prototype/crawling/genie.html',menu=menu, weather=get_weather(app),chart_list=chart_list,quote=session['quote'],addr=session['addr'])

@user_bp_c.route('/genie_jquery',methods=['GET','POST'])
def genie_jquery():
    menu = {'ho':0,'us':0,'cr':1,'sc':0,'py':0}
    chart_list = ut.genie_chart()
    return render_template('prototype/crawling/genie_jquery.html',menu=menu, weather=get_weather(app),chart_list=chart_list,quote=session['quote'],addr=session['addr'])

@user_bp_c.route('/siksin',methods=['GET','POST'])
def siksin():
    menu = {'ho':0,'us':0,'cr':1,'sc':0,'py':0}
    if request.method == 'GET':
        return render_template('prototype/crawling/siksin.html',menu=menu, weather=get_weather(app),quote=session['quote'],addr=session['addr'])
    else:
        place = request.form['place']
        siksin_list = ut.siksin_search(place)
        return render_template('prototype/crawling/siksin_res.html',menu=menu, weather=get_weather(app),siksin_list=siksin_list,quote=session['quote'],addr=session['addr'],place=place)
    