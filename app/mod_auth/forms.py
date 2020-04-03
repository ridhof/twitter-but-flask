from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

from wtforms.validators import Required


class LoginForm(FlaskForm):
    username = TextField('Username',
                         [Required(message="Forgot your username?")])
    password = PasswordField('Password',
                             [Required(message="Must provide a password!")])
