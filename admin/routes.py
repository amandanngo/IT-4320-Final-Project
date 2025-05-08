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
@admin_bp.route('/login', methods=['POST'])
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
@admin_bp.route('/dashboard', methods=['GET'])
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash('Please login first.')
        return redirect(url_for('admin.admin_login'))
    
    reservations = Reservation.query.all()
    seating_chart = SeatingChart.display_seating_chart()
    reservation_list = SeatingChart.display_reservation_list()

    # Mark the selected reserved seats
    # for r in reservations:
    #     seating_chart.toggle_seat(r.seatRow, r.seatColumn)
    
    total_sales = SeatingChart.calculate_total_sales()

    return render_template('admin.html', total_sales=total_sales, seating_chart=seating_chart, reservation_list=reservation_list)

    
    

#Delete the reservation
@admin_bp.route('/delete/<int:id>', methods=['POST'])
def delete_reservation(id):
    if not session.get('admin_logged_in'):
        flash(('Please log in first.'))
        return redirect(url_for('admin.admin_login'))
    
    res = Reservation.query.get_or_404(id)
    db.session.delete(res)
    db.session.commit()
    flash("Reservation deleted.")
    return redirect(url_for('admin.admin_dashboard'))
    



#Log out the admin
@admin_bp.route('/logout', methods=['POST'])
def admin_logout():
    session.pop('admin_logged_in', None)
    flash("Logged out succesfully")
    return redirect(url_for('admin.admin_login'))