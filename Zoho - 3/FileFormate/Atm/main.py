from atm import ATM
def main():
    atm = ATM()
    while True:
        print("\n--- ATM Menu ---")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Check Balance")
        print("4. Withdraw")
        print("5. Transactions")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == '1':
            user_id = input("User ID: ")
            pin = input("PIN: ")
            balance = float(input("Initial Balance: "))
            atm.register_user(user_id, pin, balance)

        elif choice == '2':
            user_id = input("User ID: ")
            pin = input("PIN: ")
            atm.authenticate_user(user_id, pin)

        elif choice == '3':
            user_id = input("User ID: ")
            atm.check_balance(user_id)

        elif choice == '4':
            user_id = input("User ID: ")
            amount = float(input("Amount: "))
            atm.withdraw(user_id, amount)

        elif choice == '5':
            user_id = input("User ID: ")
            atm.show_transactions(user_id)

        elif choice == '6':
            print("Bye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()