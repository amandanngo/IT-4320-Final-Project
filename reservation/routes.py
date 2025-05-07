#routes/views for the main sections of the app
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Reservation
from data_processing import create_ticket_no

res_bp = Blueprint('reservation', __name__, template_folder='templates', url_prefix='/reservation')

@res_bp.route('/form', methods=['GET'])
def show_form():
    # Seating chart should be passed from your data_processing class
    from data_processing import SeatingChart
    chart = SeatingChart()
    return render_template('reservation_form.html', seating=chart.seats)

#Create entry in 'reservations' table in db
@res_bp.route('/create', methods=['POST'])
def reservation_create():
    from data_processing import SeatingChart

    #Get info from form
    passenger_name = request.form.get('passengerName')
    seat_row = int(request.form.get('seatRow'))
    seat_column = int(request.form.get('seatColumn'))

    #Check if seat is already assigned
    existing = Reservation.query.filter_by(seatRow=seat_row, seatColumn=seat_column).first()
    if existing:
        flash(f"That seat is already assigned. Choose again.", "error")

        #Reload seating chart
        chart = SeatingChart()
        reservations = Reservation.query.all()
        for r in reservations:
            chart.seats[r.seatRow][r.seatColumn] = 'X'
        return render_template('reservation_form.html', seating=chart.seats)
    
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
    flash(f"Congratulations {passenger_name}! Seat: {seat_row}-{seat_column} is now reserved for you. Enjoy your trip!"
          f" Your eticket number is: {ticket_number}")
    
    chart = SeatingChart()
    reservations = Reservation.query.all()
    for r in reservations:
        chart.seats[r.seatRow][r.seatColumn] = 'X'
        
    return render_template('reservation_form.html', seating=chart.seats)

@res_bp.route('/delete/<int:id>', methods=['POST'])
def reservation_delete(id):
    #get the reservation based on id
    res = Reservation.query.get_or_404(id)

    #delete the reservation
    db.session.delete(res)
    db.session.commit()
    
    flash("Reservation deleted.")
    return redirect(url_for('admin.admin_dashboard'))