from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('15.file.html')
    else:
        file_image = request.files['image']
        filename = os.path.join(app.static_folder,f'upload/{file_image.filename}')
        file_image.save(filename)
        return render_template('15.file_res.html',fname=f'upload/{file_image.filename}')

if __name__ == '__main__':
    app.run(debug=True)