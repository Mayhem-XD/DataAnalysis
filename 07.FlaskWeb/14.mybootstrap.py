from flask import Flask, render_template, request
import scatter as sc
import map_util as mu
import interpark_crawling as ic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('14.mybootstrap.html')

@app.route('/carousel',methods=['GET','POST'])
def carousel():
    return render_template('14.carousel.html')

@app.route('/progress_bar',methods=['GET','POST'])
def progress_bar():
    return render_template('14.progress_bar.html')

@app.route('/scatter',methods=['GET','POST'])
def scatter():
    if request.method == 'GET':
        return render_template('14.산점도.html')
    else:
        num = int(request.form['num'])
        mean = float(request.form['mean'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        sc.draw_scatter(num,mean,std,min,max,app)
        return render_template('14.산점도_res.html')

@app.route('/interpark',methods=['GET','POST'])
def interpark():
    booklist = ic.in_bs()
    return render_template('14.interpark.html',booklist=booklist)

@app.route('/hotplaces',methods=['GET','POST'])
def hotplaces():
    if request.method == 'GET':
        return render_template('14.HotPlaces.html')
    else:
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        mu.hot_places(places, app)
        return render_template('14.HotPlaces_res.html')

if __name__ == '__main__':
    app.run(debug=True)