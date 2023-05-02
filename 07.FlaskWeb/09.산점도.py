import os 
from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/scatter',methods=['GET','POST'])
def scatter():
    if request.method == 'GET':
        return render_template('09.산점도.html')
    else:
        num = int(request.form['num'])
        mean = float(request.form['mean'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        xs= np.random.normal(loc=mean,scale=std,size=num)
        ys= np.random.uniform(min,max,num)
        plt.figure()
        plt.scatter(xs,ys)
        filename = os.path.join(app.static_folder,'img/scatter.png')
        plt.savefig(filename)
        return render_template('09.산점도_res.html')

if __name__ == '__main__':
    app.run(debug=True)