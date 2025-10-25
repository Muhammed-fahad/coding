class RailwayReservationSystem:
    def __init__(self):
        self.coaches = {
            "AC": {"seats": 60, "waiting_list": 10, "booked": [], "waiting": []},
            "Non-AC": {"seats": 60, "waiting_list": 10, "booked": [], "waiting": []},
            "Seater": {"seats": 60, "waiting_list": 10, "booked": [], "waiting": []}
        }

    def check_availability(self, coach_type):
        """Check available seats and waiting list status."""
        if coach_type in self.coaches:
            coach = self.coaches[coach_type]
            available_seats = coach["seats"] - len(coach["booked"])
            waiting_spots = coach["waiting_list"] - len(coach["waiting"])
            print(f"Available Seats: {available_seats}, Waiting List Spots: {waiting_spots}")
        else:
            print("Invalid Coach Type!")

    def book_ticket(self, name, coach_type):
        """Book a ticket in the specified coach type."""
        if coach_type not in self.coaches:
            print("Invalid Coach Type!")
            return

        coach = self.coaches[coach_type]

        if len(coach["booked"]) < coach["seats"]:
            coach["booked"].append(name)
            print(f"Ticket booked for {name} in {coach_type} Coach.")
        elif len(coach["waiting"]) < coach["waiting_list"]:
            coach["waiting"].append(name)
            print(f"{name} added to the waiting list for {coach_type} Coach.")
        else:
            print("No seats or waiting list spots available.")

    def cancel_ticket(self, name, coach_type):
        """Cancel a booked ticket and update the waiting list."""
        if coach_type not in self.coaches:
            print("Invalid Coach Type!")
            return

        coach = self.coaches[coach_type]

        if name in coach["booked"]:
            coach["booked"].remove(name)
            print(f"Ticket cancelled for {name} in {coach_type} Coach.")
            # Move first waiting list person to confirmed booking
            if coach["waiting"]:
                moved_person = coach["waiting"].pop(0)
                coach["booked"].append(moved_person)
                print(f"{moved_person} moved from waiting list to confirmed booking.")
        elif name in coach["waiting"]:
            coach["waiting"].remove(name)
            print(f"{name} removed from the waiting list in {coach_type} Coach.")
        else:
            print(f"{name} does not have a booking in {coach_type} Coach.")

    def prepare_chart(self):
        """Display the final list of booked passengers."""
        print("\n===== Final Reservation Chart =====")
        for coach_type, details in self.coaches.items():
            print(f"\n{coach_type} Coach:")
            print(f"Booked Seats ({len(details['booked'])}/{details['seats']}): {details['booked']}")
            print(f"Waiting List ({len(details['waiting'])}/{details['waiting_list']}): {details['waiting']}")


# Example Usage
system = RailwayReservationSystem()
system.book_ticket("Alice", "AC")
system.book_ticket("Bob", "AC")
system.check_availability("AC")
system.cancel_ticket("Alice", "AC")
system.prepare_chart()
