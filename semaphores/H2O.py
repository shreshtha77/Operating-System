#H2O
import threading

class H2O(object):
    def __init__(self):
        self.__l = threading.Lock()
        self.__nH = 0
        self.__nO = 0
        self.__releaseHydrogen = None
        self.__releaseOxygen = None

    def hydrogen(self, releaseHydrogen):
        with self.__l:
            self.__releaseHydrogen = releaseHydrogen
            self.__nH += 1
            self.__output()

    def oxygen(self, releaseOxygen):
        with self.__l:
            self.__releaseOxygen = releaseOxygen
            self.__nO += 1
            self.__output()

    def __output(self):
        while self.__nH >= 2 and self.__nO >= 1:
            self.__nH -= 2
            self.__nO -= 1
            self.__releaseHydrogen()
            self.__releaseHydrogen()
            self.__releaseOxygen()

# Functions to release hydrogen and oxygen
def releaseHydrogen():
    print("H", end='')

def releaseOxygen():
    print("O\n")

if __name__ == "__main__":
    h2o = H2O()

    # Creating threads for hydrogen and oxygen atoms
    threads = []
    for _ in range(6):
        threads.append(threading.Thread(target=h2o.hydrogen, args=(releaseHydrogen,)))
        threads.append(threading.Thread(target=h2o.oxygen, args=(releaseOxygen,)))

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

