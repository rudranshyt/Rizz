# author: Rudransh Shukla
# description: rizz flask app with spotify integration

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def function():
    return render_template('welcome.html')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
