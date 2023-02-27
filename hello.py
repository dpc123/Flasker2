from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#create an instance of flask
app = Flask(__name__)
#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#secret key
app.config['SECRET_KEY'] = "dpc123"
#initialise the database
db = SQLAlchemy(app)

#create a model
class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)

	#create a string
	def __repr__(self):
		return '<Name %r>' % self.name


#create a form class
class NamerForm(FlaskForm):
	name = StringField("What's your name?", validators=[DataRequired()])
	submit = SubmitField("Submit")




































#create a route decorator
@app.route('/')

#def index():
#	return "<h1>Hello World</h1>"











def index():
	first_name = "John"
	stuff = "This is bold text"
	
	fav_pizza = ['Pepperoni','Cheese', 'Mushroom', 41]
	return render_template("index.html", first_name=first_name, stuff=stuff, fav_pizza=fav_pizza)

#localhost:5000/user/john
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)

#create custom error pages

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

	# internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500




#create name page
@app.route('/name',methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	#Validate form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form submitted Successfully")

	return render_template("name.html", name=name,form=form)


