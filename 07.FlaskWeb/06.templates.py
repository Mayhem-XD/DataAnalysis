from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/Hello')
@app.route('/Hello/<name>')
def hello(name=None):
    dt = {'key1':'value1','key2':'value2','key3':'value3'}
    item = 'item'
    return render_template('06.Hello.html',name=name,dt=dt,item=item)

if __name__ == '__main__':
    app.run(debug=True)