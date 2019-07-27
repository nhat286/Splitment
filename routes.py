from flask import Flask, render_template, request, redirect, url_for, abort
#from flask_login import login_required, current_user
#from datetime import strptime
#from server import app, system, auth_manager
import db_operations as db

app = Flask(__name__,
            static_folder = './templates',
            template_folder = './templates')
#login_manager = LoginManager()
#login_manager.init_app(app)

current_id = -1
current_user = None

@app.route('/', methods=['GET'])
def index():
    if current_id > -1:
        return render_template('index.html', user=current_user)
    return render_template('index.html', user=None)


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['login-email']
        password = request.form['login-password']
        current_id, current_user = db.check_login(email, password)
        if current_id == -1:
            return render_template('login.html', error=1)
        print(current_user)
        user = {'name': current_user[3], 'email': current_user[1], 'address': current_user[4], 'rating': current_user[5]}
        return render_template('index.html', user=user)
    return render_template('login.html', error=0)

@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        name = request.form['signup-name']
        email = request.form['signup-email']
        password = request.form['signup-password']
        address = request.form['signup-address']
        user = {'email': email, 'password': password, 'name': name, 'address': address, 'rating': 0}
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
        group = {'admin': creator, 'member_count': 1, 'max_member': 5}
        db.add_group(group)
        return redirect('/')
    return render_template('createGroup.html')

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method=='POST':
        return render_template('', result=result)
    return redirect('/')

@app.route('/logout', methods=['GET'])
def logout():
    current_id = -1
    current_user = None
    return redirect('/')

app.run(debug=True)
 
