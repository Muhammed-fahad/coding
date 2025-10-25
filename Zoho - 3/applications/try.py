class ParkingLot:
    def __init__(self, max_slots=10):
        self.parking_vehicles = {}  
        self.par_id = 1  
        self.max_slots = max_slots 

    def park_vehicle(self, name, bike_num):
        if len(self.parking_vehicles) >= self.max_slots:
            print("Sorry, the parking lot is full!")
            return

        self.parking_vehicles[self.par_id] = {'Name': name, "Bike Number": bike_num}
        print(f"Your bike {bike_num} parked successfully at slot {self.par_id}")
        self.par_id += 1 

    def remove_vehicle(self, bike_num):
        for slot, values in list(self.parking_vehicles.items()):
            if values["Bike Number"] == bike_num:
                del self.parking_vehicles[slot]
                print(f"Your bike {bike_num} removed successfully from slot {slot}")
                return
        return(f"Your bike {bike_num} was not found in the parking lot.")

    def display_parked_vehicles(self):
        print("ID  ||  Name  ||  Bike Number")
        print("-----------------------------")
        if not self.parking_vehicles:
            print("No vehicles parked yet!")
        else:
            for slot, values in self.parking_vehicles.items():
                print(f"{slot} -- {values['Name']} -- {values['Bike Number']}")

    def available_slots(self):
        print(f"Total slots: {self.max_slots}")
        print(f"Available slots: {self.max_slots - len(self.parking_vehicles)}")


def main():
    parking_lot = ParkingLot(max_slots=5)

    while True:
        print("\nPARKING VEHICLES MANAGEMENT")
        print("1. Park Your Vehicle")
        print("2. Remove from Parking")
        print("3. Display Parked Vehicles")
        print("4. Available Slots")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            bike_num = input("Enter bike number: ")
            parking_lot.park_vehicle(name, bike_num)

        elif choice == "2":
            bike_num = input("Enter your bike number: ")
            parking_lot.remove_vehicle(bike_num)

        elif choice == "3":
            parking_lot.display_parked_vehicles()

        elif choice == "4":
            parking_lot.available_slots()

        elif choice == "5":
            print("Exiting... Thank you for using the Parking System!")
            break

        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()
