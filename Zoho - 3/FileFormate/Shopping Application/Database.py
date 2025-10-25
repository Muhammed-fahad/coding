from ManagerFunction import *
from userFunctions import *
from AdminFunction import adminmain


class Database:
  def __init__(self,name,password,job):
    self.name = name
    self.password = password
    self.job = job
    
db = {}
d = Database

def new_user(job = "customer"):
  name = input("Enter your name: ")
  password = int(input("Enter your password: "))
  eid = int(input("Enter user id number: "))  
  db[eid] = d(name, password, job)
  
  print(f"Succesfully {name} entered as {job} ....!")
  
  
def old_user():
  eid = int(input("Enter user id number: "))  
  password = int(input("Enter your password: "))
  user = db.get(eid)
  
  if(user and user.password == password):
    print("you are entered Succesfully....!")
    
    if(user.job == "admin"):
      adminmain()
    
    elif(user.job == "manager"):
      managerMain()
    
    elif(user.job == "customer"):
      userfunctions()
    
    else:
      print("you entered wrong job while u created....!")
      
  else:
    print("You are not a registered user....!")
  
  
def removeManager():
  eid = int(input("Enter user id number: "))
  user = db.get(eid)
  if(user.job == "manager"):
    del db[eid]
    print("Manager Removed succesfully.....!")
  
  else:
    print("The entered user id is not manager id")
  
def changePassword():
  eid = int(input("Enter user id number: "))
  password = int(input("Enter password: "))
  user = db.get(eid)
  
  if(user.password == password):
    db[eid].password = int(input("Enter new password"))
    print("password updated succesfully")
  
  else:
    print("wrong password")

def updateProfile():
  eid = int(input("Enter user id number: "))
  password = int(input("Enter you old password: "))
  user = db.get(eid)
  
  if(user and user.password == password):
    print("Now you can update ur profile")
    name = input("Enter your updated name: ")
    password = int(input("Enter your new password: "))
    db[eid].name = name
    db[eid].password = password
  
  else:
    print("you are a unregistered user...!")