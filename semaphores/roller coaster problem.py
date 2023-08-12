import threading
import time

MAX_CAPACITY = 5  # Maximum number of passengers the roller coaster can carry
roller_coaster = threading.Semaphore(0)  # Semaphore for the roller coaster ride
board_queue = threading.Semaphore(0)  # Semaphore for passengers waiting to board
unboard_queue = threading.Semaphore(0)  # Semaphore for passengers waiting to unboard
board_mutex = threading.Semaphore(1)  # Mutex for boarding process

def passenger(id):
    print(f"Passenger {id} is waiting to board.")
    board_queue.acquire()  # Wait for permission to board
    board_mutex.acquire()
    print(f"Passenger {id} is boarding.")
    board_mutex.release()
    time.sleep(1)  # Simulating the ride
    unboard_queue.acquire()  # Wait for permission to unboard
    print(f"Passenger {id} is unboarding.")
    roller_coaster.release()  # Release the roller coaster for the next ride

def rollercoaster():
    while True:
        print("Roller coaster is waiting for passengers to board.")
        for _ in range(MAX_CAPACITY):
            board_queue.release()  # Signal passengers to board
        for _ in range(MAX_CAPACITY):
            roller_coaster.acquire()  # Wait until all passengers are on board
        print("Roller coaster is starting the ride.")
        time.sleep(2)  # Simulating the ride duration
        print("Roller coaster has finished the ride. Passengers are unboarding.")
        for _ in range(MAX_CAPACITY):
            unboard_queue.release()  # Signal passengers to unboard

if __name__ == "__main__":
    roller_coaster_thread = threading.Thread(target=rollercoaster)
    passenger_threads = []

    for i in range(1, 16):  # Create 15 passenger threads
        passenger_thread = threading.Thread(target=passenger, args=(i,))
        passenger_threads.append(passenger_thread)

    roller_coaster_thread.start()
    for passenger_thread in passenger_threads:
        passenger_thread.start()

    roller_coaster_thread.join()
    for passenger_thread in passenger_threads:
        passenger_thread.join()
