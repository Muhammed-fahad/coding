from ProductDb import * 
def managerMain():
  
  print("You are Succesfully Login as a Manager....!")
  
  while(True):
    print("1. ADD Product")
    print("2. Delecte Product")
    print("3. Increase produdct quantity ")
    print("4. Log out")
    
    choise = int(input("Enter a number: "))
    if(choise == 1):
      addProduct()
    
    elif(choise == 2):
      deleteProduct()
    
    elif(choise == 3):
      increaseProductQuantity()
    
    elif(choise == 4):
      return
    
    else:
      print("Wrong input")