# Parking Lot System without SQL

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupied_slots = {}
        self.slot_id = 1

    def park_vehicle(self, vehicle_number, vehicle_type):
        if len(self.occupied_slots) < self.capacity:
            self.occupied_slots[self.slot_id] = {'vehicle_number': vehicle_number, 'vehicle_type': vehicle_type}
            print(f"Vehicle {vehicle_number} parked at slot {self.slot_id}.")
            self.slot_id += 1
        else:
            print("Parking lot is full!")

    def remove_vehicle(self, slot_id):
        if slot_id in self.occupied_slots:
            # vehicle = self.occupied_slots.pop(slot_id)
            del self.occupied_slots[slot_id]
            print(f"Vehicle removed from slot {slot_id}.")
        else:
            print("Invalid slot ID!")

    def display_parking_lot(self):
        if not self.occupied_slots:
            print("Parking lot is empty.")
        else:
            print("Slot ID | Vehicle Number | Vehicle Type")
            print("-----------------------------------")
            for slot, details in self.occupied_slots.items():
                print(f"{slot} | {details['vehicle_number']} | {details['vehicle_type']}")

def main():
    capacity = int(input("Enter parking lot capacity: "))
    parking_lot = ParkingLot(capacity)
    
    while True:
        print("\nParking Lot System")
        print("1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. Display Parking Lot")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            vehicle_number = input("Enter Vehicle Number: ")
            vehicle_type = input("Enter Vehicle Type (Car/Bike/Truck): ")
            parking_lot.park_vehicle(vehicle_number, vehicle_type)
        elif choice == "2":
            slot_id = int(input("Enter Slot ID to remove vehicle: "))
            parking_lot.remove_vehicle(slot_id)
        elif choice == "3":
            parking_lot.display_parking_lot()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
