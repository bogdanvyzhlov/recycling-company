from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
import forms
from service.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signin', methods=['GET', 'POST'])
def sign_in():
    form = forms.SignInForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserService.verify(email=request.form['email'], password=request.form['password'])
        if user:
            session['authenticated'] = 1
            session['user_id'] = user['id']
            session['email'] = user['email']
            session['phone'] = user['phone']
            session['firstname'] = user['firstname']
            session['lastname'] = user['lastname']
            session['activated'] = user['activated']
            session['role'] = user['title']
            return redirect(url_for('homepage.index'))
        else:
            flash('Incorrect login or password')
    return render_template("auth/sign_in.html", form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = forms.RegistrationUserForm(request.form)
    if request.method == 'POST' and form.validate():
        insertedId = UserService.register(email=request.form['email'], password=request.form['password'], phone=request.form['phone'], firstname=request.form['firstname'], lastname=request.form['lastname'])
        if insertedId != -1:
            return redirect(url_for('auth.sign_in'))
        else:
            flash('User with this email already exists')
    return render_template('auth/sign_up.html', form=form)

@auth_bp.route('/signout')
@auth.login_required
def signout():
    session.pop("authenticated")
    session.pop("user_id")
    session.pop("email")
    session.pop("phone")
    session.pop("firstname")
    session.pop("lastname")
    session.pop("activated")
    session.pop("role")
    return redirect(url_for('homepage.index'))
