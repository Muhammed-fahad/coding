from BusDb import whichBusGoingThere , bookBus , calculatePrice
from AdminMenu import adminMenu

class UserDb:
  def __init__(self , name , password , busNumber = 0):
    self.name = name
    self.password = password
    self.busNumber = busNumber

userdb = {}

def bookTicket():
  ID = int(input("Enter your id number: "))
  password = input("Enter Password: ")
  user = userdb.get(ID)
  
  if(user and user.password == password):
    BusNumber = bookBus(ID,user)
    if(BusNumber):
      user.busNumber = BusNumber
    
    else:
      print("Sorry There is no bus Available.....!")
  else:
    print("you are not the registered user or password is wrong....!")

def findUserBus():
  ID = int(input("Enter user id number: "))
  user = userdb.get(ID)
  if(user):
    return user.busNumber
  
  

def registerUser():
  name = input("Enter your name : ")
  password = input("Enter your password: ")
  ID = int(input("Enter your id number: "))
  
  while(ID in userdb):
    ID = int(input("your id number is already taken enter new id: "))
        
  userdb[ID] = UserDb(name,password)
  print(f"Hi {name} you are registered succesfully....!")  
  
  

def UserMenu():
  ID = int(input("Enter your id number: "))
  password = input("Enter your password: ")

  # Admin
  if(ID == 101 and password=="admin101"):
    adminMenu()
  
  # Customer
  else:
    while(True):
      print("\n1. Book Ticket")
      print("2. Check buses which are going to destination")
      print("3. Calculate the price")
      print("4. Exit From the user")
      
      choise = int(input("\nEnter the number: "))
      if choise == 1:
        bookTicket()
      
      elif choise == 2:
        source = input("Enter your source: ")
        destination = input("Enter your destination: ")
        print(whichBusGoingThere(source , destination))
        
      elif choise == 3:
        print(calculatePrice())
            
      elif choise == 4:
        return
      
      else:
        print("Wrong Choise")