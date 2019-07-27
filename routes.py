from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from datetime import strptime
#from server import app, system, auth_manager

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
	return render_template('home.html',user = none)


@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		user = request.form['user']
		password = request.form['password']
		# system.loginUser(user, password)

		return render_template('home.html')
	return render_template('login.html')

@app.route('/createGroup', methods=['POST','GET'])
@login_required
def createGroup():
	if request.method == 'POST':
		creator = current_user.name
		site = request.form['website']
		address = request.form['address']
		date = request.form['date'] 
		# system.createGroup( creator, site, address, date)	
		return render_template('home.html')	
	return render_template('createGroup.html')

@app.route('/search', methods=['POST','GET'])
def search():
	if request.method=='POST':
		

app.run(debug =True)
 
