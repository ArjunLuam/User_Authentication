from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

#used for login the user
class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	submit=SubmitField('Log in')
#used for registrations
class RegistrationForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	username=StringField('Username',validators=[DataRequired()])
	password=PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm'),messege='Passwords must match'])
	pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
	submit=SubmitField('Register!')


	def check_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered')

	def check_username(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Username already registered')
	



