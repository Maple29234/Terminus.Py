from decimal import Decimal, ROUND_UP
from datetime import date 
import random
import ast

class Game:
    def __init__(self):
        self.infShop1Price = 500 #increase maxBattery
        self.infShop2Price = 1000 #increase rechargeRate
        self.infShop3Price = 2000 #increase basePointsGain
        self.infShop4Price = 3000 #increase pointsModifier
        self.power = 0.00
        self.maxBattery = 15.00
        self.pointsModifier = 1.00
        self.points = 0
        self.basePointsGain = 1
        self.updateUsed = 0
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
    def updateInfShopPrices(self):
        i = 0
        for x in infShop.items.values():
            i+=1
            x.price = getattr(self, f"infShop{str(i)}Price")

    def infShopChecker(self, var):

        self.varDict[var] = True
        foo = 0
        for x in self.varDict.values():
            if x:
                foo +=1
        if foo == 4:
            self.infShop = True
            terminal.addCommand("infshop",infShop.shopCommand)
            terminal.helpStr += "\nInfshop - Shows infinitely purchasable items."
            print("You've unlocked the inf shop. Check 'help' for details.")



class Terminal:
    def __init__(self):
        #declare variables and add commands
        
        self.found = False
        self.message = []
        self.currentMessage = -1
        self.tDate = date.today() 
        self.helpStr = "Help - Brings this up\nTutorial - Brings up a tutorial\nShop - Brings up the shop\nCharge - Increase power\nUpdate - Convert power into points\nBalance - Prints your point balance\nGithub - Shows the github repo link\nCredits - Shows the credits\nDiscord - Gives a link to the terminus discord\nSave - Saves your game. MAKE SURE TO SAVE\nLoad - Loads your most recent save"
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
        #self.addCommand("debug",lambda:breakpoint()) #for debugging
        self.addCommand("tutorial",self.tutorial)

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
        terminal.log("You can type 'help' to see available commands. Type 'tutorial' to see a tutorial. Use 'save' to save and 'load' to load your most recent save")
    
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
    def useCommand(self,name):
        self.commands[name]()#Check if Arg was used

    #Add Command
    def addCommand(self,commandName : str,command):
        self.commands.update({commandName : command})#Add line to Commands

    #help command
    def help(self):
        terminal.log(self.helpStr)
    
    #Charge Command
    def Charge(self):
        game.power += game.rechargeRate
        if game.power >= game.maxBattery:
            game.power = game.maxBattery
            return self.log(f"Full charge. \n Battery : {game.power}")
        self.log(f"Gained {str(game.rechargeRate)} power\nCurrent battery: {game.power}")
    
    #balance command
    def balance(self):
        self.log(f"Your current balance is {game.points} points.")

    #update command
    def update(self):
        pointsGained = Decimal(str(game.power * (game.pointsModifier + game.basePointsGain))).quantize(Decimal('.01'), rounding=ROUND_UP) #Add power then multiply BasePointsGain and pointsModifier then round it up
        game.power = 0
        game.updateUsed+=1 # increase chargeUsed
        if game.updateUsed >= 10:
            game.updateUsed = 0
            game.pointsModifier += .1
        
        game.points += pointsGained
        self.log(f'Gained {str(pointsGained)} points\nYou now have {str(game.points)} points')
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
        self.log("Developer - @Maple531 on discord \n Fork of @Rando-Idiot's Terminus")
    def discord(self):
        self.log("You can find me and other people who either hate this game or enjoy it here: https://discord.gg/kYyEQ2hjPs")
    def github(self):
        self.log("https://github.com/Maple29234/Terminus.Py/tree/main")
    def save(self):
        vars = {
            "power" : game.power,
            "points" : str(game.points),
            "maxbattery" : game.maxBattery,
            "powerModifier" : game.pointsModifier,
            "powerGain" : game.basePointsGain,
            "rechargeRate" : game.rechargeRate,
            "upgStage" : game.upgStage,
            "xp" : game.xp,
            "expToLevel" : game.expToLevel,
            "varDict" : game.varDict,
            "infShop" : game.infShop,
            "infShop1Price" : game.infShop1Price,
            "infShop2Price": game.infShop2Price,
            "infShop3Price": game.infShop3Price,
            "infShop4Price": game.infShop4Price
        }
        with open('save.json', 'w') as f:
            f.write(str(vars))
        self.log("Saved")
    def load(self):
        with open('save.json', 'r') as f:
            vars = ast.literal_eval(f.read())
        for x in vars:
            if x == "points":
                setattr(game,x,Decimal(vars[x]))
                continue
            setattr(game,x,vars[x])
        if game.infShop:
            self.addCommand("infshop", infShop.shopCommand)
            self.helpStr += "\nInfshop - Shows infinitely purchasable items."
        game.updateInfShopPrices()
        self.log("Loaded")
    def tutorial(self):
        self.log("1. Use 'charge' to gain power\n2. After you've gotten max power (or just whenever) sell your power by using 'update'\n3. Check shop and buy stuff by using 'shop'\n4. Use 'save' to save and 'load' to load your most recent save")

