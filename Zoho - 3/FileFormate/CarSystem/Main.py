from Admin import Admin
def main():
    def checkPassword():
        pass

    while True:
        print("1. Register User")
        print("2. Book Car")
        print("3. Cancel Ticket")
        print("4. Time check")
        print("5. Cancel Ticket")
        print("6. Admin User")
        print("7. Check the Price")
        print("8. Exit")

        choice = int(input("Enter the number: "))
        if choice == 1:
            pass

        elif choice == 6:
            name = "FAHAD"
            password = 90921

            name1 = input("Enter your name: ")
            password1 = int(input("Enter the password: "))
            if (name==name1 and password==password1):
                Admin.main()

        elif choice == 8:
            print("Exiting.....!")
            break

        elif(checkPassword()):
            if choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
        


if __name__ == "__main__":
    main()