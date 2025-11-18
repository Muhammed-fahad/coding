class Train:
    def __init__(self,trainName,root,capsity):
        self.trainName = trainName
        self.root = root
        self.capasity = capsity
        self.passengers = []

traindb = {}

def CreateTrain():
    trainNo =int(input("Enter the Train Number: "))
    trainName = input("Enter the train name: ")
    capasity = int(input("Enter the total capacity of the train: "))
    root = list(input("Where all its going sepeteted by (Space): ").split(" "))
    traindb[trainNo] = Train(trainName,root,capasity)

def ChangeRoot():
    trainNo =int(input("Enter the Train Number: "))
    traindb[trainNo].root = list(input("Where all its going sepeteted by (Space): ").split(" "))
    print("Root Canged Succesfully !!")

def CancelTrain():
    trainNo =int(input("Enter the Train Number: "))
    del traindb[trainNo]
    print("Train cancelled Succesfully !!")


def CheckAvailability():
    trainNo = int(input("Enter the Train Number: "))
    if(traindb[trainNo].capasity > 0):
        print(traindb[trainNo].capasity)
    return "No Seats"

def CheckRoot():
    trainNo = int(input("Enter the Train Number: "))
    print(traindb[trainNo].root) 
