from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = '120a72a8f0eec439a5f211b5339a8a83' 
# import secrets
# secrets.token_hex(16)

posts = [
    {
        'author': 'svk',
        'title': 'Blog Post 1',
        'content': 'First blog post',
        'date_posted': 'September 2, 2019'
    },
    {
        'author': 'deep',
        'title': 'Blog Post 2',
        'content': 'Second blog post',
        'date_posted': 'September 3, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'svk@blog.com' and form.password.data == '1234':
            flash('Login successful!', 'success')
            return render_template('home.html')
        else:
            flash('Login unsuccessful. Please enter correct email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/password-reset')
def password_reset():
    return render_template('password-reset.html', title='Reset Password')