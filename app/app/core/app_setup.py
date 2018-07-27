from ..main import app
from flask import render_template


@app.route("/")
def hello():
    # This could also be returning an index.html
    # return '''Hello World from Flask in a uWSGI Nginx Docker container with \
    #  Python 3.6 (from the example template), 
    #  try also: <a href="/users/">/users/</a>'''
    
    title = 'hello buddy'
    
    return render_template('layout.html', **locals())

@app.route("/vis")
def vis():
    title = 'Visjs Graph'
    
    return render_template('vis.html', **locals())