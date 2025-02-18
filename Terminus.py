from decimal import Decimal, ROUND_UP
from datetime import date 
import math
import random

#game stuff
class game:
    power = 0
    maxbattery = 15.00
    pointsModifier = 1.00    
    points = 111111
    pointsGain = 1
    pointsUsed = 0
    rechargeRate = 1
    upgStage = 0
    expToLevel = 0
    class unlocks:
        begin = False
        index = False
        doctype = False
        configyml = False
        infShop = False
    
#Shop
class Shop: 
    class Items:
        
        #prices
        Prices = {
            '1' : 5,
            '2' : 20,
            '3' : 50,
            '4' : 100
        }
        
        
        #items
        Items = {
            "1": "begin: .........The beginning",
            "2": "index: ........index.html",
            "3": "doctype: ......<!DOCTYPE HTML>",
            "4": "configyml: ...config.yml"
        }
        
        #functions
        class Functions:
            def thingThatWillProbBeRemoved(self,x):
                itemsBoughtCounter = 0
                itemsNotBoughtCounter = 0
                self.ItemsBought[x]+=1
                print(f'thing{x}')
                for i in self.ItemsBought:
                    if self.ItemsBought[i] == 1:
                        itemsBoughtCounter+=1
                    else:
                        itemsNotBoughtCounter+=1
                if itemsBoughtCounter == len(self.ItemsBought) and itemsNotBoughtCounter == 0:
                    terminal.log(terminal,"Inf shop unlocked")
                    game.unlocks.InfShop = True

                
            ItemsBought2 = {
                '1' : 0,
                '2' : 0,
                '3' : 0,
                '4' : 0
            }
            ItemsBought = {
                '1' : 0,
                '2' : 0,
                '3' : 0,
                '4' : 0
            }
            
            def Item1(self,Shop):
                if game.points < Shop.Items.Prices['1']:
                    terminal.log(terminal,"Not enough money")
                    return
                if self.ItemsBought['1'] == 1:
                    terminal.log(terminal,"Already bought")
                    return
                self.thingThatWillProbBeRemoved(self,'1')
                
                game.points-=Shop.Items.Prices['1']
                game.pointsModifier+=.1
                    
                print("Purchase complete")
                terminal.log(terminal,'Total points : ' + str(game.points))
                
            def Item2(self,Shop):

                if game.points < Shop.Items.Prices['2']:
                    terminal.log(terminal,"Not enough money")
                    return
                
                if self.ItemsBought['2'] == 1:
                    terminal.log(terminal,"Already bought")
                    return
                
                self.thingThatWillProbBeRemoved(self,'2')
                
                game.points-=Shop.Items.Prices['2']
                game.pointsGain+=1
                    

                print("Purchase complete")
                terminal.log(terminal,'Total points : ' + str(game.points))
                
            def Item3(self,Shop):
                if game.points < Shop.Items.Prices['3']:
                    terminal.log(terminal,"Not enough money")
                    return
                
                if self.ItemsBought['3'] == 1:
                    terminal.log(terminal,"Already bought")
                    return
                
                self.thingThatWillProbBeRemoved(self,'3')

                game.points-=Shop.Items.Prices['3']
                game.pointsModifier+=0.5
                print("Purchase complete")
                terminal.log(terminal,'Total points : ' + str(game.points))
            
            def Item4(self,Shop):
                if Shop.Items.Prices['4'] > game.points:
                    terminal.log(terminal,"Not enough money")
                    return
                if self.ItemsBought['4'] == 1:
                    terminal.log(terminal,"Already bought")
                    return
                self.thingThatWillProbBeRemoved(self,'4')
                terminal.log(terminal,"Bought")
            functionDict = {
                '1' : Item1,
                '2' : Item2,
                '3' : Item3,
                '4' : Item4
            }
            
    def init(self):
        Items = self.Items
        
        print("--------------------------------- Shop ---------------------------------")
        
        for x,y in self.Items.Items.items():
            print(f"Item {x} :  {y} | Price :  {str(self.Items.Prices[x])}")# | Amount Bought : " + str(self.Items.Functions.ItemsBought2[x]))
        
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
    helpList = ["Help - Brings up this page","Shop - Brings up the shop",'Mine - Increase money']

    #log
    def log(self,Message):
        self.currentMessage+=1
        self.message.append(input(f"{Message}\n"))
    
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
        for i in terminal.helpList:
            if i == terminal.helpList[len(terminal.helpList)-1]:
                terminal.log(terminal,i)
            print(i)  

    #Mine Command  
    def MineCommand():

        #Increase pointsModifier when youve used Mine ten times
        if game.pointsUsed+1 >= 10:
            game.pointsUsed = 0 
            game.pointsModifier += .1
        
        pointsGained = Decimal(str(game.pointsGain * game.pointsModifier)).quantize(Decimal('.01'), rounding=ROUND_UP) #Multiply pointsGain and pointsModifier then round it up
        game.points += pointsGained # add the points gained
        game.pointsUsed+=1 # increase pointsUsed
        
        #Print pointsGained and points
        print(f'Gained {str(pointsGained)} points')
        terminal.log(terminal,f'You now have {str(game.points)} points')
    
    #Charge Command
    def Charge():
            if game.power < game.maxbattery:
                game.power = game.power + game.rechargeRate
                # Leaving cooldown out for  now dont feel like doing it
                # game.chargeCooldown = true
                #setTimeout(() => {
                #    game.chargeCooldown = false;
                #, 3000); // 5 seconds cooldown
            elif game.power == game.maxbattery: 
                return terminal.log("Full charge.")
                terminal.log(f"Current battery: {game.power}")
    
    def balance():
        terminal.log(f"Your current balance is {game.points} points.")
    def update():
        if (game.power <= 0):
            game.xp = game.xp + 10;
            terminal.log("Gained 10 exp.")
            if (game.xp == game.expToLevel):
                game.skillpoints = game.skillpoints + 1
                terminal.log("Leveled up!")
            
            return
        

        game.powerpoints = game.power / game.antipower
        game.power -= 1

        game.pointcalc()

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
            print(f"You caught a {self.name}!")
            game.points += self.price
            terminal.log(terminal,f"'{self.desc}'")
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
while "fiiiiiiiiiiiiiiiish":
    for x in terminal.Commands:
        if terminal.message[terminal.currentMessage].lower() == x:
            terminal.found = True
            if terminal.message[terminal.currentMessage].lower() == 'shop':
                terminal.useCommand(terminal,x,Shop)
            else:
                terminal.useCommand(terminal,x)
    if terminal.found != True:
        terminal.log(terminal,f"Error : '{terminal.message[terminal.currentMessage].lower()}' not defined. Please try again or enter 'help' to see a list of commands")
    else:
        terminal.found = False
