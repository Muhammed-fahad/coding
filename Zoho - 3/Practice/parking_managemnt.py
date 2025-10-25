class parking:
  def __init__(self,Parking_slot):
    self.Parking_slot = Parking_slot
    self.vehicle_id = 1
    self.occupied_slot = {}
  
  def park_vehicle(self):
    if len(self.occupied_slot) < parking_slot :
      number = input("Enter vehicle number:")
      v_type = input("Enter vehicle type car/bike: ")
    else:
      print("Sorry the parking slot is full")
      return
    
    self.occupied_slot[self.vehicle_id] = {'number': number , 'Type': v_type}
    self.vehicle_id += 1
    print("Your Vehicle is parked succesfully")
  
  def remove_vehicle(self,vehicle_id):
    del self.occupied_slot[vehicle_id]
    print("Your vehicle was removed")
  
  def show_vehicle(self):
    print("ID  ||  Number  ||  Type")
    print("------------------------")
    for v_i, details in self.occupied_slot.items():
      print(f"{v_i}  ||  {details['number']}  || {details['Type']}\n")
      
    

parking_slot = int(input("Enter Total Numbers of vechical can accomudate: "))
park = parking(parking_slot)
while(True):
  print("1. Park Your vehicle")
  print("2. Take ur vehicle")
  print("3. See the parking vehicle")
  print("4. Exit\n")
  choice = int(input("Enter Your Choice: "))
  if(choice == 1):
    park.park_vehicle()
  
  if(choice == 2):
    v_id = int(input("Enter your ID: "))
    park.remove_vehicle(v_id)
  
  if (choice == 3):
    park.show_vehicle()
  
  if(choice == 4):
    break