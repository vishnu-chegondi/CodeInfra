import os, hashlib, click

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
    )
from .db import cook_session
from .models import User

authbp = Blueprint('auth', __name__, url_prefix='/auth')

@click.command()
@click.option('--username','-u', help="Enter Username")
@click.option('--password','-p', help="Enter Password")
def adduser(username, password):
    '''
    Add user to login
    '''
    dbsession=cook_session()
    user=User(username=username)
    user.set_password(password)
    dbsession.add(user)
    dbsession.commit()

@authbp.route('/login', methods=('GET', 'POST'), endpoint="login")
def login():
    '''
    This returns home page
    '''
    if request.method == "POST":
        if "user" not in g:
            g.dbsession=cook_session()
            user = g.dbsession.query(User).filter(User.username==request.form['username']).one()
            if user.verify_password(request.form["password"]):
                g.user = user
                session.clear()
                session['username']=user.username
                return redirect(url_for('template.index'))
        else:
            return redirect(url_for('index'))
    return render_template("login.html")

@authbp.route('/logout', methods=('GET',), endpoint="logout")
def logout():
    '''
    This is for logout
    '''
    session.clear()
    return redirect(url_for('auth.login'))