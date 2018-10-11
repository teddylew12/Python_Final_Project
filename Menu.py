#Theodore Lewitt
#ITP 115 Wednesday 4-7 Mark Core
#Final Project
#lewitt@usc.edu
from MenuItem import MenuItem
class Menu:
    #The different types of Items on the Menu
    MENU_ITEM_TYPES=["Drink","Appetizer","Entree","Dessert"]
    #THe method creates a dictionary and populates it with the keys as Item Types,
    #The values are lists of all menu items that are of that type
    def __init__(self,filename):
        fileIn=open(filename,'r')
        self.__menuItemDictionary={}
        input=fileIn.readlines()
        for x in input:
            temp=x.split(',')
            tempitem=MenuItem(temp[0],temp[1],temp[2],temp[3])
            if temp[1] in self.__menuItemDictionary.keys():
                self.__menuItemDictionary[temp[1]].append(tempitem)
            else:
                self.__menuItemDictionary[temp[1]]=[tempitem]
    def getMenuItem(self,menuitem,intindex):
        return self.__menuItemDictionary[menuitem][intindex-1]
    #Prints all of the options for a singular menu type
    def printMenuItemsByType(self,menue):
        a="****All " +menue +" offerings:****\n"
        ticker=1
        for x in self.__menuItemDictionary.get(menue):
            a+=str(ticker) +") " + str(x) +"\n"
            ticker+=1
        print(a)
    def getNumMenuItemsByType(self,menue):
        return len(self.__menuItemDictionary.get(menue))

