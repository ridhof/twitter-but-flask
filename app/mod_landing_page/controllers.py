"""
Landing Page Module's Controllers
"""
from flask import Blueprint, render_template, request, send_from_directory, session

from app import DB as db

from app.mod_tweet.forms import TweetForm

from app.mod_tweet.models import Tweet
from app.mod_auth.models import User

MOD_LANDING_PAGE = Blueprint('landing_page', __name__, url_prefix='/')


@MOD_LANDING_PAGE.route('', methods=['GET', 'POST'])
def landing_page():
    """
    Return a HTML of Landing Page.
    """
    username = session['username']
    form = TweetForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(name=username).first()
        tweet = Tweet(form.tweet.data, user)
        db.session.add(tweet)
        db.session.commit()
        form.tweet.data = ""
    tweets = Tweet.query.order_by(Tweet.id.desc()).all()
    return render_template("landing_page/landing_page.html", username=username, tweets=tweets, form=form)

@MOD_LANDING_PAGE.route('/robots.txt', methods=['GET', 'POST'])
def robots():
    """
    Return robot.txt file.
    """
    return send_from_directory('static/', filename='robots.txt')
