from system import BusTicketSystem

def main():
    system = BusTicketSystem()
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
