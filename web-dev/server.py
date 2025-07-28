from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p>Hello World!11</p>'

@app.route('/<string:name>', methods = ['POST'])
def hello_name(name):
    return f'<p>Hello {name}!</p>'
