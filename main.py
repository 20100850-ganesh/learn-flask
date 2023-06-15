from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'dummy1',
        'title': 'Blog Post 1',
        'content': 'This is a first blog post content posted by dummy 1 for the flask web app.',
        'date_posted': 'June 15, 2023'
    },
    {
        'author': 'dummy2',
        'title': 'Blog Post 2',
        'content': 'This is another blog post content posted by dummy 2 for the flask web app.',
        'date_posted': 'June 16, 2023'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
