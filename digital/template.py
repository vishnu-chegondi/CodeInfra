from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
    )
from .db import cook_session, login_required
from .models import User

tempbp = Blueprint("template", __name__, url_prefix='/template')


@tempbp.route('/index', methods=('GET',), endpoint="index")
@login_required
def index():
    '''
    This returns the template dashboard
    '''
    dbsession=cook_session()
    users=dbsession.query(User).all()
    return render_template("index.html", users_list=users)

@tempbp.route('/new', methods=('GET','POST',), endpoint="new")
@login_required
def template():
    '''
    This creates a new template
    '''
    if request.method=="POST":
        pass
    else:
        return render_template("create.html")
