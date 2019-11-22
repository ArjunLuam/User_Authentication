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
@app.route('/logout')
@login_required
def logout():
	flash("You logged out")
	return redirect(url_for('home'))
@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()

		if user.check_password(form.password.data) and user is not None:
			login_user(user)
			flash('Logged in Sucessfully!')

			next=request.args.get('next') #immidiatly before logging in flask saves this as our next page and redirects it
			if next == None or not next[0]=='/':
				next=url_for('Welcome_user')

			return redirect(next)
	return render_template('login.html',form=form)		

@app.route('/register',methods=['GET','POST'])
def register():
	form=RegistrationForm()

	if form_validate_on_submit():
		User=User(email=form.email,data,username=form.username.data,password=form.password.data)

		db.session.add(user)
		db.session.commit()
		flash("Thanks for registration")
		return redirect(url_for('login'))
	return render_template('register.html',form=form)

if __name__ == '__main__':
	app.run()			
