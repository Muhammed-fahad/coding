from user import User
class ATM:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, pin, balance=0):
        if user_id in self.users:
            print("User already registered.")
        else:
            self.users[user_id] = User(pin, balance)
            print(f"User {user_id} registered successfully!")

    def authenticate_user(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            print("Authentication successful.")
            return True
        print("Invalid ID or PIN.")
        return False

    def check_balance(self, user_id):
        if user_id in self.users:
            print(f"Balance: ₹{self.users[user_id].balance}")
        else:
            print("User not found.")

    def withdraw(self, user_id, amount):
        user = self.users.get(user_id)
        if user:
            if user.balance >= amount:
                user.balance -= amount
                user.transactions.append(f"Withdrawn ₹{amount}")
                print(f"₹{amount} withdrawn.")
            else:
                print("Insufficient balance.")
        else:
            print("User not found.")

    def show_transactions(self, user_id):
        user = self.users.get(user_id)
        if user:
            print("Transactions:")
            for txn in user.transactions:
                print(txn)
        else:
            print("User not found.")
