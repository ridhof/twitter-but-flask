"""
Landing Page Module's Controllers
"""
from flask import Blueprint, render_template

MOD_LANDING_PAGE = Blueprint('landing_page', __name__, url_prefix='/')


@MOD_LANDING_PAGE.route('', methods=['GET'])
def landing_page():
    """
    Return a HTML of Landing Page.
    """
    return render_template("landing_page/landing_page.html")
