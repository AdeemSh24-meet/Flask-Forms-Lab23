from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
#app.config['password'] = 123
password = "123"


app.config['password'] = 'password'

facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]

@app.route('/')  # '/' for the default page
def login():
  return render_template('login.html')


# @app.route('/creat')  # '/' for the default page
# def home():
#   return render_template('home.html')

# @app.route('/create, methods=['GET', 'POST'])
# def home():
#     if request.method == 'post':
#         return render_template('home.html')

@app.route('/create',methods=['GET','POST'])
def create():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
		return render_template('home.html')

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
