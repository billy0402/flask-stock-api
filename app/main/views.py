from flask import render_template, session, redirect, url_for, current_app

from . import main
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    return 'success'
