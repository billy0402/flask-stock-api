from flask import Blueprint

api = Blueprint('api', __name__)

from . import (  # noqa:  F401
    news,
    stock,
)
