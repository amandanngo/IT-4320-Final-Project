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
            'reservation_row': reservations.seatRow,
            'reservation_column': reservations.seatColumn,
            'reservation_ticket': reservations.eTicketNumber
        })
           
        return reservation
    
    def display_reservation_list():
       reservation_info = []

       reservations = SeatingChart.reservation_list()

       for reservationElements in reservations:
           reservation_info.append(f"{reservationElements['reservation_name']}: row {reservationElements['reservation_row']} seat{reservationElements['reservation_column']} - ticket confirmation: {reservationElements['reservation_ticket']}") 

       convertToString = '' 
       for string in reservation_info: ##https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
           convertToString += string + '\n'

       return convertToString 
           
    def delete_reservation_info():
       reservation_info = []

       reservations = SeatingChart.reservation_list()

       for r in reservations:
           reservation_info.remove