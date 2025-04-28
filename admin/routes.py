from flask import Blueprint, render_template
from data_processing import SeatingChart

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
    pass