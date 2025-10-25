class FlightReservationSystem:
    def __init__(self):
        self.flights = {}
        self.flight_id = 1

    def book_flight(self, name, flight, seat_class):
        """Books a flight for a passenger."""
        self.flights[self.flight_id] = {'name': name, 'flight': flight, 'class': seat_class}
        print(f"Flight booked successfully with Flight ID {self.flight_id}.")
        self.flight_id += 1 

    def cancel_flight(self, flight_id):
        if flight_id in self.flights:
            del self.flights[flight_id]
            print(f"Flight ID {flight_id} canceled successfully.")
        else:
            print(f"Flight ID {flight_id} not found.")

    def display_flights(self):
        """Displays all booked flights."""
        if not self.flights:
            print("No flights booked.")
        else:
            print("\nID | Name | Flight | Class")
            print("-----------------------------")
            for f_id, details in self.flights.items():
                print(f"{f_id} | {details['name']} | {details['flight']} | {details['class']}")

def main():
    system = FlightReservationSystem()

    while True:
        print("\nFlight Reservation System")
        print("1. Book Flight")
        print("2. Cancel Flight")
        print("3. Display Flights")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Passenger Name: ")
            flight = input("Enter Flight Name: ")
            seat_class = input("Enter Seat Class: ")
            system.book_flight(name, flight, seat_class)

        elif choice == "2":
            flight_id_to_cancel = int(input("Enter Flight ID to Cancel: "))
            system.cancel_flight(flight_id_to_cancel)

        elif choice == "3":
            system.display_flights()

        elif choice == "4":
            print("Exiting... Thank you for using the Flight Reservation System!")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
