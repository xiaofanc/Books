"""
Queue:
Printing tasks
We were trying to answer a question about whether the current printer could handle the task load if it were set to print with a better quality but slower page rate. 
The approach we took was to write a simulation that modeled the printing tasks as random events of various lengths and arrival times.

Three objects: Printer, Task, PrintQueue

Printer: (printing time, busy?, nexttask)
The Printer class (Listing 2) will need to track whether it has a current task. If it does, then it is busy and the amount of time needed can be computed from the number of pages in the task. The constructor will also allow the pages-per-minute setting to be initialized. 
The tick method decrements the internal timer and sets the printer to idle if the task is completed. The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.

Single Printing task: (waiting time, pages)
When the task is created, a random number generator will provide a length from 1 to 20 pages. 
Each task will also need to keep a timestamp to be used for computing waiting time. This timestamp will represent the time that the task was created and placed in the printer queue. The waitTime method can then be used to retrieve the amount of time spent in the queue before printing begins.

In 5 PPM, whether the printer can finish the tasks in 1 hour?

"""
from Queue import Queue

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # pages-per-minute 
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):  
        # printer needs one second to print
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            print('this task has %d pages and time remaining is %d secs' % (self.currentTask.getPages(), self.timeRemaining))
            if self.timeRemaining <= 0:  # done
                self.currentTask = None

    def busy(self):
        if self.currentTask:
            return True
        else:
            return False

    def startNext(self, newtask):  
    # why * 60? total printing time is in secs
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() / self.pagerate * 60
        print('this task has %d pages and time remaining is %d secs' % (newtask.getPages(), self.timeRemaining))

import random

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime): # waiting time before printing begins
        return currenttime - self.timestamp

    def __repr__(self):
        return f"Task(t:{self.timestamp}, p:{self.pages})"

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    complete = []

    # total time is 1 hour
    for currentSecond in range(numSeconds):
        print('currentSecond: ', currentSecond)
        if newPrintTask(): # if task is created, go into the Queue to wait
            task = Task(currentSecond) # timestamp for this task
            printQueue.enqueue(task)
            print('>>printQueue',printQueue)
            print('waitingtimes: ', waitingtimes)

        # add task
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            # waiting time before printing: currentSecond - nexttask.timestamp
            waitingtimes.append(nexttask.waitTime(currentSecond))
            print('>>printQueue', printQueue)
            print('waitingtimes for all tasks: ', waitingtimes)
            labprinter.startNext(nexttask)
            complete.append(nexttask)
            print('>>complete tasks and next task: ', complete)

        # start printing
        # when the timeremaining is 0 then the printer is available
        labprinter.tick()

    if waitingtimes != []:
        averageWait = sum(waitingtimes)/len(waitingtimes)
        print("Average Wait %6.2f secs %3d tasks remaining"%(averageWait, printQueue.size()))

# if printer can finish 20 tasks per hour, that means 1 task every 180 seconds
# if printer need to finish 40 tasks per hour?
def newPrintTask():
    num = random.randrange(1, 181)
    print("probability that a task is created: ", num)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    # what is the average waiting for tasks and tasks left in the printing rate of 5 ppm in 10 independent trials?
    simulation(3600, 5)
    simulation(3600, 10)


# Average Wait  69.84 secs   2 tasks remaining
# Average Wait  81.26 secs   3 tasks remaining
# Average Wait  26.84 secs   0 tasks remaining
# Average Wait  16.60 secs   0 tasks remaining
# Average Wait  48.75 secs   0 tasks remaining
# Average Wait  39.93 secs   1 tasks remaining
# Average Wait  26.38 secs   0 tasks remaining
# Average Wait 140.22 secs   3 tasks remaining
# Average Wait 135.17 secs   0 tasks remaining
# Average Wait 139.44 secs   0 tasks remaining


