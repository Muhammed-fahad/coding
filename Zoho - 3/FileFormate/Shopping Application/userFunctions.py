from ProductDb import *
from Database import changePassword , updateProfile

def userfunctions():
  print("you are succesfully entered as user")
  
  while(True):
    print("1.Change password")
    print("2.Update profile")
    print("3.viwe products")
    print("4.remove item from cart")
    print("5.view cart")
    print("7.purchase")
    print("8.cancel order")
    print("9.view purchase history")
    
    choise = int(input("Enter your choise: "))
    
    if choise == 1:
      changePassword()
    
    elif choise == 2:
      updateProfile()
    
    elif choise == 3:
      viewProducts()
      
    elif choise == 4:
      pass
    
    elif choise == 5:
      pass
    
    elif choise == 6:
      pass
    
    elif choise == 7:
      print("Now u can buy anything...!")
      buyProduct()
      
    elif choise == 8:
      pass
    
    elif choise == 9:
      pass
    
    else:
      print("Wrong choise")
      continue
    
  