from decimal import Decimal, ROUND_UP
#Most Variables
message = []
currentMessage = 0
X = 1
CoinsModifier = 1.00
Coins = 0
CoinsGain = 1
CoinsUsed = 0

#NewMessage
def NewMessage(Message):
    global message, currentMessage
    currentMessage+=1
    message.append(input(Message))

#helpFunction
def HelpCommand():
    print("Commands : ")
    print("Help - Brings up this page")
    print("Shop - Brings up the shop")
    NewMessage('Mine - Increase money')    

#mineFunction
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
    NewMessage('You now have ' + str(Coins) + ' Coins')



#Shop
class Shop: 
    class Items:
        #items
        Items = {
        "1": "CoinsModifier+=.1",
        "2": "CoinsGainIncrease",
        "3": "CoinsModifier+=1"
        }
        
        #prices
        Prices = {
            '1' : 5,
            '2' : 8,
            '3' : 20
        }
        
        #functions
        class Functions:
            ItemsBought = {
                '1' : 0,
                '2' : 0,
                '3' : 0
            }
            
            def Item1(Self,Shop):
                global Coins, CoinsModifier, message,NewMessage
                if Coins < Shop.Items.Prices['1']:
                    NewMessage("Not enough money")
                    return
                if Self.ItemsBought['1'] == 10:
                    
                    Shop.Items.Prices['1'] += Coins * .1
                    Self.ItemsBought['1'] = 0 
                    
                if Shop.Items.Prices['1'] < Coins:
                    Self.ItemsBought['1']+=1
                    Coins-=Shop.Items.Prices['1']
                    CoinsModifier+=.1
                    
                print("Purchase complete")
                NewMessage('Total Coins : ' + str(Coins))
                
            def Item2(Self,Shop):
                global Coins, CoinsModifier, message,NewMessage

                if Coins < Shop.Items.Prices['2']:
                    NewMessage("Not enough money")
                    return
                
                if Self.ItemsBought['2'] == 10:
                    
                    Shop.Items.Prices['2'] += Coins * .1
                    Self.ItemsBought['2'] = 0 
                
                if Shop.Items.Prices['2'] < Coins:
                    Self.ItemsBought['2']+=1
                    Coins-=Shop.Items.Prices['2']
                    CoinsGain+=1
                    
                print("Purchase complete")
                NewMessage('Total Coins : ' + str(Coins))
                
            def Item3(Self,Shop):
                global Coins, CoinsGain, message,currentMessage

            functionDict = {
                '1' : Item1,
                '2' : Item2,
                '3' : Item3
            }
            
    def init(self):
        global NewMessage
        Items = self.Items
        
        print("--------------------------------- Shop ---------------------------------")
        
        for x,y in self.Items.Items.items():
            print("Item "+ x + " : "+ y+" | Price : "+ str(self.Items.Prices[x])+" | Amount Bought : " + str(self.Items.Functions.ItemsBought[x]))
        
        print(str(len(self.Items.Items)+1) + " : Cancel")
        NewMessage("Which item would you like to buy? (Requires Integer)")
        
        for x,y in self.Items.Functions.functionDict.items():
            
            if message[currentMessage] == x:
                self.Items.Functions.functionDict[x](self.Items.Functions,self)
            
            elif message[currentMessage] == str(len(self.Items.Items)+1):
                NewMessage("Canceled")

class Terminal:
    Commands = {
        
    }
    
    def useCommand(self,Name,Arg = ""):
        if Arg == "":
            self.Commands[Name]()
        else:
            self.Commands[Name](Arg)
    
    def addCommand(self,CommandName,Command):
        self.Commands.update({CommandName : Command})

Terminal.addCommand(Terminal,"mine",MineCommand)
Terminal.addCommand(Terminal,"shop",Shop.init)
Terminal.addCommand(Terminal,"help",HelpCommand)

shop = Shop()
shopItems = shop.Items()
shopFunctions = shopItems.Functions

print('Welcome to Terminus.py')
message.append(input('Enter "Help" to get a list of commands'))



#inf while loop
while X == 1:
    for x in Terminal.Commands:
        if message[currentMessage] == x:
            if message[currentMessage] == 'shop':
                Terminal.useCommand(Terminal,x,Shop)
            else:
                Terminal.useCommand(Terminal,x)