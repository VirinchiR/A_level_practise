class Card:
 # Number as Integer
 # Colour as string
 def __init__(self, Numberp, Colourp):
    self.__Number = Numberp
    self.__Colour = Colourp

def GetNumber(self):
    return self.__Number
def GetColour(self):
    return self.__Colour

CardArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
try:
    Filename = "CardValues.txt"
    File = open(Filename, 'r')
finally:
    for x in range(0, 30):
    NumberRead = int(File.readline())
    ColourRead = File.readline()
    CardArray[x] = Card(NumberRead, ColourRead)
    File.close
except IOError:
print("Could not find file")
global NumbersChosen

def chooseCard():
    global NumbersChosen
    flagContinue = True
while flagContinue == true:
    CardSelected = int(input("Select a Card from 1 to 30"))
if CardSelected < 1 or CardSelected > 30:
    print("Number must be between 1 and 30")
elif NumbersChosen(CardSelected - 1) == True:
    print("Already taken")
else:
    print("Valid")
    flagContinue = False
    NumbersChosen[CardSelected-1] = True
    return CardSelected-1

# main

NumbersChosen = [False for i in range(30)]
Player1 = []  # of type Card
for x in range(0, 4):
 ReturnNumber = ChooseCard()
 Player1.append(CardArray[ReturnNumber])
for x in range(0, 4):
 print(Player1[x].GetColour())
 print(Player1[x].GetNumber())
