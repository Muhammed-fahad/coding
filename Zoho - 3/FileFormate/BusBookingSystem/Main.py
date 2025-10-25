from UserDb import registerUser , UserMenu

def main():
  while(True):
    print("\n1. New User")
    print("2. Registered User")
    print("3. Exit From the app")
    
    try:
      choise = int(input("\nEnter the number: "))
    except ValueError:
      print("you may enter String type of data Check properly")
      
    if choise == 1:
      registerUser()
    
    elif choise == 2:
      UserMenu()
    
    elif choise == 3:
      print("Exiting....!")
      return
    
    else:
      print("you entered wrong choise...!")


if __name__ == "__main__":
  main()