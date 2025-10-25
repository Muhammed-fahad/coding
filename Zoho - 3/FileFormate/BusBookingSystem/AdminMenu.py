from BusDb import *
from UserDb import findUserBus
def adminMenu():
  while(True):
    print("1. Create a new bus")
    print("2. Change the root")
    print("3. Number of passengers in the bus")
    print("4. Details of the passengers travelling in the bus")
    print("5. ID to find which bus he is travelling")
    print("6. Exit from the admin")
    
    try:
      choise = int(input("Enter your choise: "))
    
    except ValueError:
      print("Enter int type of data you enter String trype of data")
    
    if(choise == 1):
      newbus()
    
    elif(choise == 2):
      changeBusRoot()
    
    elif choise == 3:
      NumberOfPassengers()
    
    elif choise == 4:
      detailsOfPassengers()
    
    elif choise == 5:
      findUserBus()
    
    elif(choise == 6):
      return
    
    else:
      print("You enter wrong option")
    