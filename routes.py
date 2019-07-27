from flask import Flask, render_template, request, redirect, url_for, abort
#from flask_login import login_required, current_user
from datetime import strptime
#from server import app, system, auth_manager
import db_operations as db

app = Flask(__name__)
#login_manager = LoginManager()
#login_manager.init_app(app)

current_id = -1

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', user=None)


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        account = db.check_login(email, password)
        if account == -1:
            return render_template('login.html', error=1)
        current_id = account
        return render_template('index.html', user=account)
    return render_template('login.html', error=0)

@app.route('/signup', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        user = {'email': email, 'password': password, 'name': name, 'address': address, 'rating': rating}
        account = db.add_user(user)
        if account == -1:
            return render_template('signup.html', error=1)
        return redirect('/')
    return render_template('signup.html', error=0)

@app.route('/createGroup', methods=['POST','GET'])
def createGroup():
    if request.method == 'POST':
        creator = current_id
        site = request.form['website']
        address = request.form['address']
        date = request.form['date']
        # system.createGroup( creator, site, address, date)    
        group = {'admin': creator, 'member_count': 0, 'max_member': 0}
        db.add_group(group)
        return redirect('/')
    return render_template('createGroup.html')

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method=='POST':
        return render_template('', result=result)
    return redirect('/')

app.run(debug=True)
 
