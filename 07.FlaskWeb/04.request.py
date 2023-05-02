from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/Hello')
def hello():
    return render_template('01.Hello.html')

# localhost:5000/area?pi=3.14&radius=5
@app.route('/area')                     # 따로 언급없으면 GET 방식
def area():
    # pi = request.args.get('pi','3.141592')
    # localhost:5000/area?radius=5
    pi = request.args.get('pi')
    radius = request.values['radius']
    a = float(pi) * float(radius) **2
    return f'<h1>pi = {pi} radius = {radius} area = {a} </h1>'



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:           #Method 가 POST
        uid = request.form['uid']
        pwd = request.values['pwd']
        return f'<h1>uid = {uid}, pwd = {pwd}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

