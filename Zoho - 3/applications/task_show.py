class TaskShow():
    def __init__(self):
        self.db = {}                
    
    def addTask(self):
        id = int(input("Enter your id: "))
        task = input("Enter the task: ")
        desc = input("Enter the description of the task: ")
        date = input("Enter the date (DD//MM//yy): ")
        
        while id in self.db:
            print("\nID already present Enter new id")
            id = int(input("Enter your id: "))
        self.db[id] = {'Task':task , 'Desc':desc , 'Date':date}
        return
    
    def removeTask(self):
        id = int("Enter your id: ")
        del self.db[id]
        print("Your Task is removed Succesfull !!!")
        return
    
    def showTask(self):
        print("   ID   ||  Task  ||  Desc  || Date ")
        print("------------------------------------")
        for id,val in self.db.items():
            print(f"  {id}  ||  {self.db[id]['Task']}  ||  {self.db[id]['Desc']}  ||  {self.db[id]['Date']}")
def main():
    Task = TaskShow()
    while(True):
        print("1. ADD Task\n 2. Remove Task\n 3. Show Task\n 4.Exit")
        
        choice = int(input("Enter your option: "))
        if choice == 1:
            Task.addTask()
        elif choice == 2:
            Task.removeTask()
        
        elif choice == 3:
            Task.showTask()
        
        elif choice == 4:
            print("Exiting.....")
            break

if __name__ == "__main__":
    main()