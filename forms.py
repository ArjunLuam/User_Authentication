from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import validationError


class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()]
	Submit=SubmitField('Log In')	

class RegistrationForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	username=StringField('username',validators=[DataRequired()])
	password=PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',messege='password must match')])
	pass_confirm=PasswordField('confirm password',validators=[DataRequired()])
	Submit=SubmitField('Register')

	def check_email(self,field):
		if User.query.filter_by(email=field.data).first() #if email has already been activated or registered
		raise validationError('Your email has been already registered')

	def check_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise validationError('username is taken')

