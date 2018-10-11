#Theodore Lewitt
#ITP 115 Wednesday 4-7 Mark Core
#Final Project
#lewitt@usc.edu
from Menu import Menu
from Diner import Diner
class Waiter:
    #Each Waiter object inherits the entire menu and a list of diners to keep track of
    def __init__(self,menu):
        self.__diners=[]
        self.__menu=menu
    def addDiner(self,newdiner):
        self.__diners.append(newdiner)
    def getNumDiners(self):
        return len(self.__diners)
    #Loops through each possible diner status and checks if the diner is in that part of his/her meal
    #Then it prints the diners grouped on their status
    def printDinerStatuses(self):
        for x in range(0,5):
            templist = []
            for diner in self.__diners:
                if diner.getStatus()==Diner.STATUSES[x]:
                    templist.append(diner)
            print("****" + Diner.STATUSES[x] +"*****")
            for x in templist:
                print(x)
    #Takes orders from diners in the ordering phase
    #Each order comprises of one item from each of the food types
    #The order then is added to the order of that specific diner
    def takeOrders(self):
        for diner in self.__diners:
            if diner.getStatus()==Diner.STATUSES[1]:
                for x in range(0,len(Menu.MENU_ITEM_TYPES)):
                    type2=self.__menu.MENU_ITEM_TYPES[x]
                    self.__menu.printMenuItemsByType(type2)
                    #Error checking assuming the answer will be a invalid response and breaking the loop once
                    #a correct choice has been made
                    validChoice=False
                    while not validChoice:
                        try:
                            choice=int(input("Please pick an item to order by selecting its number!"))
                            if choice >= 1 and choice <= self.__menu.getNumMenuItemsByType(type2):
                                diner.setOrder(self.__menu.getMenuItem(type2, choice))
                                validChoice = True
                            else:
                                print("Invalid input please try again!")
                        except ValueError:
                            print("Please enter an integer")

                if not diner.getOrder()==[]:
                    print(diner.printOrder())


    #Prepares a check for diners in the paying phase
    def ringUpDiners(self):
        for x in self.__diners:
            if x.getStatus()=="paying":
                cost=x.calculateMealCost()
                print("Your meal costs " + "%.2f" % cost)
    #Checks if diners are in the leaving phase and thanks them for coming
    #Loops through the list backwards to delete done diners while perserving order
    def removeDoneDiners(self):
        for x in self.__diners:

            if x.getStatus()=="leaving":
                print("Thanks for coming " +x.getName() + " !!")
        for y in range(self.getNumDiners()-1,-1,-1):
            if self.__diners[y].getStatus()==Diner.STATUSES[4]:
                del self.__diners[y]

    #Moves through the parts off the waiting process and advances the statuses of the diners
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.__diners:
            diner.updateStatus()
