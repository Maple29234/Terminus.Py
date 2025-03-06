from decimal import Decimal, ROUND_UP
from datetime import date 
import random
import ast

class Game:
    def __init__(self):
        self.power = 0.00
        self.maxbattery = 15.00
        self.powerModifier = 1.00    
        self.points = 123123
        self.powerGain = 1
        self.chargeUsed = 0  
        self.rechargeRate = 1
        self.upgStage = 0
        self.xp = 0
        self.expToLevel = 100
        self.varDict = {
            'begin' : False,
            'index' : False,
            'doctype' : False,
            'configyml' : False
        }
        self.infShop = False
    def checker(self,var):
        self.varDict[var] = True
        foo = 0
        for x in self.varDict.values():
            if x == True:
                foo +=1
        if foo == 4:
            self.infShop = True
            terminal.log("Inf shop unlocked")
        
        

class Terminal:
    def __init__(self):
        #declare variables and add commands
        
        self.found = False
        self.message = []
        self.currentMessage = -1
        self.tDate = date.today() 
        self.helpStr = "Help - Brings this up\nShop - Brings up the shop\nCharge - Increase power\nUpdate - Convert power into points\nBalance - Prints your point balance\nGithub - Shows the github repo link\nCredits - Shows the credits\nDiscord - Gives a link to the terminus discord\nSave - Saves your game. MAKE SURE TO SAVE\nLoad - Loads your most recent save"
        self.commands = {}
        
        self.shark = self.fish("Shark", "An endangered sand tiger shark, you are now in jail for killing an endangered species",500,1)
        self.salmon = self.fish("Salmon", "A sillier lil fish",30,45)
        self.cod = self.fish("Cod", "A silly lil fish", 25, 50) #add the fish
        self.addCommand("shop",shop.shopCommand)
        self.addCommand("charge",self.Charge)
        self.addCommand("update",self.update)
        self.addCommand("balance",self.balance)
        self.addCommand("catchmeafish",self.catchmeafish)
        self.addCommand("help",self.help)
        self.addCommand("github",self.github)
        self.addCommand("credits",self.credits)
        self.addCommand("discord",self.discord)
        self.addCommand("save",self.save)
        self.addCommand("load",self.load)

    def log(self,Message):
        #logs a new input in message
        self.currentMessage+=1
        self.message.append(input(f"{Message}\n"))

    def startMessage(self):
        #first message with easter eggs
        tDate = self.tDate
        if random.randrange(0, 10000) == random.randrange(0,100):
            print("Unwelcome to AntiTerminus.")
            
        elif tDate.month == 1 and tDate.day == 1: 
            print("Happy New Year! Welcome to Terminus.py")
                
        elif tDate.month == 2 and tDate.day == 4:
            print("It's Terminus.py anniversary! Welcome!")
            
        print("Welcome to Terminus.py")
        terminal.log("You can type 'help' to see available commands")
    
    #Commands
    
    #Next Command
    def nextCommand(self):
        #checks command list for message, if message is not in commmand list then log an error
        try:
            message = self.message[self.currentMessage].lower().split()[0]
        except IndexError:
            self.log(f"Error : '{self.message[self.currentMessage]}' not defined. Please try again or enter 'help' to see a list of commands")
            return
        if message in self.commands:
            self.useCommand(message)
        else:
            self.log(f"Error : '{message}' not defined. Please try again or enter 'help' to see a list of commands")

    #Use Command
    def useCommand(self,Name):
        self.commands[Name]()#Check if Arg was used

    #Add Command
    def addCommand(self,CommandName : str,Command):
        self.commands.update({CommandName : Command})#Add line to Commands

    #help command
    def help(self):
        terminal.log(self.helpStr)
    
    #Charge Command
    def Charge(self):
        #increase power
        #Increase powerModifier when youve used Mine ten times
        
            
        powerGained = Decimal(str(game.powerGain * game.powerModifier)).quantize(Decimal('.01'), rounding=ROUND_UP) #Multiply powerGain and powerModifier then round it up
        game.power = Decimal(game.power) + powerGained # add the points gained
        game.chargeUsed+=1 # increase chargeUsed
        if game.chargeUsed >= 10:
            game.chargeUsed = 0 
            game.powerModifier += .1
        if game.power >= game.maxbattery: 
            game.power = game.maxbattery
            return self.log(f"Full charge. \n Battery : {game.power}")
        self.log(f"Gained {str(powerGained)} power\nCurrent battery: {game.power}")
    
    #balance command      
    def balance(self):
        terminal.log(f"Your current balance is {game.points} points.")
        
    #update command
    def update(self):
        #Increase powerModifier when youve used Mine ten times
        if game.chargeUsed+1 >= 10:
            game.chargeUsed = 0 
            game.powerModifier += .1
        
        game.points += game.power
        terminal.log(f'Gained {str(game.power)} points\nYou now have {str(game.points)} points')
        game.power = 0
    #Fiiiish
    class fish:
        def __init__(self,name : str, desc : str, price : int, chance : int):
            self.name = name
            self.desc = desc
            self.price = price
            self.chance = chance #Out of 100
        
        def catchafish(self):
            didyacatchit = random.randrange(1, 100)
            if didyacatchit <= self.chance:
                print(f"You caught a {self.name}!")
                game.points += self.price
                terminal.log(f"'{self.desc}'")
            else:
                terminal.log('You caught nothing, you are a failure') #Sadge :(
    #Fish command
    def catchmeafish(self):
        fishIndex = [self.cod,self.salmon,self.cod,self.salmon,self.cod,self.cod,self.salmon,self.cod,self.salmon,self.shark]
        random.choice(fishIndex).catchafish() #Add your own fish.catchafish here! without it the fish no catchy watchy with this function :3
    def credits(self):
        terminal.log("Developer - @Maple531 on discord \n Fork of @Rando-Idiot's Terminus")
    def discord(self):
        terminal.log("You can find me and other people who either hate this game or enjoy it here: https://discord.gg/kYyEQ2hjPs")
    def github(self):
        terminal.log("https://github.com/Maple29234/Terminus.Py/tree/main")
    def save(self):
        vars = {
            'power' : game.power,
            'points' : game.points,
            'maxbattery' : game.maxbattery,
            'powerModifier' : game.powerModifier,
            'powerGain' : game.powerGain,
            'rechargeRate' : game.rechargeRate,
            'upgStage' : game.upgStage,
            'xp' : game.xp,
            'expToLevel' : game.expToLevel,
            'varDict' : game.varDict,
            'infShop' : game.infShop
            
            }
        with open('save.txt','w') as f:
            f.write(str(vars))
        terminal.log("Saved")
    def load(self):
        with open('save.txt','r') as f:
            vars = ast.literal_eval(f.read())
        for x in vars:
            setattr(game,x,vars[x])
        terminal.log("Loaded")
    

