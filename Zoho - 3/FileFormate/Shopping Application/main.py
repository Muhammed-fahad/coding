from Database import new_user,old_user
def main():
  print("Entering as a admin")
  new_user("admin")
  
  while(True):
    print("Enter 1 fro new user")
    print("Enter 2 fro old user")
    print("Enter 3 for exit")
    
    
    try:
      choise = int(input("Enter a number: "))
      
    except ValueError:
      print("you may entered string data")
      
      
    if(choise == 1):
      new_user()
    
    elif(choise == 2):
      old_user()
    
    elif(choise == 3):
      break
    
    else:
      print("Wrong choise")

if __name__ == "__main__":
  main()