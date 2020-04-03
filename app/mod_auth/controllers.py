"""
Auth Module's Controllers
"""
from flask import Blueprint, render_template

MOD_AUTH = Blueprint('auth', __name__, url_prefix='/')


@MOD_AUTH.route('/login', methods=['GET', 'POST'])
def login():
    """
    Return a HTML of Login Page.
    """
    return render_template("auth/login.html")

@MOD_AUTH.route('/register', methods=['GET', 'POST'])
def register():
    """
    Return a HTML of Register Page.
    """
    return render_template("auth/register.html")