class Item:
    def __init__(self, name: str, price: int | float): 
        self.name = name # initialize these members in this class, not another one!
        self.price = price
        tempName = name.split(':')[0].lower()
        if tempName in game.varDict:
            self.bought = game.varDict[tempName]

    def buy(self, game) -> bool:
        if game.points < self.price: 
            terminal.log("Not enough points") 
            return False 
        if self.bought:
            terminal.log("Already bought")
            return False
        
        game.points -= self.price 
        if hasattr(self, 'bought'):
            self.bought = True 
        terminal.log(f"Bought {self.name}\nTotal points left: {game.points}")
        return True

class ItemInit(Item): #I really dont know what to name this :/
    def __init__(self,price : int | float, name : str, boughtfunc):
        """_summary_

        Args:
            price (int | float): the price of the item
            name (str): name of the item
            boughtfunc (_type_): lambda function returning a list with 3 items, the name of the variable to modify, the amount to modify, and a short version of the item name
        """
        self.price = price
        self.name = name
        self.func = boughtfunc
        super().__init__(self.name,self.price)
    def buy(self,game) -> bool:
        success = super().buy(game) #calls Item.buy()
        if success:
            vars = self.func(game) # gets vars from lambda
            setattr(game,vars[0],vars[1]) #changes the variables specified by the lambda
            game.checker(vars[2]) #sets the bought variable of the item specified by lambda

        return success

class Shop:
    def __init__(self, items : dict[Item]):
        self.items = items
    
    def buy(self, item_name: str, game):
        return self.items[item_name].buy(game)

    def shopCommand(self):
        def checker(message : str):
#                if not message.isdigit():
#                    terminal.log(f"Error : Requires 'int' got 'str'.")
                try:
                    self.buy(message, game)
                    return
                except KeyError:
                    terminal.log(f"Error : Item '{message}' not found. Check list of items by doing 'shop'.")
        #end ofchecker
        message = terminal.message[terminal.currentMessage].lower().split()
        if len(message) == 2:
            return checker(message[1])
        i=1
        for x in self.items.values():
            print(f'{i} : {x.name} | Price : {x.price}')
            i+=1
    
        terminal.log("What would you like to buy? (Use Int)")
        checker(terminal.message[terminal.currentMessage])

game = Game()
shop = Shop({
    '1' : ItemInit(5,"Begin: The Beginning",lambda game: ['powerModifier',game.powerModifier+.1,'Begin']),
    '2' : ItemInit(20,"Index: Index.html",lambda game: ['powerGain',game.powerGain+1,'Index']),
    '3' : ItemInit(50,"Doctype: <!DOCTYPE HTML>",lambda game: ['powerModifier',game.powerModifier+.5,'Doctype']),
    '4' : ItemInit(100,"Configyml: config.yml", lambda game: ['powerModifier',game.powerModifier+1, 'Configyml'])
})
terminal = Terminal()


terminal.startMessage()
while True:
    terminal.nextCommand()