from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from data_processing import SeatingChart
from models import db, Admin, Reservation

#Set Up SQLAlchemy


admin_bp = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')

# GET route that takes user to login page
@admin_bp.route('/login', methods=['GET'])
def admin_login():
    return render_template('login.html')

#POST route that attempts to login user
#Redirects to Admin dashboard upon successful login
@admin_bp.route('/admin',)
def admin_login_post():
    username = request.form['username']
    password = request.form['password']
    
    admin = Admin.query.filter_by(username=username, password=password).first()

    if admin:
        session['admin_logged_in'] = True
        return redirect(url_for('admin.admin_dashboard'))
    else:
        flash('Invalid username or password.')
        return redirect(url_for('admin.admin_login'))

#GET route: admin dashboard page
def admin_dashboard():
    pass

