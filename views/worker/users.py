from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
from service.user_service import UserService

users_bp = Blueprint('users', __name__)

@users_bp.route('/approve', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('employee', 'admin')
def manage_accounts():
  users = UserService.get_unactivated_users()
  roles = UserService.get_roles()
  return render_template('worker/accounts/approve.html', users=users, roles=roles, current_user_id=session['user_id'])

@users_bp.route('/approve/<int:user_id>', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('employee', 'admin')
def activate_account(user_id):
  UserService.activate_user(user_id)
  return redirect(url_for('worker.users.manage_accounts'))

@users_bp.route('/delete/<int:user_id>', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('employee', 'admin')
def delete_account(user_id):
  if(user_id == session['user_id']):
    flash('You cannot delete your own account')
  else:
    if(UserService.delete_user(user_id) == False):
      flash('User cannot be deleted')
  return redirect(url_for('worker.users.manage_accounts'))