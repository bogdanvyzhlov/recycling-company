from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
from views.admin.materials import materials_bp
from views.admin.accounts import accounts_bp

admin_bp = Blueprint('admin', __name__)
admin_bp.register_blueprint(materials_bp, url_prefix='/materials')
admin_bp.register_blueprint(accounts_bp, url_prefix='/accounts')