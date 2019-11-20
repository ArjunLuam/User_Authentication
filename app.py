from My_Login_Project import app,db
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user
from My_Login_Project.models import User
from My_Login_Project.forms import LoginForm,RegistrationForm

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/welcome')
@login_required  #in order to see this view,user must b logged in
def welcome_user():
	return render_template('welcome_user.html')	