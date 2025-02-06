from decimal import Decimal, ROUND_UP
from datetime import date 
import math
import random
#Most Variables
message = []
currentMessage = -1
X = 1
CoinsModifier = 1.00    
Coins = 50
CoinsGain = 1
CoinsUsed = 0
tDate = date.today() 


#Shop
class Shop: 
    class Items:
        #items
        Items = {
        "1": "CoinsModifier+=.1",
        "2": "CoinsGainIncrease",
        "3": "CoinsModifier+=.5"
        }
        
        #prices
        Prices = {
            '1' : 5,
            '2' : 8,
            '3' : 20
        }
        
        #functions
        class Functions:
            ItemsBought2 = {
                '1' : 0,
                '2' : 0,
                '3' : 0
            }
            ItemsBought = {
                '1' : 0,
                '2' : 0,
                '3' : 0
            }
            
            def Item1(Self,Shop):
                global Coins, CoinsModifier, message, decimal
                if Coins < Shop.Items.Prices['1']:
                    terminal.NewMessage("Not enough money")
                    return

                Self.ItemsBought2['1']+=1
                Self.ItemsBought['1']+=1
                
                Coins-=Shop.Items.Prices['1']
                CoinsModifier+=.1
                
                if Self.ItemsBought['1'] >= 10:
                    if Coins != 0:
                        Shop.Items.Prices['1'] += round(Coins * Decimal(.1))
                    else:
                        Shop.Items.Prices['1'] += round(Shop.Items.Prices['1'] * .1)
                    Self.ItemsBought['1'] = 0
                    
                    
                print("Purchase complete")
                terminal.NewMessage('Total Coins : ' + str(Coins))

                
            def Item2(Self,Shop):
                global Coins, CoinsGain, message

                if Coins < Shop.Items.Prices['2']:
                    terminal.NewMessage("Not enough money")
                    return
                
                Self.ItemsBought2['2']+=1
                Self.ItemsBought['2']+=1
                
                Coins-=Shop.Items.Prices['2']
                CoinsGain+=1
                    

                if Self.ItemsBought['2'] >= 3:
                    
                    if Coins != 0:
                        Shop.Items.Prices['2'] += round(Coins * Decimal(.1))
                    else:
                        Shop.Items.Prices['2'] += round(Shop.Items.Prices * .1)
                    Self.ItemsBought['2'] = 0 
                    
                print("Purchase complete")
                terminal.NewMessage('Total Coins : ' + str(Coins))
                
            def Item3(Self,Shop):
                global Coins, CoinsModifier, message
                if Coins < Shop.Items.Prices['3']:
                    terminal.NewMessage("Not enough money")
                    return
                Self.ItemsBought2['3']+=1
                
                Self.ItemsBought['3']+=1
                Coins-=Shop.Items.Prices['3']
                CoinsModifier+=0.5

                if Self.ItemsBought['3'] >= 1:
                    print("S")
                    if Coins > 8:
                        Shop.Items.Prices['3'] += round(Coins)
                    else:
                        Shop.Items.Prices['3'] += round(Shop.Items.Prices * .25)
                    Self.ItemsBought['3'] = 0 

                print("Purchase complete")
                terminal.NewMessage('Total Coins : ' + str(Coins))
                
            functionDict = {
                '1' : Item1,
                '2' : Item2,
                '3' : Item3
            }
            
    def init(self):
        Items = self.Items
        
        print("--------------------------------- Shop ---------------------------------")
        
        for x,y in self.Items.Items.items():
            print("Item "+ x + " : "+ y+" | Price : "+ str(self.Items.Prices[x])+" | Amount Bought : " + str(self.Items.Functions.ItemsBought2[x]))
        
        print(str(len(self.Items.Items)+1) + " : Cancel")
        terminal.NewMessage("Which item would you like to buy? (Requires Integer)")
        
        for x,y in self.Items.Functions.functionDict.items():
            
            if message[currentMessage] == x:
                self.Items.Functions.functionDict[x](self.Items.Functions,self)
            
            elif message[currentMessage] == str(len(self.Items.Items)+1):
                terminal.NewMessage("Canceled")

class terminal:
    #NewMessage
    def NewMessage(Message):
        global message, currentMessage
        currentMessage+=1
        message.append(input(Message))
    
    Commands = {
        
    }
    
    def useCommand(self,Name,Arg = ""):
        if Arg == "":
            self.Commands[Name]()
        else:
            self.Commands[Name](Arg)
    
    def addCommand(self,CommandName,Command):
        self.Commands.update({CommandName : Command})



def randomnumbah(min,max):
    return math.floor(random.random() * (max - min + 1) + min);


def greetMessage():
    if (randomnumbah(0, 10000) == 1):
        return("Unwelcome to AntiTerminus.")
        
    elif (tDate.month == 1 and tDate.day == 1): 
        return("Happy New Year! Welcome to Terminus.py")
        
    elif (tDate.month == 2 and tDate.day == 4):
        return("It's Terminus.py anniversary! Welcome!")
        
    return("Welcome to Terminus.py")
    

def startMessage():
    print(greetMessage())
    terminal.NewMessage("You can type 'help' to see available commands")

def HelpCommand():
    print("Commands : ")
    print("Help - Brings up this page")
    print("Shop - Brings up the shop")
    terminal.NewMessage('Mine - Increase money')    

def MineCommand():
    global CoinsUsed, Coins,CoinsModifier,CoinsGain,currentMessage,message
    
    #Increase CoinsModifier when youve used Mine ten times
    if CoinsUsed+1 >= 10:
        CoinsUsed = 0 
        CoinsModifier += .1
    
    CoinsGained = Decimal(str(CoinsGain * CoinsModifier)).quantize(Decimal('.01'), rounding=ROUND_UP) #Multiply CoinsGain and CoinsModifier then round it up
    Coins += CoinsGained # add the coins gained
    CoinsUsed+=1 # increase coinsUsed
    
    #Print CoinsGained and Coins
    print('Gained ' + str(CoinsGained) + ' Coins')
    terminal.NewMessage('You now have ' + str(Coins) + ' Coins')



terminal.addCommand(terminal,"mine",MineCommand)
terminal.addCommand(terminal,"shop",Shop.init)
terminal.addCommand(terminal,"help",HelpCommand)



shop = Shop()
shopItems = shop.Items()
shopFunctions = shopItems.Functions
found = False



startMessage()

#inf while loop
while X == 1:
    for x in terminal.Commands:
        print(message)
        print(currentMessage)
        if message[currentMessage].lower() == x:
            found = True
            if message[currentMessage].lower() == 'shop':
                terminal.useCommand(terminal,x,Shop)
            else:
                terminal.useCommand(terminal,x)
    if found != True:
        terminal.NewMessage("Error : Command Not Found. Please try again or enter 'help' to see a list of commands")
    else:
        found = False
