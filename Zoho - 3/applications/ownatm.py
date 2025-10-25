class ATM:
  def __init__(self):
    self.user = {}
    self.transaction_data = {}
  
  def register(self,name,user_id,balance):
    if user_id not in self.user:
      self.user[user_id] = {'Name':name , 'Balance':balance}
      self.transaction_data[user_id] = []
      print(f"Account created id - {user_id} name {name}")
    else:
      print(f"User id-{user_id} already Registered")
    
  def withdraw(self,user_id,amount):
    if user_id in self.user:
      if self.user[user_id]['Balance']>=amount:
        self.user[user_id]['Balance'] -= amount
        self.transaction_data[user_id].append(f"withdraw - {amount}")
        avai =self.user[user_id]['Balance']
        print(f"Amount withdrawn {amount} succesfully available bal {avai}")
    else:
      print("ID not Found")
      
  def deposit(self,user_id,amount):
    if user_id in self.user:
      self.user[user_id]['Balance'] += amount
      self.transaction_data[user_id].append(f"Deposited - {amount}")
      avai = self.user[user_id]['Balance']
      print(f"Amount Deposited {amount} succesfully available bal {avai}")
  
  def balance_check(self,user_id):
    if user_id in self.user:
      print(self.user[user_id]['Balance'])
    else:
      print("user not found")
  
  def transaction(self,user_id):
    if user_id in self.transaction_data:
      for i in self.transaction_data[user_id]:
        print(i)

def main():
  atm = ATM()
  
  while True:
    print("ATM MACHINE")
    print("1. Register User")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Balance Check")
    print("5. Transcation History")
    choise = input("Enter your choise: ")

    if choise == "1":
      name = input("Enter your name: ")
      user_id = int(input("Enter user ID: "))
      balance = int(input("Enter amount you want to open with: "))
      atm.register(name,user_id,balance)
      
    elif choise == "2":
      user_id = int(input("Enter user ID: "))
      amount = int(input("Enter amount you want Withdraw: "))
      atm.withdraw(user_id,amount)
      
    elif choise == "3":
      user_id = int(input("Enter user ID: "))
      amount = int(input("Enter amount you want to Deposit: "))
      atm.deposit(user_id,amount)
    
    elif choise == "4":
      userid = int(input("Enter your user_id: "))
      atm.balance_check(userid)
      
    elif choise=="5":
      uid = int(input("Enter user id: "))
      atm.transaction(user_id)

if __name__ == "__main__":
  main()