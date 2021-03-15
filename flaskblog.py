from flask import Flask, render_template
app = Flask(__name__)
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
    return render_template('home.html', posts = posts_data)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)
    