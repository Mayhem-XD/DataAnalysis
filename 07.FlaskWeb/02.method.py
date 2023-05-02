from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/Hello')
def hello():
    return render_template('01.Hello.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:           #Method 가 POST
        return '환영합니다.'

if __name__ == '__main__':
    app.run(debug=True)

