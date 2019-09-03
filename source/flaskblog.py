from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='../templates', static_folder='../static')

posts = [
    {
        'author': 'svk',
        'title': 'Blog Post 1',
        'content': 'First blog post',
        'date_poste': 'September 2, 2019'
    },
    {
        'author': 'deep',
        'title': 'Blog Post 2',
        'content': 'Second blog post',
        'date_poste': 'September 3, 2019'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')