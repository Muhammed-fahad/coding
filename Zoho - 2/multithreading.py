import threading
import time

def loop1():
    for i in range(1,5):
        print(i)
        time.sleep(3)

def loop2():
    for i in range(5,10):
        print(i)
        time.sleep(4)
        

# Create threads
t1 = threading.Thread(target=loop1, name="Thread-1")
t2 = threading.Thread(target=loop2, name="Thread-2")

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()
