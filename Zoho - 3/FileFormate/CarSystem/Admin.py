from Car import Car
class Admin:
    def __init__(self):
        pass

    def main():
        while True:
            print("1. Create a Car")
            print("2. Delete a Car")
            print("3. Check passenger")
            print("4. change the Price")
            print("5. Exit")

            choice = int(input("Enter the number: "))
            if choice == 1:
                Car.CreateCar()
            elif choice ==2:
                Car.DeleteCar()
            elif choice ==3:
                Car.CheckPassenger()
            elif choice ==4:
                Car.ChangePrice()
            elif choice == 5:
                print("Exiting Bye....!")
                break
            else:
                print("wrong Choice")
