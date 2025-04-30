from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# "admins" table
class Admin(db.Model):
    __tablename__ = 'admins'
    
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)

# "reservations" table
class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passengerName = db.Column(db.String, nullable=False)
    seatRow = db.Column(db.Integer, nullable=False)
    seatColumn = db.Column(db.Integer, nullable=False)
    eTicketNumber = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.current_timestamp())
