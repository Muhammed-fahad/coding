class ATM:
    def __init__(self):
        self.users = {}
        self.transaction_history = {}

    def register_user(self, user_id, pin, balance=0):        
        while user_id in self.users:
            print("User already registered.")
            user_id = input("Enter new User ID: ")
            pin = input("Enter PIN: ")
            balance = float(input("Enter Initial Balance: "))

        self.users[user_id] = {'pin': pin, 'balance': balance}
        self.transaction_history[user_id] = []
        print(f"User {user_id} registered successfully !")

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id]['pin'] == pin:
            print("Authentication successful.")
            return True
        else:
            print("Invalid user ID or PIN.")
            return False

    def check_balance(self, user_id):
        if user_id in self.users:
            balance = self.users[user_id]['balance']
            print(f"Current balance: {balance}")
        else:
            print("User not found.")

    def withdraw_cash(self, user_id, amount):
        if user_id in self.users:
            if self.users[user_id]['balance'] >= amount:
                self.users[user_id]['balance'] -= amount
                self.transaction_history[user_id].append(f"Withdrawn: {amount}")
                print(f"Withdrawal successful. Dispensed {amount}.")
            else:
                print("Insufficient balance.")
        else:
            print("User not found.")

    def view_transaction_history(self, user_id):
        if user_id in self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history[user_id]:
                print(transaction)
        else:
            print("No transactions found.")

def main():
    atm = ATM()
    
    while True:
        print("\n ATM System")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Check Balance")
        print("4. Withdraw Cash")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")
            balance = float(input("Enter Initial Balance: "))
            atm.register_user(user_id, pin, balance)
            
        elif choice == "2":
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")
            atm.authenticate_user(user_id, pin)
            
        elif choice == "3":
            user_id = input("Enter User ID: ")
            atm.check_balance(user_id)
            
        elif choice == "4":
            user_id = input("Enter User ID: ")
            amount = float(input("Enter Amount to Withdraw: "))
            atm.withdraw_cash(user_id, amount)
            
        elif choice == "5":
            user_id = input("Enter User ID: ")
            atm.view_transaction_history(user_id)
            
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()