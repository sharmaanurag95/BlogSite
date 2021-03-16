from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bcf398418d2915b84ef2299e1d37002d'
# To generate this key, following code is used:
# import secrets
# secrets.token_hex(16)

posts_data = [
    {
     'author': 'Anurag Sharma',
     'title': 'First Dummy Blog',
     'content': 'First post content',
     'date_posted': 'March 10, 2021',
     },
    {
     'author': 'Vipul Sharma',
     'title': 'Second Dummy Blog',
     'content': 'Second post content',
     'date_posted': 'March 16, 2021',
     },
    {
     'author': 'Nick Fury',
     'title': 'Third Dummy Blog',
     'content': 'Third post content',
     'date_posted': 'March 16, 2021',
     }
    ]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts_data, title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Successfully logged in!!', 'success')
        return redirect(url_for('home')) #redirecting to home page through home method
    return render_template('register.html', title='Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)
    