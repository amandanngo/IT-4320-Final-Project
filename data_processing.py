from models import db, Admin, Reservation

def create_ticket_no(name):
    #mashes up user's name with "INFOTC4320" to create ticket number
    pass

class SeatingChart:

    def get_cost_matrix():
        cost_matrix = [[100, 75, 50, 100] for row in range(12)]
        return cost_matrix

    def calculate_total_sales():
        reservations = Reservation.query.all()
        cost_matrix = SeatingChart.get_cost_matrix()

        for r in reservations:
            totalCost = cost_matrix[r.seatRow][r.seatColumn]
       
        return totalCost


    def display_seating_chart():
        pass