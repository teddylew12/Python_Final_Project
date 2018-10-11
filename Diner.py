#Theodore Lewitt
#ITP 115 Wednesday 4-7 Mark Core
#Final Project
#lewitt@usc.edu
from MenuItem import MenuItem
class Diner:
    #A list of all the different parts of the dining experience a Diner could experience
    STATUSES=["seated","ordering","eating","paying","leaving"]
    def __init__(self,name):
        self.__name=name
        self.__order=[]
        self.__status=0
    #Getter and Setter methods for the Diner Class
    def getName(self):
        return self.__name
    def getOrder(self):
        return self.__order
    def getStatus(self):
        return self.STATUSES[self.__status]
    def getStatusInt(self):
        return self.__status
    def setName(self,newname):
        self.__name=newname
    def setOrder(self,neworder):
        if len(self.__order)==0:
            self.__order=[neworder]
        else:
            self.__order.append(neworder)
    def setStatus(self,newstatus):
        self.__status=int(newstatus)
    def updateStatus(self):
        self.__status+=1
    #Prints all parts of the order, regardless of type
    def printOrder(self):
        a=self.getName() +" has ordered:"
        print(a)
        for x in self.getOrder():
            if  not x==None:
                print(x)
    #calculates Meal Cost of a full meal
    def calculateMealCost(self):
        total=0
        for x in self.getOrder():
            total+=float(x.getPrice())
        return total
    #String method for Diner class
    def __str__(self):
        a="Diner " + self.getName() + " is currently " + self.getStatus()
        return a
