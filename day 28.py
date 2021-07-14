
#Python - Multithreaded Programming
#1. Define a subclass using threading.Thread class.

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print( "Exiting " + self.name)

def print_time(threadName, counter, delay):
     while counter:
        if exitFlag:
            threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
#2. Instantiate the subclass and trigger the thread.

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
In [6]:
thread1.start()
thread2.start()

print("Exiting Main Thread")
Starting Thread-1
Starting Thread-2
Exiting Main Thread
