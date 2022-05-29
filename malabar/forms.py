from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from flask_login import current_user
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from malabar.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Usuario', [DataRequired(), Length(min=3, max=20)])
	email = StringField('Email', [DataRequired(), Length(min=3, max=20), Email(message='invalid email')])
	password = PasswordField('Contraseña', [DataRequired(), Length(min=4, max=20)])
	confirm_password = PasswordField('Confirmar Contraseña', [DataRequired(), EqualTo('password', message="las contraseñas no coinciden"), Length(min=4, max=20)])
	submit = SubmitField('Listo')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Ese usuario ya esta tomado')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('Ese Email ya esta tomado')

class LoginForm(FlaskForm):
	email = StringField('Email', [DataRequired()])
	password = PasswordField('Password', [DataRequired()])
	remember = BooleanField('Keep me logged in')
	submit = SubmitField('Log in')


class UpdateAccountForm(FlaskForm):
	username = StringField('Usuario', [DataRequired(), Length(min=3, max=20)])

	email = StringField('Email', [DataRequired(), Length(min=3, max=20),
		Email(message='invalid email')])

	submit = SubmitField('Actualizar')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Ese usuario ya esta tomado')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()

			if user:
				raise ValidationError('Ese Email ya esta tomado')


class ShippingForm(FlaskForm):
	first_name = StringField('First name', Length(min=3, max=20))
	last_name = StringField('Last name', Length(min=3, max=20))
	adress = StringField('Adress', Length(max=30), [DataRequired()])
	number = IntegerField('Phone', [DataRequired(), Length(max=15)])
	apartment = StringField('Apartment, Suite, etc. (optional)', [Length(max=20)])
	city = StringField('City', [DataRequired(), Length(max=20)])
	country = StringField('country', [DataRequired(), Length(max=20)])