class Item:
    def __init__(self, name: str, price: int | float): 
        self.name = name # initialize these members in this class, not another one!
        self.price = price
        tempName = name.split(':')[0].lower()
        if tempName in game.varDict:
            self.bought = game.varDict[tempName]

    def buy(self) -> bool:
        if game.points < self.price: 
            terminal.log("Not enough points") 
            return False 
        if hasattr(self,'bought'):
            if self.bought:
                terminal.log("Already bought")
                return False
        
        game.points -= Decimal(self.price)
        if hasattr(self, 'bought'):
            self.bought = True 
        terminal.log(f"Bought {self.name}\nTotal points left: {game.points}")
        return True

class ItemInit(Item): #I really don't know what to name this :/
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
    def buy(self) -> bool:
        success = super().buy() #calls Item.buy()
        if success:
            lambdaVars = self.func(self) # gets vars from lambda
            setattr(game, lambdaVars[0], lambdaVars[1]) #changes the variables specified by the lambda
            game.infShopChecker(lambdaVars[2]) #sets the bought variable of the item specified by lambda
            if len(lambdaVars) > 3:
                setattr(lambdaVars[3],lambdaVars[4],lambdaVars[5]) # for infShop's prices to increase as you buy stuff
                setattr(game,lambdaVars[6],lambdaVars[7]) #this is probably a terrible way to do it isnt it? eh im sure its fine

        return success

class Shop:
    def __init__(self, items : dict[str,ItemInit]):
        self.items = items
    def buy(self, item_name: str):
        return self.items[item_name].buy()

    def shopCommand(self):
        def checker(message : str):
                try:
                    self.buy(message)
                    return
                except KeyError:
                    terminal.log(f"Error : Item '{message}' not found. Check list of items by doing 'shop'.")
        #end of checker
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
    '1' : ItemInit(5,"Begin: The Beginning", lambda self: ['basePointsGain', game.basePointsGain + 10, 'Begin']),
    '2' : ItemInit(20,"Index: Index.html", lambda self: ['pointsModifier', game.pointsModifier + .5, 'Index']),
    '3' : ItemInit(50,"Doctype: <!DOCTYPE HTML>", lambda self: ['pointsModifier', game.pointsModifier + .5, 'Doctype']),
    '4' : ItemInit(100,"Configyml: config.yml", lambda self: ['basePointsGain', game.basePointsGain*2, 'Configyml'])
})
infShop = Shop({
    '1' : ItemInit(game.infShop1Price,"Increase maxBattery", lambda self: ['maxBattery', game.maxBattery*1.5,'maxBattery',self,"price",round(self.price*1.2),"infShop1Price",game.infShop1Price*1.2]),
    '2' : ItemInit(game.infShop2Price,"Increase rechargeRate", lambda self: ['rechargeRate', game.rechargeRate*2,'rechargeRate',self,"price",round(self.price*1.2),"infShop2Price",game.infShop2Price*1.2]),
    '3' : ItemInit(game.infShop3Price,"Increase basePointsGain", lambda self: ['basePointsGain', game.basePointsGain*1.5,'basePointsGain',self,"price",round(self.price*1.2),"infShop3Price",game.infShop3Price*1.2]),
    '4': ItemInit(game.infShop4Price, "Increase pointsModifier",lambda self: ['pointsModifier',game.pointsModifier*1.1,'pointsModifier',self,"price",round(self.price * 1.2), "infShop4Price", game.infShop4Price*1.2]),

})
terminal = Terminal()


terminal.startMessage()
while True:
    terminal.nextCommand()