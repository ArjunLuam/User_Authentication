from My_Login_Project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hah
from flask_login import UserMixin
#from below commands we get the database of specific user
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)
class User(db.Model,UserMixin):#(usermixin has all the features of login property)
	__tablename__='users'

	id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(64),unique=True,index=True)
	username=db.Column(db.String(128))
	password_hash=db.Column(db.String(128))

	def __init__(self,email,username,password):
		self.email=email
		self.username=username
		self.password_hash=generate_password_hash(password)
	
	def check_password(self,password):
		return check_password_hah(self.password_hash.password)






