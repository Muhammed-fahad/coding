import User
import Train
from Admin import Main
def main():
    while True:
        print("\n1. Register User")
        print("2. Book Ticket")
        print("3. check Avaiilability")
        print("4. Cancel Ticket")
        print("5. Train Root")
        print("6. Admin User")
        print("7. Delete Account")
        print("8. Check the Root")
        print("9. Exit")

        choice = int(input("Enter the number: "))
        if choice == 1:
            User.CreateUser()
        if choice == 2:
            User.BookTicket()
        if choice == 3:
            Train.CheckAvailability()
        if choice == 4:
            User.CancelTicket()
        if choice == 5:
            Train.CheckRoot()
        if choice == 6:
            Main()
        if choice == 7:
            User.DeleteUser()
        if choice == 8:
            User.CheckRoot()
        if choice == 9:
            break 

main()
