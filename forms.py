import re
from wtforms import Form, StringField, PasswordField, validators, IntegerField, TextAreaField


class SignInForm(Form):
    email = StringField(name='email', label='E-mail', validators=[validators.InputRequired(), validators.Email(message='Invalid email address')])
    password = PasswordField(name='password', label='Password', validators=[validators.InputRequired(message='Passwords must contain at least six characters')])

class RegistrationUserForm(Form):
    firstname = StringField(name='firstname', label='First name', validators=[validators.InputRequired(), validators.Length(min=2, max=32)])
    lastname = StringField(name='lastname', label='Last name', validators=[validators.InputRequired(), validators.Length(min=2, max=32)])
    email = StringField(name='email', label='Email', validators=[validators.InputRequired(), validators.Email(message='Invalid email address')])
    password = PasswordField(name='password', label='Password', validators=[validators.InputRequired(message='Passwords must contain at least six characters'), validators.Length(min=8, max=32)])
    password_repeat = PasswordField(name='password_repeat', label='Repeat password', validators=[validators.InputRequired(), validators.EqualTo(fieldname='password', message='Passwords must match')])
    #Allowed phone number formats: +420XXXXXXXXX, +421XXXXXXXXX, 00420XXXXXXXXX, 00421XXXXXXXXX, 420XXXXXXXXX, 421XXXXXXXXX, +420 XXXXXXXXX, +421 XXXXXXXXX, 00420 XXXXXXXXX, 00421 XXXXXXXXX, 420 XXXXXXXXX, 421 XXXXXXXXX
    phone = StringField(name='phone', label='Phone number', validators=[validators.InputRequired(), validators.Regexp(regex=r'^((\+)?|(00))((420)|(421))(\s)?(\d{9})$', flags=re.MULTILINE, message='Phone number must be in format +420XXXXXXXXX or +421XXXXXXXXX')], render_kw={'placeholder': '+420XXXXXXXXX'})




class MaterialForm(Form):
    name = StringField(name='name', label='Name', validators=[validators.InputRequired(), validators.Length(min=2, max=32)], render_kw={'placeholder': 'Iron'})
    price = StringField(name='price', label='Price per kg', validators=[validators.InputRequired(), validators.Regexp(regex=r'^\d+(\.(\d)+)?$', flags=re.MULTILINE, message='Supported price formatting: 123 (integer) or 123.00 (float)')], render_kw={'placeholder': '129.90'})



class UpdateUserForm(Form):
    street_main = StringField(name='street_main', label='Street of permanent',
                            validators=[validators.Length(min=2, max=32)])
    city_main = StringField(name='city_main', label='City of permanent',
                           validators=[validators.Length(min=2, max=32)])
    postalcode_main = StringField(name='postalcode_main', label='Zip of permanent',
                            validators=[validators.Regexp(regex='[0-9]{5}', flags=re.MULTILINE, message='Supported czech postalcode format')])

    street = StringField(name='street', label='Street of temporary',
                              validators=[validators.Length(min=2, max=32)])
    city = StringField(name='city', label='City or temporary',
                            validators=[validators.Length(min=2, max=32)])
    postalcode = StringField(name='postalcode', label='Zip of temporary',
                                  validators=[validators.Regexp(regex='[0-9]{5}', flags=re.MULTILINE, message='Supported czech postalcode format')])
    email = StringField(name='email', label='Email',
                        validators=[validators.Email(message='Invalid email address')])
    password = PasswordField(name='password', label='Password', validators=[
        validators.InputRequired(message='Passwords must contain at least six characters'),
        validators.Length(min=8, max=32)])
    password_repeat = PasswordField(name='password_repeat', label='Repeat password',
                                    validators=[validators.InputRequired(), validators.EqualTo(fieldname='password',
                                                                                               message='Passwords must match')])
    # Allowed phone number formats: +420XXXXXXXXX, +421XXXXXXXXX, 00420XXXXXXXXX, 00421XXXXXXXXX, 420XXXXXXXXX, 421XXXXXXXXX, +420 XXXXXXXXX, +421 XXXXXXXXX, 00420 XXXXXXXXX, 00421 XXXXXXXXX, 420 XXXXXXXXX, 421 XXXXXXXXX
    phone = StringField(name='phone', label='Phone number', validators=[validators.Regexp(
        regex=r'^((\+)?|(00))((420)|(421))(\s)?(\d{9})$', flags=re.MULTILINE,
        message='Phone number must be in format +420XXXXXXXXX or +421XXXXXXXXX')],
                        render_kw={'placeholder': '+420XXXXXXXXX'})


class CollectionForm(Form):
    weight = StringField(name='weight', label='Weight', validators=[validators.InputRequired(), validators.Regexp(regex=r'^\d+(\.(\d)+)?$', flags=re.MULTILINE, message='Supported price formatting: 123 (integer) or 123.00 (float)')])
    description = TextAreaField(name='description', label='Description', validators=[validators.InputRequired()])
    email = StringField(name='email', label='Email', validators=[validators.InputRequired(), validators.Email(message='Invalid email address')])
