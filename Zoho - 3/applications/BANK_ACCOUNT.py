class Bank:
    def __init__(self):
        self.accounts = {}  
        self.account_id = 1


    def create_account(self, name, balance):
        if balance < 0:
            print("Initial balance cannot be negative.")
            return
        self.accounts[self.account_id] = {'name': name, 'balance': balance}
        print(f"Account created successfully with Account ID {self.account_id}.")
        self.account_id += 1

    def deposit(self, account_id, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        if account_id in self.accounts:
            self.accounts[account_id]['balance'] += amount
            print(f"Deposited {amount} successfully. New balance: {self.accounts[account_id]['balance']}")
        else:
            print(f"Account ID {account_id} not found.")

    def withdraw(self, account_id, amount):
        """Withdraws money from the given account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if account_id in self.accounts:
            if self.accounts[account_id]['balance'] >= amount:
                self.accounts[account_id]['balance'] -= amount
                print(f"Withdrawn {amount} successfully. Remaining balance: {self.accounts[account_id]['balance']}")
            else:
                print("Insufficient balance.")
        else:
            print(f"Account ID {account_id} not found.")

    def display_accounts(self):
        """Displays all account details."""
        if not self.accounts:
            print("No accounts found.")
        else:
            print("\nID | Name | Balance")
            print("--------------------------")
            for acc_id, details in self.accounts.items():
                print(f"{acc_id} | {details['name']} | {details['balance']}")

def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Accounts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))
            bank.create_account(name, balance)

        elif choice == "2":
            acc_id = int(input("Enter Account ID: "))
            amount = float(input("Enter Amount to Deposit: "))
            bank.deposit(acc_id, amount)

        elif choice == "3":
            acc_id = int(input("Enter Account ID: "))
            amount = float(input("Enter Amount to Withdraw: "))
            bank.withdraw(acc_id, amount)

        elif choice == "4":
            bank.display_accounts()

        elif choice == "5":
            print("Exiting... Thank you for using the Bank Management System!")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()