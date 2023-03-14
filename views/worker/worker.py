from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from views.worker.collections import collections_bp
from views.worker.users import users_bp

worker_bp = Blueprint('worker', __name__)
worker_bp.register_blueprint(collections_bp, url_prefix='/collections')
worker_bp.register_blueprint(users_bp, url_prefix='/users')