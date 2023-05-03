from flask import Flask, request, render_template
import interpark_crawling as ic
app = Flask(__name__)

@app.route('/')
def index():
    return 'interpark_crawling'

@app.route('/bestseller', methods=['GET','POST'])
def bestseller():
        booklist = ic.in_bs()
        return render_template('11.interpark.html',booklist=booklist)

if __name__ == '__main__':
    app.run(debug=True)