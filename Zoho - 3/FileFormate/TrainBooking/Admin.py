import Train
class Admin:
    def __init__(self,name,password):
        self.name = name
        self.paasword = password

adminDB = {}
passwordmain = "FAHAD"

def Main():
    print("1. Create Admin ")
    print("2. Login as a Admin ")

    choice = int(input("Enter the number: "))

    if(choice == 2):
        id = int(input("Enter your id: "))
        password = (input("Enter your password: "))
        if (adminDB[id].paasword == password):
            while(True):
                print("\n1. Create a train Account")
                print("2. Change the Root")
                print("3. Cancel the Train")
                print("4. Check the Root")
                print("5. Exit")

                choice = int(input("Enter the number: "))
                if choice == 1:
                    Train.CreateTrain()
                if choice == 2:
                    Train.ChangeRoot()
                if choice == 3:
                    Train.CancelTrain()
                if choice == 4:
                    Train.CheckRoot()
                if choice == 5:
                    print("Exiting")
                    return 
        
        else:
            print("Wrong password")
    else:
        password = (input("Enter your password: "))
        if(password == passwordmain):
            name = input("Enter your name: ")
            id = int(input("Enter your ID: "))
            passwordadmin = input("Enter Admin new password: ")
            adminDB[id] = Admin(name,passwordadmin)
        else:
            print("Wromg password")

