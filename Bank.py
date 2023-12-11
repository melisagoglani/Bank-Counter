import os
customerCount= int(input("How many cutomers do you want to enter: "))
os.system('cls')

class Customers:
    def __init__(self, entryTime, expectedTime,id):
        self.EntTime = entryTime
        self.ExpTime = expectedTime
        self.copyOfExpTime = expectedTime
        self.id = id
    def __str__(self):
         return f"{self.id}"


Customer=[]
max_time = 0
for i in range(customerCount):
    Customer.append(f"Customer{i+1}")
    print(f"Customer{i+1}:\n")
    entryTime = int(input("Entry Time: "))
    expectedTime = int(input("Expected time: "))
    Customer[i] = Customers(entryTime, expectedTime,i+1)
    max_time += expectedTime
    os.system('cls')


Counters = [[],[],[]]

for time in range(max_time+1):
    for person in Customer:
        if(time==person.EntTime):

            TimeList = [] 
            for index in range(len(Counters)): 
                TotalTime = 0
                for personInLine in Counters[index]:
                    TotalTime += personInLine.ExpTime
                TimeList.append(TotalTime)
            min = TimeList[0]
            for i in range(1, len(TimeList)):
                if TimeList[i] < min:
                    min = TimeList[i]
            minIndex = TimeList.index(min)
            Counters[minIndex].append(person)
            person.timeSpent = 0
            print(f"{time}: Customer{person} is in counter {minIndex+1}")


    for counter in Counters:
        if len(counter):
            counter[0].copyOfExpTime -= 1
            if (counter[0].copyOfExpTime == 0):
                print(f"{time+1}: Customer{counter[0]} has left.")
                del counter[0]      
        for personInLine in counter:
            personInLine.timeSpent += 1


ExpTimeSum = 0 
TimeSpentSum = 0
Sub = 0
num = 0
for person in Customer:
    Sub += person.timeSpent
    ExpTimeSum += person.ExpTime
    TimeSpentSum += person.timeSpent
    num += 1

SubAvg = Sub/num
ExpTimeAvg = ExpTimeSum/num
TimeSpentAvg = TimeSpentSum/num
print(f"The average of difference between expected time and the actual time spent in the bank: {SubAvg}")
print(f"The Average of Expected time in the bank: {ExpTimeAvg}")
print(f"The Average of time spent in the bank: {TimeSpentAvg}")