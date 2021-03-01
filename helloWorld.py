from flask import Flask,url_for, render_template
from markupsafe import escape, Markup

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World'

@app.route('/<name>')
def greet(name = None):
    return render_template('index.html', name = name) #'Hello %s Ji !' % format(escape()

with app.test_request_context():
    print(url_for('helloWorld'))
    print(url_for('greet',name='Saurabh'))





