class Bus:
  def __init__(self,busName , busNumber , capasity , busgoingareas):
    self.busName = busName
    self.busNumber = busNumber
    self.capasity = capasity
    self.busgoingareas = busgoingareas
    self.passengers = {}

busdb = {}  

def newbus():
  busName = input("Enter Bus name: ")
  busNumber = int(input("Enter Bus number: "))
  capasity = int(input("Enter the bus capacity: "))
  busgoingareas = input("Enter all the destinations with the gap: ").split()
  busdb[busNumber] = Bus(busName,busNumber,capasity,busgoingareas)  
  print(f"{busName} bus was created Succesfully....!")

def whichBusGoingThere(source,destination):
  for busnumber,details in busdb.items():
    if((source in details.busgoingareas) and (destination in details.busgoingareas)):
      return busnumber
  return False

def bookBus(ID , user):
  source = input("Enter your source: ")
  destination = input("Enter your destination: ")
  busNumber = whichBusGoingThere(source,destination)
  
  if((busNumber) and (busdb[busNumber].capasity > 0)):
    busdb[busNumber].passengers[ID] = user
    busdb[busNumber].capasity -= 1
    print(f"Bus {busNumber} Booked Succesfully....!")
    return busNumber
  
  else:
    return False

def changeBusRoot():
  busNumber = int(input("Enter Bus number: "))
  busgoingareas = input("Enter all the destinations with the gap: ").split()
  busdb[busNumber].busgoingareas = busgoingareas
  
def NumberOfPassengers():
  busNumber = int(input("Enter Bus number: "))
  print(len(busdb[busNumber].passengers))

def detailsOfPassengers():
  busNumber = int(input("Enter Bus number: "))
  details = busdb[busNumber].passengers
  print("  ID  ||  Name  ")
  for id , deta in details.items():
    print(f"  {id}  ||  {deta.name}")

def calculatePrice():
  source = input("Enter the Starting point: ")
  destination = input("Enter the destination you want to go: ")
  ID = whichBusGoingThere(source,destination)
  return abs(busdb[ID].busgoingareas.index(source) - busdb[ID].busgoingareas.index(destination))*15