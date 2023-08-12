from threading import Semaphore, Thread

# Shared variables
boat = Semaphore(1)
mutex = Semaphore(1)

# Get inputs from the user
people = int(input("Enter the number of people: "))
max_capacity = int(input("Enter the maximum number of people allowed in the boat: "))
crossing = Semaphore(max_capacity)

def cross_river(person_id):
    # Cross river from one side to another
    print(f'Person {person_id} is waiting to cross the river.')
    
    # Acquire crossing semaphore to limit the number of people in the boat
    crossing.acquire()  
    
    
    mutex.acquire()
    print(f'Person {person_id} boarded the boat.')
    mutex.release()
    
    # Acquire the boat semaphore to ensure exclusive access to the boat
    boat.acquire()  
    
    # Crossing the river (simulated by a sleep)
    print(f'Person {person_id} is crossing the river.')
    
    boat.release()  # Release the boat semaphore after crossing
    
    mutex.acquire()
    print(f'Person {person_id} disembarked from the boat.')
    mutex.release()
    
    # Release the crossing semaphore to allow others to cross
    crossing.release()  
    
# Creating and starting threads for people crossing the river
threads = []

for i in range(people):
    t = Thread(target=cross_river, args=(i,))
    threads.append(t)
    t.start()

# Waiting for all threads to complete
for t in threads:
    t.join()

print('All people have crossed the river.')
