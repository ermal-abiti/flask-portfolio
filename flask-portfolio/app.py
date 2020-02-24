from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'postTitle': "Post 3",
        'postDate': "24/02/2020",

        'postContent': """
        This is a simple post!!!!
        """,

        'postAuthor': "Ermal Abiti"

    },
    {
        'postTitle': "Post 2",
        'postDate': "24/02/2020",

        'postContent': """
        This is a simple post!!!!
        """,

        'postAuthor': "Ermal Abiti"

    },
    {
        'postTitle': "Post 1",
        'postDate': "24/02/2020",

        'postContent': """
        This is a simple post!!!!
        """,

        'postAuthor': "Ermal Abiti"

    },
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title="Home")


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/library')
def library():
    return render_template('library.html', title="Library")


@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)