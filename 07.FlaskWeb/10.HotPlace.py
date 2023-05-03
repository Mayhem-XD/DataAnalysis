from flask import Flask, render_template, request
import map_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hotplace',methods=['GET','POST'])
def hotplace():
    if request.method == 'GET':
        return render_template('10.HotPlaces.html')
    else:
        # client 가 입력한 장소
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        mu.hot_places(places)
        return render_template('10.HotPlaces_res.html')


if __name__ == '__main__':
    app.run(debug=True)