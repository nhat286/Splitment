from flask import Flask, render_template, request, redirect, url_for, abort
#from flask_login import login_required, current_user
#from datetime import strptime
#from server import app, system, auth_manager
import db_operations as db
import roles

app = Flask(__name__,
            static_folder = './templates',
            template_folder = './templates')
#login_manager = LoginManager()
#login_manager.init_app(app)

def user_profile():
    if roles.current_id > -1:
        return {'name': roles.current_user[3], 'email': roles.current_user[1], 'address': roles.current_user[4], 'rating': roles.current_user[5]}
    return None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', user=user_profile())


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['login-email']
        password = request.form['login-password']
        roles.current_id, roles.current_user = db.check_login(email, password)
        if roles.current_id == -1:
            return render_template('login.html', error=1)
        print(roles.current_user)
        return redirect(url_for('index'))
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
        return redirect(url_for('index'))
    return render_template('signup.html', error=0)

@app.route('/createGroup', methods=['POST','GET'])
def createGroup():
    if request.method == 'POST':
        creator = roles.current_id
        shop = request.form['ngo-order']
        site = request.form['ngo-order-url']
        address = request.form['ngo-location']
        deadline = request.form['ngo-deadline']
        max_member = request.form['ngo-members']
        # system.createGroup( creator, site, address, date)    
        group = {'admin': creator, 'member_count': 1, 'max_member': max_member}
        print(group)
        print(roles.current_user)
        group_id = db.add_group(group)
        if group_id > -1:
            order = {'group_id': group_id, 'deadline': deadline, 'location': address, 'retail_name': shop, 'retail_link': site}
            if db.add_order(order) == -1:
                return render_template('newGroupOrder.html', error=2)
        else:
            return render_template('newGroupOrder.html', error=1)
        return redirect(url_for('index'))
    return render_template('newGroupOrder.html', error=0)

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method=='POST':
        return render_template('', result=result)
    return redirect('/')

@app.route('/logout', methods=['GET'])
def logout():
    roles.current_id = -1
    roles.current_user = None
    return redirect(url_for('index'))

app.run(debug=True)
 
