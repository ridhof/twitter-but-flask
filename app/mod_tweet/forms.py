from flask_wtf import FlaskForm
from wtforms import TextAreaField

from wtforms.validators import Required


class TweetForm(FlaskForm):
    tweet = TextAreaField(
        'Tweet',
        validators=[
            Required(
                message="You can't post a blank tweet, right?")], 
        render_kw={'id': 'textarea1', 'data-length': "120", 'maxlength': "120"})
