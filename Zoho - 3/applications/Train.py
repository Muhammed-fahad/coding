class Passenger:
    def __init__(self, name, age, gender, berth_preference):
        self.name = name
        self.age = age
        self.gender = gender
        self.berth_preference = berth_preference
        self.allotted_berth = None

class TrainTicketSystem:
    def __init__(self):
        self.confirmed_tickets = []  # 63 berths
        self.rac_tickets = []  # 18 berths
        self.waiting_list = []  # 10 berths
        self.total_confirmed = 63
        self.total_rac = 18
        self.total_waitlist = 10
        
    def book_ticket(self, passenger):
        if passenger.age < 5:
            print(f"{passenger.name} is under 5 years. No ticket allocated but details stored.")
            return

        if len(self.confirmed_tickets) < self.total_confirmed:
            # Allocate lower berth for senior citizens or women with children
            if passenger.age > 60 or (passenger.gender == 'F' and passenger.berth_preference == 'Lower'):
                passenger.allotted_berth = 'Lower'
            else:
                passenger.allotted_berth = 'Any'
            
            self.confirmed_tickets.append(passenger)
            print(f"Ticket confirmed for {passenger.name}, Berth: {passenger.allotted_berth}")
        
        elif len(self.rac_tickets) < self.total_rac:
            passenger.allotted_berth = 'Side-Lower (RAC)'
            self.rac_tickets.append(passenger)
            print(f"RAC Ticket allotted for {passenger.name}")
        
        elif len(self.waiting_list) < self.total_waitlist:
            passenger.allotted_berth = 'Waiting List'
            self.waiting_list.append(passenger)
            print(f"{passenger.name} added to Waiting List")
        
        else:
            print("No tickets available")
    
    def cancel_ticket(self, name):
        # Cancel from Confirmed Tickets
        for passenger in self.confirmed_tickets:
            if passenger.name == name:
                self.confirmed_tickets.remove(passenger)
                print(f"Ticket cancelled for {name}")
                
                # Move RAC to Confirmed
                if self.rac_tickets:
                    moved_passenger = self.rac_tickets.pop(0)
                    moved_passenger.allotted_berth = 'Any'
                    self.confirmed_tickets.append(moved_passenger)
                    print(f"RAC passenger {moved_passenger.name} moved to Confirmed Ticket")
                    
                    # Move Waiting List to RAC
                    if self.waiting_list:
                        moved_waitlist_passenger = self.waiting_list.pop(0)
                        moved_waitlist_passenger.allotted_berth = 'Side-Lower (RAC)'
                        self.rac_tickets.append(moved_waitlist_passenger)
                        print(f"Waiting List passenger {moved_waitlist_passenger.name} moved to RAC Ticket")
                return
        
        print(f"No ticket found for {name}")
    
    def print_booked_tickets(self):
        print("\n--- Confirmed Tickets ---")
        for p in self.confirmed_tickets:
            print(f"Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Berth: {p.allotted_berth}")
        print(f"Total Confirmed Tickets: {len(self.confirmed_tickets)}/63")
        
        print("\n--- RAC Tickets ---")
        for p in self.rac_tickets:
            print(f"Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Berth: {p.allotted_berth}")
        print(f"Total RAC Tickets: {len(self.rac_tickets)}/18")
        
        print("\n--- Waiting List ---")
        for p in self.waiting_list:
            print(f"Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Berth: {p.allotted_berth}")
        print(f"Total Waiting List Tickets: {len(self.waiting_list)}/10")
    
    def print_available_tickets(self):
        print("\n--- Available Tickets ---")
        print(f"Available Confirmed Tickets: {self.total_confirmed - len(self.confirmed_tickets)}")
        print(f"Available RAC Tickets: {self.total_rac - len(self.rac_tickets)}")
        print(f"Available Waiting List Tickets: {self.total_waitlist - len(self.waiting_list)}")

# Example Usage
train_system = TrainTicketSystem()

train_system.book_ticket(Passenger("Alice", 65, "F", "Lower"))
train_system.book_ticket(Passenger("Bob", 30, "M", "Upper"))
train_system.book_ticket(Passenger("Charlie", 4, "M", "Any"))  # Child under 5
train_system.book_ticket(Passenger("Diana", 28, "F", "Lower"))

train_system.print_booked_tickets()
train_system.cancel_ticket("Bob")
train_system.print_booked_tickets()
train_system.print_available_tickets()