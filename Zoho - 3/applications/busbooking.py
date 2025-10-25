class BusTicketBooking:
    def __init__(self, total_seats=20):
        self.bookings = {} 
        self.ticket_id = 1 
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_ticket(self, name, bus_name, seat_number):
        if self.available_seats >= 1:
            self.bookings[self.ticket_id] = {'name': name, 'bus_name': bus_name, 'seat_number': seat_number}
            print(f"Ticket booked successfully! Ticket ID: {self.ticket_id}, Seat Number: {seat_number}")
            self.ticket_id += 1
            self.available_seats -= 1

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
            print("\n Ticket ID | Name | Bus | Seat Number")
            print("--------------------------------------")
            for t_id, details in self.bookings.items():
                print(f"{t_id} | {details['name']} | {details['bus_name']} | {details['seat_number']}")

    def check_available_seats(self):
        print(f"Available seats: {self.available_seats}/{self.total_seats}")

def main():
    system = BusTicketBooking()

    while True:
        print("\nBus Ticket Booking System")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Bookings")
        print("4. Check Available Seats")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Passenger Name: ")
            bus_name = input("Enter Bus Name: ")
            seat_number = int(input("Enter Seat Number: "))
            system.book_ticket(name, bus_name, seat_number)

        elif choice == "2":
            ticket_id = int(input("Enter Ticket ID to Cancel: "))
            system.cancel_ticket(ticket_id)

        elif choice == "3":
            system.display_bookings()

        elif choice == "4":
            system.check_available_seats()

        elif choice == "5":
            print("Exiting... Thank you for using the Bus Ticket Booking System!")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()