#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

# should be declared before importing views
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# pep8 doesn't like this
from api.v1.views.users import *
from api.v1.views.index import *

User.load_from_file()
