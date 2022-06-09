import os, click, functools
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Base
from flask import (
    session, redirect, url_for
)
from instance.config import DATABASE

def get_engine():
    engine = create_engine('sqlite:///'+DATABASE)
    return engine

@click.command()
def migrate():
    engine = get_engine()
    Base.metadata.create_all(engine)

def cook_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

def login_required(view):
    functools.wraps(view)
    def wrapper(**kwargs):
        if "username" in session:
            return view(**kwargs)
        else:
            return redirect(url_for('auth.login'))
    return wrapper
