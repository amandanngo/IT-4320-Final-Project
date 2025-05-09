from models import db, Admin, Reservation


class SeatingChart:

    def get_cost_matrix():
        cost_matrix = [[100, 75, 50, 100] for row in range(12)]
        return cost_matrix

    def calculate_total_sales():
        reservations = Reservation.query.all()
        cost_matrix = SeatingChart.get_cost_matrix()

        totalCost = 0

        for r in reservations:
            totalCost += cost_matrix[r.seatRow][r.seatColumn]
       
        return totalCost

    def display_seating_chart():
        seats = [['O' for _ in range(4)] for _ in range(12)]
        for reservations in Reservation.query.all():
            seats[reservations.seatRow][reservations.seatColumn] = 'X'    
        return seats
    
    def reservation_list():
        reservation = []
        for reservations in Reservation.query.all():
           reservation.append({
            'reservation_name': reservations.passengerName,
            'reservation_id': reservations.id,
            'reservation_row': reservations.seatRow,
            'reservation_column': reservations.seatColumn,
            'reservation_ticket': reservations.eTicketNumber})
           
        return reservation
    
   