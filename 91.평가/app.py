from flask import Flask, render_template,request
import utils as ut
import jinja2

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
env = jinja2.Environment()
env.globals.update(zip=zip)
@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/melon',methods=['GET','POST'])
def melon():
    chart_list = ut.rt_chart()
    return render_template('melon.html',chart_list=chart_list)
@app.route('/youtube_ranking',methods=['GET','POST'])
def youtube_ranking():
    rank_list = ut.rt_rank()
    return render_template('youtube_ranking.html',rank_list=rank_list)
@app.route('/m3',methods=['GET','POST'])
def m3():
    rank_list = ut.rt_rank()
    t20 = ut.return_top20(rank_list)
    ctg,idx_ = ut.return_ctg(rank_list)
    return render_template('m3.html',t20=t20,ctg=ctg,idx_=idx_)




if __name__ == '__main__':
    app.run(debug=True)