from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/index')
# def home():
#     return render_template('index.html')
#
# @app.route('/works')
# def works():
#     return render_template('works.html')
#
# @app.route('/work')
# def work():
#     return render_template('work.html')
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')

@app.route('/contact_submit', methods = ['POST'])
def contact():
    form_data = request.form.to_dict()
    print(form_data)
    return render_template('thankyou.html')
