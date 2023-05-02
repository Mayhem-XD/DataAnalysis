import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/static_resource')
def static_resource():
    image_file = os.path.join(app.root_path, 'static/img/고양이.jpg')
    mtime = int(os.stat(image_file).st_mtime)
    return render_template('05.static.html',mtime =mtime)

if __name__ == '__main__':
    app.run(debug=True)