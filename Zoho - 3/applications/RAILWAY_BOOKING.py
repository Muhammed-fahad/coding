tickets = {}
ticket_id = 1

def book_ticket(name, train, seat_class):
    global ticket_id
    tickets[ticket_id] = {'name': name, 'train': train, 'class': seat_class}
    print(f"Ticket booked successfully with Ticket ID {ticket_id}.")
    ticket_id += 1

def cancel_ticket(ticket_id):
    if ticket_id in tickets:
        del tickets[ticket_id]
        print(f"Ticket ID {ticket_id} canceled successfully.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

def display_tickets():
    if not tickets:
        print("No tickets booked.")
    else:
        print("ID | Name | Train | Class")
        print("-----------------------------------")
        for ticket_id, details in tickets.items():
            print(f"{ticket_id} | {details['name']} | {details['train']} | {details['class']}")

def main():
    while True:
        print("\nRailway Ticket Booking System")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Display Tickets")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter Passenger Name: ")
            train = input("Enter Train Name: ")
            seat_class = input("Enter Seat Class: ")
            book_ticket(name, train, seat_class)
        elif choice == "2":
            ticket_id_to_cancel = int(input("Enter Ticket ID to Cancel: "))
            cancel_ticket(ticket_id_to_cancel)
        elif choice == "3":
            display_tickets()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
