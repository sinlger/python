from flask import Flask, escape, url_for

import config

app = Flask(__name__)

app.config.from_object(config)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, ddd'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run()
