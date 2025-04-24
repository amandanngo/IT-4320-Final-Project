from flask import Blueprint, render_template

#Set Up SQLAlchemy


admin_bp = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')

# GET route that takes user to login page
@admin_bp.route('/login')
def admin_login():
    pass

#POST route that attempts to login user
#Redirects to Admin dashboard upon successful login
@admin_bp.route('/admin',)
def admin_login_post():
    pass