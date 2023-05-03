from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/child1')
def child1():
    return render_template('12.child1.html')

@app.route('/child2')
def child2():
    return render_template('12.child2.html')

if __name__ == '__main__':
    app.run(debug=True)