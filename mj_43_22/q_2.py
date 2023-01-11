class balloon :
    def __init__(self, PdefenceItem, Pcolour):
        self.__Health = 100
        self.__colour = Pcolour
        self.__DefenceItem = PdefenceItem
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self, Change):
        self.__Health = self.__Health + Change
    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False
Method = input("Enter balloon defence method")
Colour = input("Enter the balloon colour")
Balloon1 = balloon(Method,Colour)

def Defend(MyBalloon):
    Strength = int(input("Enter the strength of the opponent"))
    MyBalloon.ChangeHealth(-Strength)
    print("You defend with", str(MyBalloon.GetDefenceItem()))
    if MyBalloon.CheckHealth() == True:
        print("Defence has Failed")
    else:
        print("Defended")
    return MyBalloon

Balloon1 = Defend(Balloon1)