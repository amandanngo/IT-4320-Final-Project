# reservation/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Reservation
from data_processing import create_ticket_no

res_bp = Blueprint('reservation', __name__, template_folder='templates', url_prefix='/reservation')

def build_seats():
    """Creates a 12×4 grid of 'O' then marks taken seats as 'X'."""
    seats = [['O' for _ in range(4)] for _ in range(12)]
    for r in Reservation.query.all():
        seats[r.seatRow][r.seatColumn] = 'X'
    return seats

@res_bp.route('/form', methods=['GET'])
def show_form():
    seating = build_seats()
    return render_template('reservation_form.html', seating=seating)

@res_bp.route('/create', methods=['POST'])
def reservation_create():
    first_name = request.form.get('firstName', '').strip()
    last_name = request.form.get('lastName', '').strip()
    passenger_name = f"{first_name} {last_name}".strip()
    seat_row       = int(request.form.get('seatRow'))
    seat_column    = int(request.form.get('seatColumn'))

    # 1) Check if seat is already reserved
    if Reservation.query.filter_by(seatRow=seat_row, seatColumn=seat_column).first():
        flash("That seat is already assigned. Please choose another.", "error")
    else:
        # 2) Reserve it
        initials = ''.join([c for c in passenger_name.upper() if c.isalpha()])[:3]
        ticket_number = f"{initials}-INFOTC4320"

        new_res = Reservation(
            passengerName=passenger_name,
            seatRow=seat_row,
            seatColumn=seat_column,
            eTicketNumber=ticket_number
        )
        db.session.add(new_res)
        db.session.commit()
        flash(
            f"Congratulations {passenger_name}! "
            f"Seat {seat_row}-{seat_column} is now reserved for you. Enjoy your trip! "
            f"Your eTicket number is: {ticket_number}",
            "success"
        )

    # 3) Re-render the form with updated chart + any flash
    return redirect(url_for('reservation.show_form'))