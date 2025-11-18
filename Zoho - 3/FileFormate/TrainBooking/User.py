import Train
class User:
    def __init__(self,name , password , age):
        self.name = name
        self.password = password
        self.age = age
        self.tickets = []

users = {}
id = 1

def CreateUser():
    global id
    name = input("Enter your name: ")
    password = input("Enter your Password: ")
    age = int(input("Enter age: "))
    users[id] = User(name,password,age)
    print(f"User is Created succesfull with the yser id {id}")
    id+=1    

def DeleteUser():
    id = int(input("Enter your ID: "))
    password = input("Enter your password: ")
    person = users[id]
    if(person and person.password == password):
        del users[id]
    else:
        print("your ID or Password is Worng")

def BookTicket():
    id = int(input("Enter your ID: "))
    password = input("Enter your password: ")
    person = users[id]
    if(person and person.password == password):
        trainNo = int(input("Enter the train Number: "))
        if (trainNo in Train.traindb):
            traindata = Train.traindb[trainNo]
            traindata.capasity -= 1
            Train.traindb[trainNo].passengers.append(id)
            users[id].tickets.append(trainNo)
            print(f"You have Succesfully booked {trainNo} the train")
        else:
            print("No Train is there")

def CancelTicket():
    id = int(input("Enter your ID: "))
    password = input("Enter your password: ")
    person = users[id]
    if(person and person.password == password):
        trainNo = int(input("Enter the train Number: "))
        if trainNo in person.tickets:
            person.tickets.remove(trainNo)
            print("you Succesfully cancelled the ticket !!!")
        else:
            print("Wrong Train number")
    else:
        print("Wrong password")

def ShowTicket():
    id = int(input("Enter your ID: "))
    password = input("Enter your password: ")
    person = users[id]
    if(person and person.id == id and person.password == password):
        for i,j in enumerate(len(person.tickets)):
            print(f"{i}. {j}")
    else:
        print("Wrong password")

def CheckRoot():
    Train.ChangeRoot()