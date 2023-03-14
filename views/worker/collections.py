from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
import forms
from service.collections_service import CollectionsService
from service.materials_service import MaterialsService
from service.user_service import UserService

collections_bp = Blueprint('collections', __name__)

@collections_bp.route('/all', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('employee', 'admin')
def update_collections():
  collections = CollectionsService.get_all_collections()
  return render_template('worker/collections/all_collections.html', collections=collections)


@collections_bp.route('/register', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('employee', 'admin')
def new_collection():
  materials = MaterialsService.get_materials()
  form = forms.CollectionForm(request.form)
  if request.method == 'POST':
    email = request.form.get('email')
    users_id = UserService.get_user_id(email)
    user= UserService.get_user(users_id)
    materials_id = request.form.get('materials_id')

    if users_id != -1:
      if user['activated'] == 1:
        if form.validate():
          insertedId = CollectionsService.register_collection(weight=request.form['weight'], description=request.form['description'], users_id=users_id, materials_id=materials_id)
          if insertedId != -1 and form.validate():
            return redirect(url_for('worker.collections.update_collections'))
        else:
          flash('Error: incorrectly filled in data in the form')
      else:
        flash('Error: This account is not activated')
    else:
      flash('Error: This email does not exist in database')
  return render_template('worker/collections/register.html', materials=materials, form=form)