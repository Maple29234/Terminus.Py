from decimal import Decimal, ROUND_UP
from datetime import date 
import math
import random

#Coin Variables
class game:
    maxBattery = 15.00
    powerModifier = 1.00    
    power = 50
    powerGain = 1
    powerUsed = 0
    rechargerate = 1

#Shop
class Shop: 
    class Items:
        #items
        Items = {
            "1": "powerModifier+=.1",
            "2": "powerGainIncrease",
            "3": "powerModifier+=.5"
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
            
            def Item1(self,Shop):
                if game.power < Shop.Items.Prices['1']:
                    terminal.log(terminal,"Not enough money")
                    return

                self.ItemsBought2['1']+=1
                self.ItemsBought['1']+=1
                
                game.power-=Shop.Items.Prices['1']
                game.powerModifier+=.1
                
                if self.ItemsBought['1'] >= 10:
                    if game.power != 0:
                        Shop.Items.Prices['1'] += round(game.power * Decimal(.1))
                    else:
                        Shop.Items.Prices['1'] += round(Shop.Items.Prices['1'] * .1)
                    self.ItemsBought['1'] = 0
                    
                    
                print("Purchase complete")
                terminal.log(terminal,'Total power : ' + str(game.power))

                
            def Item2(self,Shop):

                if game.power < Shop.Items.Prices['2']:
                    terminal.log(terminal,"Not enough money")
                    return
                
                self.ItemsBought2['2']+=1
                self.ItemsBought['2']+=1
                
                game.power-=Shop.Items.Prices['2']
                game.powerGain+=1
                    

                if self.ItemsBought['2'] >= 3:
                    
                    if game.power != 0:
                        Shop.Items.Prices['2'] += round(game.power * Decimal(.1))
                    else:
                        Shop.Items.Prices['2'] += round(Shop.Items.Prices * .1)
                    self.ItemsBought['2'] = 0 
                    
                print("Purchase complete")
                terminal.log(terminal,'Total power : ' + str(game.power))
                
            def Item3(self,Shop):
                if game.power < Shop.Items.Prices['3']:
                    terminal.log(terminal,"Not enough money")
                    return
                self.ItemsBought2['3']+=1
                
                self.ItemsBought['3']+=1
                game.power-=Shop.Items.Prices['3']
                game.powerModifier+=0.5

                if self.ItemsBought['3'] >= 1:
                    print("S")
                    if game.power > 8:
                        Shop.Items.Prices['3'] += round(game.power)
                    else:
                        Shop.Items.Prices['3'] += round(Shop.Items.Prices * .25)
                    self.ItemsBought['3'] = 0 

                print("Purchase complete")
                terminal.log(terminal,'Total power : ' + str(game.power))
                
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
        terminal.log(terminal,"Which item would you like to buy? (Requires Integer)")
        
        for x,y in self.Items.Functions.functionDict.items():
            
            if terminal.message[terminal.currentMessage] == x:
                self.Items.Functions.functionDict[x](self.Items.Functions,self)
            
            elif terminal.message[terminal.currentMessage] == str(len(self.Items.Items)+1):
                terminal.log(terminal,"Canceled")

#Terminal
class terminal:
    #Variables
    found = False
    message = []
    currentMessage = -1
    tDate = date.today() 

    #log
    def log(self,Message):
        self.currentMessage+=1
        self.message.append(input(Message+"\n"))
    
    #Commands
    Commands = {
        
    }
    
    #Use Command
    def useCommand(self,Name,Arg = ""):
        if Arg == "":
            self.Commands[Name]()#Check if Arg was used
        else:
            self.Commands[Name](Arg)#If Arg was used then use it
    
    #Add Command
    def addCommand(self,CommandName,Command):
        self.Commands.update({CommandName : Command})#Add line to Commands

    #Start Message Function
    def startMessage():
        def greetMessage():
            tDate = terminal.tDate
            if helpers.randomnumbah(0, 10000) == 1:
                return("Unwelcome to AntiTerminus.")
                
            elif tDate.month == 1 and tDate.day == 1: 
                return("Happy New Year! Welcome to Terminus.py")
                
            elif tDate.month == 2 and tDate.day == 4:
                return("It's Terminus.py anniversary! Welcome!")
                
            return("Welcome to Terminus.py")
        print(greetMessage())
        terminal.log(terminal,"You can type 'help' to see available commands")


    #Command Functions

    #Fish command
    def catchmeafish():
        fishIndex = {
            '1' : cod,
            '2' : salmon,
            '3' : cod,
            '4' : salmon,
            '5' : cod,
            '6' : cod,
            '7' : salmon,
            '8' : cod,
            '9' : salmon,
            '10' : shark
            
        }
        tempVar = helpers.randomnumbah(1,10)
        fishIndex[str(tempVar)].catchafish() #Add your own fish.catchafish here! without it the fish no catchy watchy with this function
    
    #Help Command
    def HelpCommand():
        print("Commands : ")
        print("Help - Brings up this page")
        print("Shop - Brings up the shop")
        terminal.log(terminal,'Mine - Increase money')  

    #Mine Command  
    def MineCommand():

        #Increase powerModifier when youve used Mine ten times
        if game.powerUsed+1 >= 10:
            game.powerUsed = 0 
            game.powerModifier += .1
        
        powerGained = Decimal(str(game.powerGain * game.powerModifier)).quantize(Decimal('.01'), rounding=ROUND_UP) #Multiply powerGain and powerModifier then round it up
        game.power += powerGained # add the power gained
        game.powerUsed+=1 # increase powerUsed
        
        #Print powerGained and power
        print('Gained ' + str(powerGained) + ' power')
        terminal.log(terminal,'You now have ' + str(game.power) + ' power')
    
    #Charge Command
    def Charge():
            if game.power < game.maxbattery:
                game.power = game.power + game.rechargerate
                # Leaving cooldown out for  now dont feel like doing it
                # game.chargeCooldown = true
                #setTimeout(() => {
                #    game.chargeCooldown = false;
                #, 3000); // 5 seconds cooldown
            elif game.power == game.maxbattery: 
                return terminal.log("Full charge.")
                terminal.log("Current battery: " + game.power)

#Fiiiish
class fish:
    def __init__(self,name, desc, price, chance):
        self.name = name
        self.desc = desc
        self.price = price
        self.chance = chance #Out of 100
    
    def catchafish(self):
        didyacatchit = helpers.randomnumbah(1, 100)
        if didyacatchit >= 0 and didyacatchit <= self.chance:
            print("You caught a " + self.name + "!")
            game.power += self.price
            terminal.log(terminal,"'" + self.desc + "'")
        else:
            terminal.log(terminal,'You caught nothing, you are a failure') #Sadge :(

#Random functions
class helpers:
    def randomnumbah(min,max):
        return math.floor(random.random() * (max - min + 1) + min);

shop = Shop
shopItems = shop.Items
shopFunctions = shopItems.Functions

shark = fish("Shark", "An endangered sand tiger shark, you are now in jail for killing an endangered species",500,1)
salmon = fish("Salmon", "A sillier lil fish",30,45)
cod = fish("Cod", "A silly lil fish", 25, 50)
terminal.addCommand(terminal,"catchmeafish",terminal.catchmeafish)
#:3 :3
terminal.addCommand(terminal,"mine",terminal.MineCommand)
terminal.addCommand(terminal,"shop",Shop.init)
terminal.addCommand(terminal,"help",terminal.HelpCommand)
terminal.addCommand(terminal,"charge",terminal.Charge)

terminal.startMessage()

#inf while loop
while "Astolfo Pores":
    for x in terminal.Commands:
        if terminal.message[terminal.currentMessage].lower() == x:
            terminal.found = True
            if terminal.message[terminal.currentMessage].lower() == 'shop':
                terminal.useCommand(terminal,x,Shop)
            else:
                terminal.useCommand(terminal,x)
    if terminal.found != True:
        terminal.log(terminal,"Error : Command Not Found. Please try again or enter 'help' to see a list of commands")
    else:
        terminal.found = False
