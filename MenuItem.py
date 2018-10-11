#Theodore Lewitt
#ITP 115 Wednesday 4-7 Mark Core
#Final Project
#lewitt@usc.edu
class MenuItem:
    #Initiates menu item
    def __init__(self,name,type,price,description):
        self.__name=name
        self.__price=float(price)
        self.__description=description
        self.__type1=type
    #Getters and Setter Methods for the Class
    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    def getDescription(self):
        return self.__description
    def getType(self):
        return self.__type1
    def setName(self,newname):
        self.__name=newname
    def setPrice(self, newprice):
        self.__price = newprice
    def setDescription(self,newdes):
        self.__description=newdes
    def setType(self,newtype):
        self.__type1=newtype
    #String Method for the Class,Returns all pertinent information about the MenuItem Object
    def __str__(self):
        a= self.getName() +" (" +self.getType()+"): $"+str(self.getPrice())
        a+="\n\t"+self.getDescription()
        return a

