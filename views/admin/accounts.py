from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
from service.user_service import UserService

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/manage', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin', 'limited_admin')
def manage_accounts():
  users = UserService.get_users()
  roles = UserService.get_roles()
  return render_template('admin/accounts/manage.html', users=users, roles=roles, current_user_id=session['user_id'])

@accounts_bp.route('/activate/<int:user_id>', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin', 'limited_admin')
def activate_account(user_id):
  UserService.activate_user(user_id)
  return redirect(url_for('admin.accounts.manage_accounts'))

@accounts_bp.route('/change_role/<int:user_id>', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin', 'limited_admin')
def change_role(user_id):
  role_id = request.args.get('role_id')
  UserService.set_user_role(user_id, role_id)
  return redirect(url_for('admin.accounts.manage_accounts'))

@accounts_bp.route('/delete/<int:user_id>', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin', 'limited_admin')
def delete_account(user_id):
  if(user_id == session['user_id']):
    flash('You cannot delete your own account')
  else:
    if(UserService.delete_user(user_id) == False):
      flash('User cannot be deleted')
  return redirect(url_for('admin.accounts.manage_accounts'))