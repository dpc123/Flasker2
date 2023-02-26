from flask import Flask, render_template


#create an instance of flask
app = Flask(__name__)

#create a route decorator
@app.route('/')

#def index():
#	return "<h1>Hello World</h1>"











def index():
	first_name = "John"
	stuff = "This is bold text"
	
	fav_pizza = ['Pepperoni','Cheese', 'Mushroom', 41]
	return render_template("index.html",
		first_name=first_name,
		stuff =stuff,
		fav_pizza=fav_pizza)

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


