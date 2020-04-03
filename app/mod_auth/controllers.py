"""
Auth Module's Controllers
"""
from flask import Blueprint, flash, render_template, request

from app import DB as db

from app.mod_auth.forms import LoginForm

from app.mod_auth.models import User

MOD_AUTH = Blueprint('auth', __name__, url_prefix='/')


@MOD_AUTH.route('/login', methods=['GET', 'POST'])
def login():
    """
    Return a HTML of Login Page.
    """
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user:
            flash('Welcome')
        flash('Username atau Password tidak ditemukan.')
    return render_template("auth/login.html", form=form)


@MOD_AUTH.route('/register', methods=['GET', 'POST'])
def register():
    """
    Return a HTML of Register Page.
    """
    return render_template("auth/register.html")
