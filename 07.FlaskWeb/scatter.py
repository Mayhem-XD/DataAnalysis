import numpy as np
import matplotlib.pyplot as plt
import os 

def draw_scatter(num,mean,std,min,max,app):

    xs= np.random.normal(loc=mean,scale=std,size=num)
    ys= np.random.uniform(min,max,num)
    plt.figure()
    plt.scatter(xs,ys)
    filename = os.path.join(app.static_folder,'img/scatter.png')
    plt.savefig(filename)