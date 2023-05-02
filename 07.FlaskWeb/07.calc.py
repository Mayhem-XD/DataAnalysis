from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/calc', methods=['GET','POST'])
def calc():
    if request.method == 'GET':
        op_list = ['+', '-','*', '/', '//', '%']
        return render_template('07.calc.html',op_list=op_list)
    else:
        num1 = int(request.values['num1'])
        op = request.values['op']
        num2 = int(request.values['num2'])
        result = eval(f'{num1}{op}{num2}')
        return render_template('07.calc_res.html',num1=num2,op=op,num2=num2,result=result)

if __name__ == '__main__':
    app.run(debug=True)