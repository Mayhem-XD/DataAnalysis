from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/Hello')
def hello():
    return render_template('01.Hello.html')

if __name__ == '__main__':
    app.run(debug=True)