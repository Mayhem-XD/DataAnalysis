from flask import Flask, render_template, request, redirect
import db.kpop_dao as kd

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask with MySQL'

@app.route('/song/list')
def song_list():
    songs = kd.get_song_list(20)
    return render_template('01.song_list.html', songs=songs)

@app.route('/gg/list')
def gg_list():
    groups = kd.get_girl_group_list(20)
    return render_template('11.gg_list.html', groups=groups)

@app.route('/insert_song', methods=['POST','GET'])
def insert_song():
    if request.method == 'GET':
        return render_template('21.insert_song.html')
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        params = (title,lyrics)
        kd.insert_song(params=params)
        return redirect('/insert_song')
    
# @app.route('/insert_gg',methods=['POST','GET'])
# def insert_gg():
#     if request.method == 'GET':
#         return render_template('23.insert_gg.html')
#     else:
#         title = request.form['title']
#         lyrics = request.form['lyrics']
#         params = (title,lyrics)
#         kd.insert_song(params=params)
#         return redirect('/insert_gg')
    
@app.route('/song/update/<sid>',methods=['POST','GET'])
def song_update(sid):
    if request.method == 'GET':
        return render_template('03.song_update.html',sid=sid)
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        sid = int(sid)
        params = (title,lyrics,sid)
        kd.song_update(params=params)
        songs = kd.get_song_list(20)
        return redirect('/song/list')

@app.route('/song/delete/<sid>',methods=['POST','GET'])
def song_delete(sid):
    sid = int(sid)
    kd.song_delete(sid)
    return redirect('/song/list')


if __name__ == '__main__':
    app.run(debug=True)