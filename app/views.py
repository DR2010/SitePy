from flask import render_template, flash, redirect
from app import app
from .models import Collection
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Arthur'}  # fake user
    posts = [  
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])



@app.route('/collections')
def collections():
    user = {'nickname': 'Arthur'}  # fake user

    col1 = Collection('ANIMALS', 'Animals', 'Collection of Animals')
    col2 = Collection('CARS', 'Cars', 'Collection of Cars')
	
    collections = [ col1, col2 ]
	
    return render_template("collections.html",
                           title='Home',
                           user=user,
                           collections=collections)