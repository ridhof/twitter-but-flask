"""
Landing Page Module's Controllers
"""
from flask import Blueprint, render_template, request, send_from_directory, session
import time

from app import DB as db, REDIS as redis, REDIS_QUEUE as rqueue

from app.mod_tweet.forms import TweetForm

from app.mod_tweet.models import Tweet
from app.mod_auth.models import User

from app.mod_landing_page.tasks import bg_insert_tweet

from common import pretty_result, code

MOD_LANDING_PAGE = Blueprint('landing_page', __name__, url_prefix='/')


def insert_tweet(text, username):
    print(f"Inserting a Tweet")
    start = time.time()

    user = User.query.filter_by(name=username).first()
    tweet = Tweet(text, user=user)
    print(f"Creating a Tweet object: {tweet}")
    # tweet.insert()
    db.session.add(tweet)
    db.session.commit()

    end = time.time()
    time_elapsed = end - start
    return f"Stored to Database in {time_elapsed} ms"

@MOD_LANDING_PAGE.route('', methods=['GET', 'POST'])
def landing_page():
    """
    Return a HTML of Landing Page.
    """
    username = session['username']
    form = TweetForm(request.form)
    if form.validate_on_submit():
        task = rqueue.enqueue(bg_insert_tweet, form.tweet.data, username)
        form.tweet.data = ""
    tweets = Tweet.query.order_by(Tweet.id.desc()).limit(5)
    return render_template("landing_page/landing_page.html", username=username, tweets=tweets, form=form)

@MOD_LANDING_PAGE.route('/tweet', methods=['GET', 'POST'])
def get_tweet():
    """
    Return tweets
    """
    if request.method == 'GET':
        query_tweets = Tweet.query.order_by(Tweet.id.desc()).limit(5)
        tweets = []
        for query_tweet in query_tweets:
            tweets.append({
                'tweet': query_tweet.text, 
                'username': query_tweet.get_username(),
                'user_id': query_tweet.user_id,
            })
        return pretty_result(code.OK, data=tweets)
    else:
        result = insert_tweet(request.form['text'], request.form['username'])
        return result

@MOD_LANDING_PAGE.route('/robots.txt', methods=['GET', 'POST'])
def robots():
    """
    Return robot.txt file.
    """
    return send_from_directory('static/', filename='robots.txt')
