from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from datetime import strptime
#from server import app, system, auth_manager
import db_operations
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
	if current_user.is_authenticated():
	    # search = sytem.createFeedListByLocation();
	else:
	    # search = sytem.createFeedListByDate();
	return render_template('home.html',user = none, searchResults = search)


@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		user = request.form['user']
		password = request.form['password']
		load_user(login)	
		# system.loginUser(user, password)

		return render_template('home.html')
	return render_template('login.html')



@app.route('/createAccount', methods=['POST','GET'])
def createAccount():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		name = request.form['name']
		address = request.form['address']	
		user = new 	
		# system.loginUser(user, password)
		
		return render_template('home.html')
	return render_template('createAccount.html')
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
		if current_user.is_authenticated:
			# list = []
			# location = user.getLocation()
			# groups = system.groups
			# while groups.size() > 0:
				# list.add.groups.max
				# groups.remove.max	
				
			

app.run(debug =True)
 
