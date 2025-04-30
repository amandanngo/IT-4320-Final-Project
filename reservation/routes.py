#routes/views for the main sections of the app
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Reservation
from data_processing import create_ticket_no

res_bp = Blueprint('reservation', __name__, template_folder='templates', url_prefix='/reservation')

#Create entry in 'reservations' table in db
@res_bp.route('/create', methods=['POST'])
def reservation_create():
    #Get info from form
    passenger_name = request.form.get('passengerName')
    seat_row = int(request.form.get('seatRow'))
    seat_column = int(request.form.get('seatColumn'))
    
    #Generate confirmation code
    ticket_number = create_ticket_no(passenger_name)

    #Add entry using SQLAlchemy
    new_res = Reservation(
        passengerName=passenger_name,
        seatRow=seat_row,
        seatColumn=seat_column,
        eTicketNumber=ticket_number
    )
    db.session.add(new_res)
    db.session.commit()

    #Display order confirmation on page
    return render_template('confirmation.html', name=passenger_name, code=ticket_number)

@res_bp.route('/delete/<int:id>', methods=['POST'])
def reservation_delete(id):
    #get the reservation based on id
    res = Reservation.query.get_or_404(id)

    #delete the reservation
    db.session.delete(res)
    db.session.commit()
    
    flash("Reservation deleted.")
    return redirect(url_for('admin.admin_dashboard'))