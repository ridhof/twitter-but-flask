"""
Auth Module's Controllers
"""
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

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
            if user.check_password(form.password.data):
                session['username'] = user.name
                return redirect(url_for('landing_page.landing_page'))
        flash('Username atau Password tidak ditemukan.', 'danger')
    return render_template("auth/login.html", form=form)


@MOD_AUTH.route('/register', methods=['GET', 'POST'])
def register():
    """
    Return a HTML of Register Page.
    """
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if not user:
            user = User(form.username.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(
                'User %r telah berhasil didaftarkan.' %
                (user.name), 'success')
        else:
            flash(
                'Username %r telah terdaftar.' %
                (user.name), 'danger')
    return render_template("auth/register.html", form=form)

@MOD_AUTH.route('/logout', methods=['GET'])
def logout():
    """
    Do logout (erase a session).
    """
    session['username'] = None
    flash('Berhasil logout', 'info')
    return redirect(url_for('auth.login'))
