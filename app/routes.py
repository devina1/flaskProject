from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'damos'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC305', 'title': 'Databases'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC208', 'title': 'Discrete Mathematics'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC346', 'title': 'Enterprise Programming'}, 'instructor': 'Evan Noynaert'},
               {'classInfo': {'code': 'MAT111', 'title': 'Statistics'}, 'instructor': 'Lori McCune'}]
    return render_template('index.html', title='Home', user=user, classes=classes)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

