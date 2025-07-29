from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p>Hello World!11</p>'

@app.route('/<string:name>', methods = ['POST'])
def hello_name(name):
    return f'<p>Hello {name}!</p>'

@app.route('/app')
def app_route():
    args = { 'name': 'Anonymous', 'id': 'Unknown' }
    return render_template('index.html', **args)

# <type:var> - string,path,uuid,int,float

@app.route('/app/<string:name>/<int:id>')
def app_route_name(**args):
    return render_template('index.html', **args)

