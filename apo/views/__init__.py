"""
Blueprint for views pages
"""
from flask import Blueprint

views_blueprint = Blueprint("views", __name__, template_folder="templates")

from . import routes