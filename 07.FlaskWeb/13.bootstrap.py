from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/carousel')
def carousel():
    return render_template('13.carousel.html')

@app.route('/progress_bar')
def progress_bar():
    return render_template('13.progress_bar.html')

if __name__ == '__main__':
    app.run(debug=True)