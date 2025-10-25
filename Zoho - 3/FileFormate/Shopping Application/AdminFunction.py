from ProductDb import *
from Database import *

def adminmain():
  print("You are Succesfully Login as a Admin....!")
  
  while(True):
    print("1. ADD Product")
    print("2. Delecte Product")
    print("3. Increase produdct quantity ")
    print("4. Add manager")
    print("5. Remove manager")
    print("6. Log out")
    
    choise = int(input("Enter a number: "))
    if(choise == 1):
      addProduct()
    
    elif(choise == 2):
      deleteProduct()
    
    elif(choise == 3):
      increaseProductQuantity()
    
    elif(choise == 4):
      new_user("manager")
    
    elif(choise == 5):
      removeManager()
    
    elif(choise == 6):
      return