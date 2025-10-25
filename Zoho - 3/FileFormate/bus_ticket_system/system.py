from ticket import Ticket

class BusTicketSystem:
    def __init__(self, total_seats=20):
        self.bookings = {}
        self.ticket_id = 1
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_ticket(self, name, bus_name, seat_number):
        if self.available_seats > 0:
            ticket = Ticket(self.ticket_id, name, bus_name, seat_number)
            self.bookings[self.ticket_id] = ticket
            print(f"Ticket booked successfully! Ticket ID: {self.ticket_id}, Seat Number: {seat_number}")
            self.ticket_id += 1
            self.available_seats -= 1
        else:
            print("No seats available!")

    def cancel_ticket(self, ticket_id):
        if ticket_id in self.bookings:
            del self.bookings[ticket_id]
            self.available_seats += 1
            print(f"Ticket ID {ticket_id} canceled successfully.")
        else:
            print(f"Ticket ID {ticket_id} not found.")

    def display_bookings(self):
        if not self.bookings:
            print("No tickets booked yet.")
        else:
            print("\nTicket ID | Name | Bus | Seat Number")
            print("--------------------------------------")
            for t in self.bookings.values():
                print(f"{t.ticket_id} | {t.name} | {t.bus_name} | {t.seat_number}")

    def check_available_seats(self):
        print(f"Available seats: {self.available_seats}/{self.total_seats}")
