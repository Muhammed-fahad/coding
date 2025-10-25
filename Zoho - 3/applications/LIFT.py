class Lift:
    def __init__(self, floors=10):
        self.current_floor = 0
        self.total_floors = floors
        
    def move_up(self, target_floor):
        if target_floor > self.total_floors:
            print(f"Invalid floor. This building has only {self.total_floors} floors.")
        elif target_floor > self.current_floor:
            print(f"Moving up from floor {self.current_floor} to floor {target_floor}.")
            self.current_floor = target_floor
        else:
            print("Lift is already on or above the target floor.")

    def move_down(self, target_floor):
        if target_floor < 0:
            print("Invalid floor. Floors start from 0.")
        elif target_floor < self.current_floor:
            print(f"Moving down from floor {self.current_floor} to floor {target_floor}.")
            self.current_floor = target_floor
        else:
            print("Lift is already on or below the target floor.")

    def display_floor(self):
        print(f"Current floor: {self.current_floor}")

def main():
    lift = Lift()
    while True:
        print("\nLift System")
        print("1. Move Up")
        print("2. Move Down")
        print("3. Display Current Floor")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            floor = int(input("Enter floor number to move up: "))
            lift.move_up(floor)
        elif choice == "2":
            floor = int(input("Enter floor number to move down: "))
            lift.move_down(floor)
        elif choice == "3":
            lift.display_floor()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
