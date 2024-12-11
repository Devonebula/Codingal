import random
import time
def getRandomDate(startDate, endDate):
    print("Printing random dates betwee,", startDate, "and", endDate)
    randomno=random.random()
    dateFormat="%d/%m/%Y"
    startTime=time.mktime(time.strptime(startDate, dateFormat))
    endTime=time.mktime(time.strptime(endDate, dateFormat))
    randomTime=startTime+randomno*(endTime-startTime)
    randomTime=time.strftime(dateFormat, time.localtime(randomTime))
    return randomTime
print(getRandomDate("01/01/2020", "31/12/2024"))