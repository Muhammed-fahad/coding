parking_lot = {}
slot_id = 1

def park_vehicle(vehicle_number, owner_name):
    global slot_id
    if vehicle_number in parking_lot:
        print(f"Vehicle {vehicle_number} is already parked.")
    else:
        parking_lot[slot_id] = {'vehicle_number': vehicle_number, 'owner_name': owner_name}
        print(f"Vehicle {vehicle_number} parked successfully in slot {slot_id}.")
        slot_id += 1

def remove_vehicle(vehicle_number):
    for slot, details in list(parking_lot.items()):
        if details['vehicle_number'] == vehicle_number:
            del parking_lot[slot]
            print(f"Vehicle {vehicle_number} removed successfully.")
            return
    print(f"Vehicle {vehicle_number} not found.")

def display_parked_vehicles():
    if not parking_lot:
        print("No vehicles parked.")
    else:
        print("Slot ID | Vehicle Number | Owner Name")
        print("-----------------------------------")
        for slot, details in parking_lot.items():
            print(f"{slot} | {details['vehicle_number']} | {details['owner_name']}")

def check_available_slots():
    print(f"Total occupied slots: {len(parking_lot)}")

def main():
    while True:
        print("\nParking Management System")
        print("1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. Display Parked Vehicles")
        print("4. Check Available Slots")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            vehicle_number = input("Enter Vehicle Number: ")
            owner_name = input("Enter Owner Name: ")
            park_vehicle(vehicle_number, owner_name)
        elif choice == "2":
            vehicle_number = input("Enter Vehicle Number to Remove: ")
            remove_vehicle(vehicle_number)
        elif choice == "3":
            display_parked_vehicles()
        elif choice == "4":
            check_available_slots()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
