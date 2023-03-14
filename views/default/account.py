from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from service.collections_service import CollectionsService
import forms
import auth
from service.user_service import UserService
account_bp= Blueprint('account', __name__)


@account_bp.route('/account', methods=['GET', 'POST'])
@auth.login_required
def account():
    form = forms.UpdateUserForm(request.form)
    user = UserService.get_user(session['user_id'])
    addresses_main=UserService.get_addresses_by_user_main(session['user_id'])
    addresses= UserService.get_addresses_by_user(session['user_id'])
    if request.method == 'POST' and form.validate():
        UserService.update_user(request.form['email'], request.form['password'], request.form['phone']
                           ,session['user_id'])
        UserService.update_address_main(request.form['street_main'], request.form['city_main'], request.form['postalcode_main'],
                                        session['user_id'])
        UserService.update_address(request.form['street'], request.form['city'], request.form['postalcode'],
                                        session['user_id'])
        return redirect(url_for('account.account'))
    return render_template('default/account.html', form=form, user=user,addresses=addresses, addresses_main=addresses_main)


@account_bp.route('/history', methods=['GET', 'POST'])
@auth.login_required
def history():
    sum_month= CollectionsService.get_total_price_by_user_actual_month(session['user_id'])
    collections= CollectionsService.get_collections_by_user(session['user_id'])

    return render_template('default/history.html', collections=collections, sum_month=sum_month)