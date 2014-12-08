from Tkinter import *
from eventBasedAnimationClass import EventBasedAnimationClass
import math, random, sys
from threading import *
import tkMessageBox
import tkSimpleDialog

class CardGameDialog(tkSimpleDialog.Dialog):
    """Custom Dialog boxes, which the user uses to specify 
    attribute of the game."""

    def __init__(self,canvas,dialogType,minMax=False,
                 canPass=True,seedText=("",),numberOfPlayers=4):
        """Initializes a dialog"""
        self.dialogType = dialogType
        self.canPass = canPass
        self.result = ""
        self.entrys = []
        self.numberOfPlayers = numberOfPlayers
        self.seedText = seedText
        if (minMax): (self.minBid,self.maxBid) = minMax
    # Next 3 Lines:
    # http://svn.python.org/projects/python/trunk/Lib/lib-tk/tkSimpleDialog.py
        import Tkinter
        parent = Tkinter._default_root
        tkSimpleDialog.Dialog.__init__(self, parent)

    def body(self, master):
        """Initializes the body of the dialog: labels, text fields, etc."""
        if self.dialogType == "bid": self.initBidDialog(master)
        elif self.dialogType == "trump": self.initTrumpDialog(master)
        elif self.dialogType == "bidtrump": self.initBidTrumpDialog(master)
        elif self.dialogType == "omitCards": self.initOmitCardsDialog(master)
        elif self.dialogType == "points": self.initPointsDialog(master)
        elif self.dialogType == "startingPlayer":self.initStartingPlayer(master)
        elif self.dialogType == "pickTrump": self.initPickTrumpDialog(master)
        elif self.dialogType == "partners": self.initPartnersDialog(master)
        elif self.dialogType == "pickBid": self.initPickBidDialog(master)
        elif self.dialogType == "cardOrder": self.initCardOrderDialog(master)
        elif self.dialogType == "playerNames":self.initPlayerNamesDialog(master)
        elif self.dialogType=="illegalSuits":self.initIllegalSuitsDialog(master)
        elif self.dialogType == "winner": self.initWinnerDialog(master)
        elif self.dialogType == "pass": self.initPassDialog(master)
        elif self.dialogType == "dealOrder": self.initDealOrderDialog(master)
        elif self.dialogType == "loadPreset": self.initLoadPresetDialog(master)
        elif self.dialogType == "savePreset": self.initSavePresetDialog(master)
        elif self.dialogType == "numberOfPlayers": 
            self.initNumberOfPlayersPresetDialog(master)
        elif self.dialogType == "cardsPerPlayer": 
            self.initCardsPerPlayerPresetDialog(master)
        elif self.dialogType == "afterRound": 
            self.initAfterRoundPresetDialog(master)
        return self.entrys[0] # initial focus

    def initEntries(self, numOfEntrys, rowCol, master):
        """Initializes the number and locations of Entrys in the dialog"""
        for num in xrange(numOfEntrys):
            text = StringVar()
            self.entrys.append(Entry(master,textvariable=text))
            self.entrys[-1].grid(row=rowCol[num][0],column=rowCol[num][1])
            text.set(self.seedText[num])

    def initBidDialog(self, master):
        """Initializes the bid dialog, used to bid during gameplay"""
        Label(master, text="Bid:").grid(row=0)
        self.initEntries(1,[(0,1)],master)

    def initTrumpDialog(self, master):
        """Initializes the trump dialog, used to set trump during gameplay"""
        Label(master, text="Trump:").grid(row=0)
        self.initEntries(1,[(0,1)],master)

    def initBidTrumpDialog(self, master):
        """Initializes the bidTrump dialog, used to bid a number and a trump"""
        Label(master, text="Bid:").grid(row=0)
        Label(master, text="Trump:").grid(row=1)
        self.initEntries(2,[(0,1),(1,1)],master)

    def initOmitCardsDialog(self, master):
        """Initializes the omitCards dialog"""
        instructions =("Write suits and/or values to omit separated by a" +
                       " comma. Ex: 'hearts, clubs 2-7, spades A, clubs Q, K'."+
                       "\nNOTE: WRITE SUIT BEFORE VALUE")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initPointsDialog(self, master):
        """Initializes the points dialog"""
        instructions=("Write suits and/or values, followed by a point value,"+
                      " separated by commas. Ex: 'hearts 1, spades Q 13, J 1'."+
                       "\nNOTE: WRITE SUIT BEFORE VALUE")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initStartingPlayer(self, master):
        """Initializes the startingPlayer dialog"""
        instructions = ("Write a single suit and value to indicate which card"+
                         " must start.EX: 'clubs 2'\nOtherwise, write 'dealer'"+
                         " to indicate that the person to the left of the"+
                         " dealer starts, or 'winner' for the winner of the"+
                         " bid to start.  \nNOTE: WRITE SUIT BEFORE VALUE")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initPickTrumpDialog(self, master):
        """Initializes the pickTrump dialog, 
        used to pick trump before gameplay"""
        instructions = ("Write a single suit to be trump.  If you want the"+
                        " winner of the bid to set trump,\nwrite 'winner'"+
                        " (you MUST HAVE A BID for this to work.)\n  If"+
                        " you want a random trump, write 'random'.")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initPartnersDialog(self, master):
        """Initializes the partners dialog"""
        instructions = "How are partners determined? EX: 'across'"
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initPickBidDialog(self, master):
        """Initializes the pickBid dialog, used to pick bid before gameplay"""
        Label(master, text="Min Bid:").grid(row=0, column=0)
        Label(master, text="Max Bid:").grid(row=1, column=0)
        instructions = ("BidType:'oneByOne' if everyone bids only once,"+
                        " 'round' if people keep bidding in a circle \nuntil"+
                        " everyone passes, and 'faceOff' if two people bid"+
                        " back and forth until one passes.")
        Label(master, text=instructions).grid(row=2, column=0)
        Label(master, text="Can Pass?: (Y/N)").grid(row=3, column=0)
        instructions = ("Can the player before, after, no one, or everyone"+
                        " match the bid? EX: 'after'")
        Label(master, text=instructions).grid(row=4, column=0)
        self.initEntries(5,[(0,1),(1,1),(2,1),(3,1),(4,1)],master)

    def initCardOrderDialog(self, master):
        """Initializes the cardOrder dialog, used to 
        pick which cards are higher than others"""
        instructions=("Write the order of cards, lowest to highest: EX:"+
                      " '2,3,4,5,6,7,8,9,10,J,Q,K,A'")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initPlayerNamesDialog(self, master):
        """Initializes the playerNames dialog"""
        Label(master, text="Enter Player Names:").grid(row=0, column=1)
        if self.numberOfPlayers == 3:
            self.initEntries(3,[(1,1),(2,2),(2,0)],master)
        elif self.numberOfPlayers == 4:
            self.initEntries(4,[(1,1),(2,2),(3,1),(2,0)],master)
        elif self.numberOfPlayers == 5:
            self.initEntries(5,[(1,1),(2,2),(3,2),(3,0),(2,0)],master)

    def initIllegalSuitsDialog(self,master):
        """Initializes the illegalSuits dialog"""
        instructions=("Write suits that the user cannot play until a card\n"+
                "from that suit has first been discarded. EX: 'clubs, hearts'")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initWinnerDialog(self, master):
        """Initializes the winner dialog"""
        instructions=("Designate how someone wins the game.  Possible options:"+
                      " 'leastPoints', 'mostPoints','points>=Bid',\n"+
                      "'points<=Bid', 'points==Bid', 'mostTricks', "+
                      "'leastTricks', 'tricks==bid', 'tricks>=bid', \n"+
                      "'tricks<=bid'.  NOTE:  You MUST HAVE points/bid for the"+
                      "corresponding option to work!")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initPassDialog(self, master):
        """Initializes the pass dialog"""
        Label(master, text="Number of cards to pass?").grid(row=0)
        instructions = "Direction(s)? EX: 'left, right, across, none'"
        Label(master, text=instructions).grid(row=2)
        self.initEntries(2,[(1,0),(3,0)],master)

    def initDealOrderDialog(self,master):
        """Initializes the dealOrder dialog"""
        Label(master, text="Number of cards to deal before bid?").grid(row=0)
        Label(master, text="Number of cards to deal after bid?").grid(row=2)
        self.initEntries(2,[(1,0),(3,0)],master)

    def initLoadPresetDialog(self,master):
        """Initializes the loadPreset dialog"""
        instructions =("Write the name of your preset file"+
                       " (one word, no special characters.)")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initSavePresetDialog(self,master):
        """Initializes the loadPreset dialog"""
        instructions =("Write a single word, no special characters, for your"+
                       " preset file name.  You will need this to load your"+
                       " preset file later.")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initNumberOfPlayersPresetDialog(self, master):
        """Initializes the numberOfPlayers dialog"""
        instructions = "How many players (min=3, max=5) will be in the game?"
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initCardsPerPlayerPresetDialog(self, master):
        """Initializes the cardsPerPlayer dialog"""
        instructions = "How many cards should each player recieve?"
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def initAfterRoundPresetDialog(self, master):
        """Initializes the afterRound dialog"""
        instructions = ("By how many cards should the number of cards per"+
                      " player change per round?  Can be positive or negative"+
                      " numbers. Ex: '-1'")
        Label(master, text=instructions).grid(row=0)
        self.initEntries(1,[(1,0)],master)

    def destroy(self):
        """Destroys the dialog if applicable"""
        if (self.dialogType == "trump" and self.entrys[0].get() == ""):
            warning="Sorry, you must set a trump, or 'no' for no trump"
            tkMessageBox.showwarning("Opps!",warning)
            return
        elif (self.dialogType == "bid" and not self.canPass and 
              self.entrys[0].get() == ""): 
            tkMessageBox.showwarning("Cannot Pass","You cannot pass.")
        else:
            tkSimpleDialog.Dialog.destroy(self)

    def validate(self):
        """Determines whether the entered bid/trump is legal"""
        if self.dialogType == "bid": return self.isBidLegal()
        elif self.dialogType == "trump": return self.isTrumpLegal()
        elif self.dialogType == "bidtrump": self.isBidTrumpLegal()
        else: return 1

    def isBidLegal(self):
        """Determines whether the entered bid is legal"""
        if (self.entrys[0].get().isdigit() and 
            self.minBid <= int(self.entrys[0].get()) <= self.maxBid): 
            return 1
        else:
            errorMessage = "Please enter only a number between %d and %d"
            errorMessage = errorMessage % (self.minBid,self.maxBid)
            tkMessageBox.showwarning("Invalid Bid", errorMessage)
            return 0

    def isTrumpLegal(self):
        """Determines whether the entered trump is legal"""
        if (self.entrys[0].get()[0].lower() in ["d","c","h","s","n"]): return 1
        else:
            tkMessageBox.showwarning("Invalid Trump",
                    "Please enter only a valid suit or no trump")
            return 0

    def isBidTrumpLegal(self):
        """Determines whether the entered bid and trump is legal"""
        if (self.entrys[0].get().isdigit()):
            if (self.entrys[1].get()[0].lower() in ["d","c","h","s","n"]): 
                return 1
            else:
                tkMessageBox.showwarning("Invalid Trump",
                        "Please enter only a valid suit or no trump")
                return 0
        else:
            tkMessageBox.showwarning("Invalid Bid",
                                     "Please enter only a number")
            return 0

    def apply(self):
        """Sets the Dialog's reuslt attribute, so the text can be 
        read/interpreted by the game"""
        result = []
        for entry in self.entrys:
            result.append(entry.get())
        self.result = result

class Button(object):
    """Custom button class"""

    def __init__(self, bbox, callback, text="Button", color="white",
                font="Arial 20 bold"):
        """Initializes the button"""
        self.bbox = bbox
        self.callback = callback
        self.text = text
        self.color = color
        self.font = font
        (self.width,self.height) = (bbox[2]-bbox[0],bbox[3]-bbox[1])
        self.highlighted = False

    def isClickInsideBox(self,x,y):
        """Determines whether the user clicked the button"""
        bbox = self.bbox
        if (bbox[0]<x<bbox[2] and bbox[1]<y<bbox[3]):
            self.highlighted = True
            return True
        else: return False

    def clicked(self):
        """Calls the button's callback function"""
        self.callback()

    def draw(self, canvas):
        """Draws the button"""
        (x0,y0,x2,y2) = self.bbox
        (x1,y1,x3,y3) = (x2,y0,x0,y2)
        (cx,cy) = ((x0+x2)/2,(y0+y2)/2)
        cornerRad = self.width/5
        # Bbox which includes rounded corners
        bbox = (x0,y0,x0+cornerRad,y0,x1-cornerRad,y1,x1,y1,x1,y1+cornerRad,
                x1,y2-cornerRad,x2,y2,x2-cornerRad,y2,x3+cornerRad,y2,x3,y3,
                x3,y3-cornerRad,x3,y0+cornerRad)
        color = self.color if self.highlighted == False else "white"
        canvas.create_polygon(*bbox, fill=color, smooth=True, outline="black")
        canvas.create_text(cx,cy,text=self.text,font=self.font)

class DragAndDrop(Button):
    """Let's the user drag and drop a button, and perform an action upon drop"""

    def draw(self, canvas,cx="",cy=""):
        """Draws the dragAndDrop"""
        canvas.delete(self.text.replace(" ",""))
        if not cx==cy=="": 
            (x0,y0,x2,y2) = (cx-self.width/2,cy-self.height/2,
                             cx+self.width/2,cy+self.height/2)
        else: (x0,y0,x2,y2) = self.bbox
        (x1,y1,x3,y3) = (x2,y0,x0,y2)
        (cx,cy) = ((x0+x2)/2,(y0+y2)/2)
        cornerRad = self.width/5
        # Bbox which includes rounded corners
        bbox = (x0,y0,x0+cornerRad,y0,x1-cornerRad,y1,x1,y1,x1,y1+cornerRad,
                x1,y2-cornerRad,x2,y2,x2-cornerRad,y2,x3+cornerRad,y2,x3,y3,
                x3,y3-cornerRad,x3,y0+cornerRad)
        canvas.create_polygon(*bbox, fill=self.color, smooth=True, 
                                outline="black",tag=self.text.replace(" ",""))
        canvas.create_text(cx,cy,text=self.text,font="Arial 20 bold",
                            tag=self.text.replace(" ",""))
        self.bbox = (x0,y0,x2,y2)

class Card(object):
    """A single card with a suit and value"""
    cardCount = 0

    def __init__(self, suit, value, valueOrder=""):
        """Initializes the card"""
        self.suit = suit
        self.value = value
        self.aboutToPass = False
        self.points = 0
        (self.maxWidth, self.maxHeight) = (100,140)
        # self.rotation = 0
        if valueOrder == "":
            self.valueOrder = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",
                                9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}
        else: self.valueOrder = valueOrder
        self.valueConversion = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",
                                9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}
        self.bbox = None
        self.playerWhoOwnsTheCard = None
        self.ID = Card.cardCount
        Card.cardCount += 1

    def drawCard(self, canvas, imageDict,highlighted=False):
        """Draws the card"""
        tag=str(self) + str(self.ID)
        canvas.delete(tag)
        (x0,y0,x1,y1,x2,y2,x3,y3) = self.bbox
        (cx,cy) = ((x0+x2)/2, (y0+y2)/2)
        cornerRad = self.width/5
        # Bbox which includes rounded corners
        bbox = (x0,y0,x0+cornerRad,y0,x1-cornerRad,y1,x1,y1,x1,y1+cornerRad,
                x1,y2-cornerRad,x2,y2,x2-cornerRad,y2,x3+cornerRad,y2,x3,y3,
                x3,y3-cornerRad,x3,y0+cornerRad)
        if highlighted:
            canvas.create_polygon(*bbox, fill="white", outline="black",
                                    smooth=True,width=10,tag=tag)
        else: canvas.create_polygon(*bbox, fill="white", outline="black",
                                    smooth=True,tag=tag)
        value = self.valueConversion[self.value]
        suitImage = imageDict[self.suit]
        fontSize = self.width*40/125
        font = "Arial %d" %fontSize
        canvas.create_text(x0+(cx-x0)/3,y0+(cy-y0)/3,text=value,anchor=CENTER,
                            font=font,tag=tag)
        canvas.create_text(x2-(x2-cx)/3,y2-(y2-cy)/3,text=value,anchor=CENTER,
                            font=font,tag=tag)
        canvas.create_image(cx, cy, image=suitImage, anchor=CENTER,tag=tag)

    def move(self, dx, dy):
        """Moves the card"""
        bbox = self.bbox
        bbox = (bbox[0]+dx, bbox[1]+dy, bbox[2]+dx, bbox[3]+dy,
                bbox[4]+dx, bbox[5]+dy, bbox[6]+dx, bbox[7]+dy)
        self.bbox = bbox

    @staticmethod
    def heightFromWidth(width):
        """Returns the card's height, given a width"""
        return int(3.5*width/2.5)

    @staticmethod
    def widthFromHeight(height):
        """Returns the card's width, given a height"""
        return int(2.5*height/3.5)

    def isXYInsideCard(self, x, y):
        """Determines whether the mouse is on top of or clicked a card"""
        # if self.bbox == None: return False
        (x0,y0,x1,y1,x2,y2,x3,y3) = self.bbox
        if (x0<x<x2 and y0<y<y2):
            return True
        return False

    def __str__(self):
        """Converts Card to string"""
        return "(%d,%d)" % (self.suit, self.value)

    def __repr__(self):
        """Converts Card to repr, used for debugging"""
        return "(%d, %d)" % (self.suit, self.value)

    def setDimensions(self, x0, y0, width):
        """Sets dimensions of the card"""
        self.width = width
        self.height = height = int(3.5*width/2.5)
        self.bbox = (x0,y0,x0+width,y0,x0+width,y0+height,x0,y0+height)

    def adjustPosition(self,x0,y0):
        """Moves the card up if the user wants to pass it"""
        (width,height) = (self.width,self.height)
        if self.aboutToPass == False:
            self.bbox = (x0,y0,x0+width,y0,x0+width,y0+height,x0,y0+height)
        else:
            dy = -20
            self.bbox = (x0,y0+dy,x0+width,y0+dy,x0+width,
                         y0+height+dy,x0,y0+height+dy)

    def resetCard(self):
        """Returns the card to the deck"""
        self.bbox = self.playerWhoOwnsTheCard = None
        self.points = 0

    def __gt__(self, other):
        """Determines which card is greater, used to sort hand"""
        selfVal = self.valueOrder[self.valueConversion[self.value]]
        otherVal = self.valueOrder[self.valueConversion[other.value]]
        if (self.suit > other.suit):
            return True
        if (self.suit == other.suit and selfVal > otherVal):
            return True
        return False

    def __eq__(self,other):
        if (type(other) == Card):
            if (self.suit == other.suit and self.value == other.value):
                return True
        elif (type(other) == tuple):
            if (self.suit == other[0] and self.value == other[1]):
                return True
        return False

    def __ge__(self,other):
        """Determines which card is greater, used to sort hand"""
        return self > other or self == other

    def __lt__(self,other):
        """Determines which card is lesser, used to sort hand"""
        return not self >= other

    def __le__(Self,other):
        """Determines which card is lesser, used to sort hand"""
        return not self > other

class Player(object):
    """Player, contains all the information about a specific player's cards, 
    tricks, points, etc."""

    def __init__(self, name, playerNum):
        """Initializes the player"""
        self.hand = []
        self.tricks = []
        self.name = name
        self.playerNum = playerNum
        self.passCardIndices = []
        self.recievedCards = []
        self.bid = False
        self.partnerPoints = 0

    def resetPlayer(self):
        """Resets player's attributes between rounds"""
        self.hand = []
        self.tricks = []
        self.passCardIndices = []
        self.recievedCards = []
        self.bid = False
        self.partnerPoints = 0

    def getsDealtCard(self, card):
        """Player recieves a card"""
        card.playerWhoOwnsTheCard = self.playerNum
        self.hand.append(card)
        self.sortHand()

    def __str__(self):
        """Converts player to string"""
        text = (self.name + " | Hand: " + str(self.hand) + "\n" + "Tricks: " + 
                str(self.tricks))
        return text

    def playsCardAtIndex(self, index):
        """Player plays a card"""
        return self.hand.pop(index)

    def sortHand(self):
        """Sorts the player's hand"""
        self.hand.sort()

    def numberOfCards(self):
        """Returns number of cards the player has"""
        return len(self.hand)

    def pointsInHand(self):
        """Returns the total points in a player's hand"""
        totalPoints = 0
        for card in self.hand:
            totalPoints += card.points
        return totalPoints

    def pointsInTricks(self):
        """Returns the total points in a player's tricks"""
        totalPoints = 0
        for trick in self.tricks:
            for card in trick:
                totalPoints += card.points
        return totalPoints

    def points(self):
        """Determines the number of points a player and his/her partner have"""
        return self.pointsInTricks() + self.partnerPoints

    def suitsInHand(self):
        """Returns the suits the player has in hand"""
        suits = set()
        for card in self.hand:
            suits.add(card.suit)
        return suits

    def bids(self, bid):
        """Sets the player's bid"""
        self.bid = bid

    def passCards(self):
        """Sets the cards the player will pass"""
        cards = []
        self.passCardIndices.sort()
        for index in xrange(len(self.passCardIndices)):
            card = self.hand.pop(self.passCardIndices[index]-index)
            card.aboutToPass = False
            cards.append(card)
        self.passCardIndices = []
        return cards

    def recievesCards(self, cards):
        """The player recieves cards that another player passed"""
        for card in cards:
            card.playerWhoOwnsTheCard = self.playerNum
            self.recievedCards.append(card)
    
    def addCardsToHand(self):
        """The player adds the recieve cards to his/her hand"""
        for card in self.recievedCards:
            self.hand.append(card)
        self.sortHand()

class Menu(EventBasedAnimationClass):
    """The initial menu the user sees, allows a user to view help or create a 
    game."""
    def __init__(self):
        """Initializes the menu class"""
        self.width = 1000
        self.height = 700
        self.buttons = {}
        self.cards = []
        self.helpCards = []
        self.subview = None
        self.name = "Card Game Creator"
        self.isShowingHelp = False
        super(Menu, self).__init__(self.width, self.height)

    def initAnimation(self):
        """Binds events and sets the suit images"""
        self.root.bind("<Button>", lambda event: self.onMousePressed(event))
        self.root.bind("<ButtonRelease-1>", 
                        lambda event: self.onMouseReleased(event))
        self.canvas.bind("<Motion>", lambda event: self.mouseMotion(event))
        self.imageDict = {0:PhotoImage(file='diamonds.gif').subsample(3,3),
                          1:PhotoImage(file='clubs.gif').subsample(3,3),
                          2:PhotoImage(file='hearts.gif').subsample(3,3),
                          3:PhotoImage(file='spades.gif').subsample(3,3)}
        self.redrawAll()

    def redrawAll(self):
        """Redraws the canvas, background, and buttons"""
        self.canvas.delete(ALL)
        if self.isShowingHelp: 
            self.drawHelp()
            self.drawHelpCards()
        else:
            self.drawTitle()
            self.drawCards()
            self.drawButtons()

    def drawHelp(self):
        """Draws the help menu"""
        helpText = ""
        with open('helpText.txt','rt') as doc: helpText = doc.read()
        helpText = self.splitText(helpText, 60)
        (cx,cy) = (self.width/2,self.height/2)
        self.canvas.create_text(cx,cy,text=helpText,font="Arial 20 bold")
        self.buttons = {}
        (cx,cy) = (self.width/2,self.height-50)
        (width,height) = (300,75)
        self.buttons["back"] = Button((cx-width/2,cy-height/2,cx+width/2,
                                       cy+height/2),lambda:self.back(),"Back",
                                    "green","Arial 40 bold")
        self.buttons["back"].draw(self.canvas)
        cy = 75
        self.canvas.create_text(self.width/2,cy,text="Help",
                                font="Arial 60 bold")


    def splitText(self, text, charPerLine):
        """Splits the help text into lines of a given length"""
        for charI in xrange(1,len(text)/charPerLine):
            charI = charI*charPerLine + charI - 1
            if "\n" in text[text.find("\n", charI-charPerLine)+1:charI]: 
                continue
            splitI = text.find(" ", charI)
            print charI, splitI
            text = text[:splitI+1] + "\n" + text[splitI+1:]
        print repr(text)
        return text
            
    def back(self):
        """Returns from help screen to menu"""
        self.buttons.pop("back")
        self.isShowingHelp = False

    def drawHelpCards(self):
        """Draw the cards on the sides of the help screen"""
        if len(self.helpCards) == 0:
            height = 175
            width = Card.widthFromHeight(height)
            (x0,y0,x1,y1) = (0,0,width,self.height)
            self.createHelpCards(x0,y0,x1,y1)
            (x0,y0,x1,y1) = (self.width-width,0,self.width,self.height)
            self.createHelpCards(x0,y0,x1,y1)
        for card in self.helpCards:
            card.drawCard(self.canvas,self.imageDict)

    def createHelpCards(self,x0,y0,x1,y1):
        """Creates and positions the cards displayed on the help screen"""
        width = x1-x0
        height = Card.heightFromWidth(width)
        numOfCards = (y1-y0)/height
        print numOfCards
        valueOrder = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",
                          9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}
        for card in xrange(numOfCards):
            (suit,value) = (random.randint(0,3),random.randint(2,14))
            self.helpCards.append(Card(suit,value,valueOrder))
            self.helpCards[-1].setDimensions(x0,y0+card*height,width)

    def drawTitle(self):
        """Draws the title of the game"""
        cy = 50
        self.canvas.create_text(self.width/2,cy,text=self.name,
                           font="Arial 60 bold")

    def drawCards(self):
        """Draws the card in the background of the menu"""
        if len(self.cards) == 0:
            height = 200
            width = Card.widthFromHeight(height)
            (x0,y0,x1,y1) = (0,100,self.width,300)
            self.createCards(x0,y0,x1,y1)
            (x0,y0,x1,y1) = (0,300,width*2,500)
            self.createCards(x0,y0,x1,y1)
            (x0,y0,x1,y1) = (self.width-width*2,300,self.width,500)
            self.createCards(x0,y0,x1,y1)
            (x0,y0,x1,y1) = (0,500,self.width,700)
            self.createCards(x0,y0,x1,y1)
        for card in self.cards:
            card.drawCard(self.canvas,self.imageDict)

    def createCards(self,x0,y0,x1,y1):
        """Creates and positions the cards in the background of the menu"""
        height = y1-y0
        width = Card.widthFromHeight(height)
        numOfCards = (x1-x0)/width
        valueOrder = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",
                          9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}
        for card in xrange(numOfCards):
            (suit,value) = (random.randint(0,3),random.randint(2,14))
            self.cards.append(Card(suit,value,valueOrder))
            self.cards[-1].setDimensions(x0+card*width,y0,width)


    def drawButtons(self):
        """Creates and draws the two menu buttons"""
        if ("createGame" not in self.buttons): 
            (cx,cy) = (self.width/2-50,350)
            (width,height) = (300,75)
            self.buttons["createGame"] = Button((cx-width/2,cy-height/2,
                                                cx+width/2,cy+height/2),
                                                lambda:self.createGame(),
                                                "Create Game","green",
                                                "Arial 40 bold")
        if ("help" not in self.buttons): 
            (cx,cy) = (self.width/2+50,450)
            (width,height) = (300,75)
            self.buttons["help"] = Button((cx-width/2,cy-height/2,cx+width/2,
                                           cy+height/2),lambda:self.help(),
                                           "Help","green","Arial 40 bold")
        for key in self.buttons:
            button = self.buttons[key]
            button.draw(self.canvas)

    def onMousePressed(self, event):
        """Checks if user clicked a button"""
        print "mousepressed"
        (x,y) = (event.x, event.y)
        try:
            for key in self.buttons:
                button = self.buttons[key]
                if (button.isClickInsideBox(x,y)): button.clicked()
        except Exception,e: print str(e)


    def onMouseReleased(self, event):
        """Un-highlights the buttons"""
        for key in self.buttons:
            button = self.buttons[key]
            button.highlighted = False
        self.redrawAll()

    def mouseMotion(self, event): 
        """Overrides the mouse motion binding in any subviews"""
        pass

    def createGame(self):
        """Moves to the next menu when a user clicks the createGame button"""
        self.canvas.delete(ALL)
        self.timerDelay = None
        thread = Thread(target = lambda: self.checkIfSubviewIsDone())
        thread.start()
        self.subview = DefineRulesMenu(self.canvas,self.root)

    def help(self): 
        """Processes button click when a user clicks help"""
        self.isShowingHelp = True
        self.redrawAll()

    def checkIfSubviewIsDone(self):
        """Continually checks if the subview (the DefineRulesMenu) is done, and 
        if so, removes them and re-draws the menu"""
        try:
            if (self.subview.done):
                print "yayyyy!!!"
                self.subview = None
                self.timerDelay = 250
                for key in self.buttons:
                    button = self.buttons[key]
                    button.highlighted = False
                self.initAnimation()
            else:
                thread = Thread(target = lambda: self.checkIfSubviewIsDone())
                thread.start()
        except Exception,e: 
            #print str(e)
            thread = Thread(target = lambda: self.checkIfSubviewIsDone())
            thread.start()

class DefineRulesMenu(object):
    """The next-level menu, where a user is able to drag and drop rules together
    to create his/her own game"""
    def __init__(self, canvas, root):
        """Initializes the menu, including the area for the users to drop rules 
        to."""
        self.width = canvas.winfo_width()
        self.height = canvas.winfo_height()
        self.canvas = canvas
        self.root = root
        self.dragAndDrops = {}
        self.buttons = {}
        self.subview = None
        self.done = False
        self.currentlyDragging = ""
        self.rules = {}
        (vOffset, hOffset, width) = (100,50,700)
        self.rulesBbox = (self.width-width-hOffset,vOffset,self.width-hOffset,
                          vOffset,self.width-hOffset,self.height-vOffset,
                          self.width-width-hOffset,self.height-vOffset)
        (vOffset, width) = (100,200)
        self.optionsBbox = (0,vOffset,width,vOffset,width,self.height-vOffset,
                            0,self.height-vOffset)
        self.initAnimation()

    def initAnimation(self):
        """Binds all events"""
        self.root.bind("<Button>", lambda event: self.onMousePressed(event))
        self.root.bind("<ButtonRelease-1>", 
                        lambda event: self.onMouseReleased(event))
        self.canvas.bind("<Motion>", lambda event: self.mouseMotion(event))
        self.redrawAll()

    def onMousePressed(self, event):
        """Checks if user clicked a button or a dragAndDrop"""
        (x,y) = (event.x, event.y)
        try:
            for key in self.dragAndDrops:
                dragAndDrop = self.dragAndDrops[key]
                if (dragAndDrop.isClickInsideBox(x,y)): 
                    self.currentlyDragging = key
            for key in self.buttons:
                button = self.buttons[key]
                if (button.isClickInsideBox(x,y)): 
                    button.clicked()
        except Exception,e: print str(e)

    def onMouseReleased(self, event):
        """Checks if the user released a dragAndDrop"""
        (x,y) = (event.x,event.y)
        if self.currentlyDragging != "":
            if (self.rulesBbox[0]<x<self.rulesBbox[4] and 
                self.rulesBbox[1]<y<self.rulesBbox[5]):
                self.dragAndDrops[self.currentlyDragging].clicked()
            else: 
                self.dragAndDrops.pop(self.currentlyDragging)
                if self.currentlyDragging in self.rules:
                    self.rules.pop(self.currentlyDragging)
                self.redrawAll()
        self.currentlyDragging = ""
        for key in self.buttons:
            button = self.buttons[key]
            button.highlighted = False
        self.redrawAll()

    def mouseMotion(self, event):
        """If the user is dragging a dragAndDrop, this moves it"""
        (x,y) = (event.x, event.y)
        if (self.currentlyDragging != ""):
            dragAndDrop = self.dragAndDrops[self.currentlyDragging]
            dragAndDrop.draw(self.canvas,x,y)

    def redrawAll(self):
        """Redraws all buttons, boxes, and dragAndDrops"""
        self.drawBackgroundInfo()
        self.drawDragAndDrops()
        self.drawButtons()

    def drawBackgroundInfo(self):
        """Draws the background boxes and text."""
        canvas = self.canvas
        (x0,y0,x1,y1,x2,y2,x3,y3) = self.rulesBbox
        (cx,cy,cornerRad) = ((x2+x0)/2,y0+20,50)
        bbox = (x0,y0,x0+cornerRad,y0,x1-cornerRad,y1,x1,y1,x1,y1+cornerRad,
                x1,y2-cornerRad,x2,y2,x2-cornerRad,y2,x3+cornerRad,y2,x3,y3,
                x3,y3-cornerRad,x3,y0+cornerRad)
        canvas.create_polygon(*bbox, fill="green", smooth=True, outline="black")
        canvas.create_text(cx,cy,text="Rules",font="Arial 20 bold")
        (x0,y0,x1,y1,x2,y2,x3,y3) = self.optionsBbox
        (cx,cy,cornerRad) = ((x2+x0)/2,y0+20,50)
        bbox = (x0,y0,x0+cornerRad,y0,x1-cornerRad,y1,x1,y1,x1,y1+cornerRad,
                x1,y2-cornerRad,x2,y2,x2-cornerRad,y2,x3+cornerRad,y2,x3,y3,
                x3,y3-cornerRad,x3,y0+cornerRad)
        canvas.create_polygon(*bbox, fill="grey", smooth=True, outline="black")
        canvas.create_text(cx,cy,text="Options",font="Arial 20 bold")
        canvas.create_text(483,45,text="Presets:",
                            font="Arial 20 bold")
        (cx,cy) = ((self.optionsBbox[4]+self.rulesBbox[0])/2, self.height-50)
        canvas.create_text(cx,cy,text="Drag and Drop", font="Arial 40 bold")


    def drawButtons(self):
        """Creates and draws all the buttons in this menu"""
        (width,height) = (100,50)
        offset = 20
        if ("clear" not in self.buttons):
            voffset,hoffset = 20,500
            self.buttons["createGame"] = Button((hoffset,
                            self.height-height-voffset,width+hoffset,
                            self.height-voffset),lambda:self.clear(),"Clear",
                            "green")
        if ("heartsPreset" not in self.buttons):
            self.buttons["heartsPreset"] = Button((self.width-width-offset,
                            offset,self.width-offset,height+offset),
                            lambda:self.readInPreset('heartsPreset.txt'),
                            "Hearts","green")
        if ("twentyNinePreset" not in self.buttons):
            voffset,hoffset = 20, 140
            self.buttons["twentyNinePreset"] = Button((self.width-width-hoffset,
                            voffset,self.width-hoffset,height+voffset),         
                            lambda:self.readInPreset('twentyNinePreset.txt'),
                            "29","green")
        if ("loadPreset" not in self.buttons):
            voffset,hoffset = 20, 260
            self.buttons["loadPreset"] = Button((self.width-width-hoffset,
                                voffset,self.width-hoffset,height+voffset),
                                lambda:self.loadPreset(),"Load","green")
        if ("savePreset" not in self.buttons):
            voffset,hoffset = 20, 380
            self.buttons["savePreset"] = Button((self.width-width-hoffset,
                                voffset,self.width-hoffset,height+voffset),
                                lambda:self.savePreset(),"Save","green")
        (width,height) = (200,50)
        if ("back" not in self.buttons):
            self.buttons["back"] = Button((offset,offset,width+offset,
                            height+offset),lambda:self.back(),"Back","green")
        if ("playerNames" not in self.buttons):
            voffset,hoffset = 20, 240
            self.buttons["playerNames"] = Button((hoffset,voffset,width+hoffset,
                                    height+voffset),lambda:self.playerNames(),
                                    "Player Names","green")
        if ("startGame" not in self.buttons):
            self.buttons["startGame"] = Button((self.width-width-offset,
                                self.height-height-offset,self.width-offset,
                                self.height-offset),lambda:self.startGame(),
                                "Start Game","green")
        for key in self.buttons:
            button = self.buttons[key]
            button.draw(self.canvas)

    def drawDragAndDrops(self):
        """Creates and draws all the dragAndDrops on this menu"""
        (width,height) = (150,30)
        self.names = ["Anna","Katie","William","Amal","Varun"]
        if ("omitCards" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*0,25)
            self.omitCardsText = [""]
            if "omitCards" in self.rules: self.rules.pop("omitCards")
            self.dragAndDrops["omitCards"] = DragAndDrop((hOffset,vOffset,
                                    hOffset+width,vOffset+height),
                                    lambda:self.omitCards(),"Omit Cards","grey")
        if ("points" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*1,25)
            self.pointsText = [""]
            if "points" in self.rules: self.rules.pop("points")
            self.dragAndDrops["points"] = DragAndDrop((hOffset,vOffset,
                                        hOffset+width,vOffset+height),
                                        lambda:self.points(),"Points","grey")
        if ("passCards" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*2,25)
            self.passCardsText = ["",""]
            if "passCards" in self.rules: self.rules.pop("passCards")
            self.dragAndDrops["passCards"] = DragAndDrop((hOffset,vOffset,
                                        hOffset+width,vOffset+height),
                                        lambda:self.passCards(),"Pass","grey")
        if ("playerWhoStarts" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*3,25)
            self.playerWhoStartsText = [""]
            if "playerWhoStarts" in self.rules: self.rules.pop("playerWhoStarts")
            self.dragAndDrops["playerWhoStarts"] = DragAndDrop((hOffset,vOffset,
                                            hOffset+width,vOffset+height),
                                            lambda:self.playerWhoStarts(),
                                            "Starting Player","grey")
        if ("suitsLegalityDict" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*4,25)
            self.suitsLegalityDictText = [""]
            if "suitsLegalityDict" in self.rules: 
                self.rules.pop("suitsLegalityDict")
            self.dragAndDrops["suitsLegalityDict"] = DragAndDrop((hOffset,
                                        vOffset,hOffset+width,vOffset+height),
                                        lambda:self.suitsLegalityDict(),
                                        "Illegal Suits","grey")
        if ("winner" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*5,25)
            self.winnerText = [""]
            if "winner" in self.rules: self.rules.pop("winner")
            self.dragAndDrops["winner"] = DragAndDrop((hOffset,vOffset,
                                        hOffset+width,vOffset+height),
                                        lambda:self.winner(),"Winner","grey")
        if ("trump" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*6,25)
            self.trumpText = [""]
            if "trump" in self.rules: self.rules.pop("trump")
            self.dragAndDrops["trump"] = DragAndDrop((hOffset,vOffset,
                                        hOffset+width,vOffset+height),
                                        lambda:self.trump(),"Trump","grey")
        if ("bid" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*7,25)
            self.bidText = ["","","","",""]
            if "bid" in self.rules: self.rules.pop("bid")
            self.dragAndDrops["bid"] = DragAndDrop((hOffset,vOffset,
                                            hOffset+width,vOffset+height),
                                            lambda:self.bid(),"Bid","grey")
        if ("dealOrder" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*8,25)
            self.dealOrderText = ["",""]
            if "dealOrder" in self.rules: self.rules.pop("dealOrder")
            self.dragAndDrops["dealOrder"] = DragAndDrop((hOffset,vOffset,
                                    hOffset+width,vOffset+height),
                                    lambda:self.dealOrder(),"Deal Order","grey")
        if ("valueOrder" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*9,25)
            self.valueOrderText = [""]
            if "valueOrder" in self.rules: self.rules.pop("valueOrder")
            self.dragAndDrops["valueOrder"] = DragAndDrop((hOffset,vOffset,
                                hOffset+width,vOffset+height),
                                lambda:self.valueOrder(),"Card Order","grey")
        if ("isTrumpHidden" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*10,25)
            self.isTrumpHiddenText = ["False"]
            if "isTrumpHidden" in self.rules: self.rules.pop("isTrumpHidden")
            self.dragAndDrops["isTrumpHidden"] = DragAndDrop((hOffset,vOffset,
                                        hOffset+width,vOffset+height),
                                        lambda:self.isTrumpHidden(),
                                        "Trump Hidden?","grey")
        if ("partners" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*11,25)
            self.partnersText = [""]
            if "partners" in self.rules: self.rules.pop("partners")
            self.dragAndDrops["partners"] = DragAndDrop((hOffset,vOffset,
                                    hOffset+width,vOffset+height),
                                    lambda:self.partners(),"Partners","grey")
        if ("numberOfPlayers" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*12,25)
            self.numberOfPlayersText = [""]
            if "numberOfPlayers" in self.rules: self.rules.pop("numberOfPlayers")
            self.dragAndDrops["numberOfPlayers"] = DragAndDrop((hOffset,vOffset,
                                        hOffset+width,vOffset+height),
                                        lambda:self.numberOfPlayers(),
                                        "# of Players","grey")
        if ("cardsPerPlayer" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*13,25)
            self.cardsPerPlayerText = [""]
            if "cardsPerPlayer" in self.rules: self.rules.pop("cardsPerPlayer")
            self.dragAndDrops["cardsPerPlayer"] = DragAndDrop((hOffset,vOffset,
                                            hOffset+width,vOffset+height),
                                            lambda:self.cardsPerPlayer(),
                                            "# of Cards","grey")
        if ("afterRound" not in self.dragAndDrops): 
            (cx,cy) = (self.width/2,self.height/2)
            (vOffset,hOffset) = (150+height*14,25)
            self.afterRoundText = [""]
            if "afterRound" in self.rules: self.rules.pop("afterRound")
            self.dragAndDrops["afterRound"] = DragAndDrop((hOffset,vOffset,
                                        hOffset+width,vOffset+height),
                                        lambda:self.afterRound(),
                                        "After Round","grey")
        for key in self.dragAndDrops:
            dragAndDrop = self.dragAndDrops[key]
            dragAndDrop.draw(self.canvas)

    def savePreset(self):
        """Prompts the user for a name to save the preset by"""
        response = CardGameDialog(self.canvas, "savePreset").result
        if response != None:
            fileName = response[0].lower() + ".txt"
            with open(fileName, 'wt') as doc:
                    preset = ""
                    for key in self.rules:
                        keyText = key + "Text"
                        if preset != "": preset += "\n"
                        preset += keyText + ": "
                        attributes = self.__dict__[keyText]
                        if len(attributes) == 1:
                            preset += attributes[0]
                        else:
                            attributeText = ""
                            for attribute in attributes:
                                if attributeText=="":attributeText += attribute
                                else: attributeText += " | "+ attribute
                            preset += attributeText
                    doc.write(preset)

    def loadPreset(self):
        """Prompts the user for the name of a preset to load"""
        response = CardGameDialog(self.canvas, "loadPreset").result
        if response != None:
            fileName = response[0].lower() + ".txt"
            self.readInPreset(fileName)

    def readInPreset(self,fileName):
        """Reads in a preset txt file and stores the parameters in the rules 
        dictionary"""
        try: 
            with open(fileName,'rt') as doc: preset = doc.read()
        except: 
            error = ("Sorry, there is no preset saved by that filename.  Check"+
                     " your spelling and try again.")
            tkMessageBox.showwarning("Invalid File Name", error)
            return
        attributes = preset.splitlines()
        for attribute in attributes:
            print attribute
            index = attribute.index(":")
            keyText = attribute[:index]
            key = keyText[:-4]
            setting = attribute[index+1:]
            setting = setting.strip()
            if not "|" in setting: #Only one item in list
                self.__dict__[keyText] = [setting]
            else: 
                settingsList = []
                while "|" in setting:
                    settingsList.append(setting[:setting.index("|")].strip())
                    setting = setting[setting.index("|")+1:]
                settingsList.append(setting.strip())
                self.__dict__[keyText] = settingsList
            print key
            if (key in dir(self)):
            # Move corresponding drag and drop
                dragAndDrop = self.dragAndDrops[key]
                (x0,y0,x1,y1,x2,y2,x3,y3) = self.rulesBbox
                cx = random.randint(x0+50,x2-50)
                cy = random.randint(y0+50,y2-50)
                dragAndDrop.draw(self.canvas,cx,cy)
            # Run the corresponding method, to parse text and add to rules
                method = "self.%s(False)" % key
                print key
                eval(method)
            else: 
                error =("Pres et file is corrupted, cannot find %s option"%key)
                tkMessageBox.showwarning("Invalid File", error)

    def playerNames(self):
        """Prompts the user to enter the player names"""
        if "numberOfPlayers" in self.rules: num = self.rules["numberOfPlayers"]
        else: num = 4
        response = CardGameDialog(self.canvas, "playerNames",
                        seedText=self.names[:num], numberOfPlayers=num).result
        if response != None: 
            for index in xrange(len(response)):
                self.names[index] = response[index]

    def passCards(self, showMessage=True):
        """Prompts the user for more info regarding how/where cards will be 
        passed"""
        if showMessage:
            response = CardGameDialog(self.canvas, "pass",
                                        seedText=self.passCardsText).result
            self.passCardsText = ["",""] if response == None else response
        try:
            if self.passCardsText[0] == "" or self.passCardsText[1] == "": 
                self.dragAndDrops.pop("passCards")
                self.redrawAll()
            else:
                cardsToPass = int(self.passCardsText[0])
                directions = self.passCardsText[1].split(",")
                directionsAbbr = []
                for direction in directions:
                    direction = direction.strip()
                    directionsAbbr.append(direction[0].lower())
                self.rules["passCards"] = (cardsToPass, tuple(directionsAbbr))
                print self.rules["passCards"]
        except Exception,e:
                print str(e)
                tkMessageBox.showwarning("Invalid Message",
                            "There was an error processing your instructions. \
                            Please modify them and try again.")

    def numberOfPlayers(self, showMessage=True):
        """Prompts the user for more details regarding the number of players"""
        if showMessage:
            response = CardGameDialog(self.canvas, "numberOfPlayers",
                                    seedText=self.numberOfPlayersText).result
            self.numberOfPlayersText = [""] if response == None else response
        try:
            if self.numberOfPlayersText == [""]: 
                self.dragAndDrops.pop("numberOfPlayers")
                self.redrawAll()
            else:
                numberOfPlayers = int(self.numberOfPlayersText[0])
                if numberOfPlayers < 3 or numberOfPlayers > 5:
                    raise Exception("Sorry, you can only play with between \
                                    three and five players.")
                self.rules["numberOfPlayers"] = numberOfPlayers
                print self.rules["numberOfPlayers"]
        except Exception,e:
                print str(e)
                tkMessageBox.showwarning("Invalid Message",
                            "There was an error processing your instructions. \
                             Please modify them and try again.")

    def cardsPerPlayer(self, showMessage=True):
        """Prompts the user for more details regarding the number of cards per 
        player"""
        if showMessage:
            response = CardGameDialog(self.canvas, "cardsPerPlayer",
                                        seedText=self.cardsPerPlayerText).result
            self.cardsPerPlayerText = [""] if response == None else response
        try:
            if self.cardsPerPlayerText == [""]: 
                self.dragAndDrops.pop("cardsPerPlayer")
                self.redrawAll()
            else:
                cardsPerPlayer = int(self.cardsPerPlayerText[0])
                if "omitCards" in self.rules:omit = len(self.rules["omitCards"])
                else: omit = 0
                if "numberOfPlayers" in self.rules: 
                    players = self.rules["numberOfPlayers"]
                else: players = 4
                if (not cardsPerPlayer <= (52-omit)/players):
                    raise Exception("Sorry, there are not enough cards to \
                                    deal that amount per player.")
                self.rules["cardsPerPlayer"] = cardsPerPlayer
                print self.rules["cardsPerPlayer"]
        except Exception,e:
                print str(e)
                tkMessageBox.showwarning("Invalid Message",
                            "There was an error processing your instructions. \
                             Please modify them and try again.")

    def afterRound(self, showMessage=True):
        """Prompts the user for more details regarding what happens after a 
        round"""
        if showMessage:
            response = CardGameDialog(self.canvas, "afterRound",
                                            seedText=self.afterRoundText).result
            self.afterRoundText = [""] if response == None else response
        try:
            if self.afterRoundText == [""]: 
                self.dragAndDrops.pop("afterRound")
                self.redrawAll()
            else:
                afterRound = int(self.afterRoundText[0])
                self.rules["afterRound"] = afterRound
                print self.rules["afterRound"]
        except Exception,e:
                print str(e)
                tkMessageBox.showwarning("Invalid Message",
                            "There was an error processing your instructions. \
                             Please modify them and try again.")

    def partners(self, showMessage=True):
        """Prompts the user for more details regarding partners"""
        if showMessage:
            response = CardGameDialog(self.canvas, "partners",
                                        seedText=self.partnersText).result
            self.partnersText = [""] if response == None else response
        try:
            if self.partnersText == [""]: 
                self.dragAndDrops.pop("partners")
                self.redrawAll()
            else:
                if "across" in self.partnersText[0]: 
                    self.rules["partners"] = "across"
                print self.rules["partners"]
        except Exception,e:
                print str(e)
                tkMessageBox.showwarning("Invalid Message",
                            "There was an error processing your instructions. \
                             Please modify them and try again.")

    def isTrumpHidden(self, showMessage=True):
        """Prompts the user for more details regarding whether the trump is 
        hidden or not"""
        if showMessage:
            if tkMessageBox.askyesno("Trump Hidden?", "Would you like to hide \
                                    the trump until a player who does not have \
                                    the leading suit asks to reveal it?"):
                self.isTrumpHiddenText = ["True"]
            else:
                self.isTrumpHiddenText = ["False"]
                self.dragAndDrops.pop("isTrumpHidden")
                self.redrawAll()
        isTrumpHiddenText =True if self.isTrumpHiddenText == ["True"] else False
        self.rules["isTrumpHidden"] = isTrumpHiddenText

    def valueOrder(self, showMessage=True):
        """Prompts the user for more details regarding the order of cards"""
        if showMessage:
            response = CardGameDialog(self.canvas, "cardOrder",
                                        seedText=self.valueOrderText).result
            self.valueOrderText = [""] if response == None else response
        try:
            if self.valueOrderText == [""]: 
                self.dragAndDrops.pop("valueOrder")
                self.redrawAll()
            else:
                valueOrder = {}
                cards = self.parseUserCardInput(self.valueOrderText[0])
                print cards
                values = set(range(2,15)) - self.omittedValues()
                values = sorted(list(values))
                assert(len(values) == len(cards))
                for value in cards:
                    value = value[0]
                    valueOrder[value] = values.pop(0)
                self.rules["valueOrder"] = valueOrder
                print self.rules["valueOrder"]
        except Exception,e:
                print str(e)
                tkMessageBox.showwarning("Invalid Message",
                            "There was an error processing your instructions. \
                             Please modify them and try again.")

    def dealOrder(self, showMessage=True):
        """Prompts the user for more details regarding how to deal"""
        if showMessage:
            response = CardGameDialog(self.canvas, "dealOrder",
                                        seedText=self.dealOrderText).result
            self.dealOrderText = ["",""] if response == None else response
        try:
            if self.dealOrderText[0] == "" or self.dealOrderText[1] == "": 
                self.dragAndDrops.pop("dealOrder")
                self.redrawAll()
            else:
                dealOrder = [int(self.dealOrderText[0]),
                             int(self.dealOrderText[1])]
                self.rules["dealOrder"] = dealOrder
                print self.rules["dealOrder"]
        except Exception,e:
                print str(e)
                tkMessageBox.showwarning("Invalid Message",
                            "There was an error processing your instructions. \
                             Please modify them and try again.")

    def omittedValues(self):
        """Returns what card values are completely omitted from the game"""
        if "omitCards" not in self.rules: return set()
        omittedValues = set()
        timesSeen = {}
        for value in xrange(2,15): timesSeen[value] = 0
        for card in self.rules["omitCards"]: 
            value = card[1]
            timesSeen[value] += 1
        for value in timesSeen:
            if timesSeen[value] == 4: omittedValues.add(value)
        return omittedValues


    def playerWhoStarts(self, showMessage=True):
        """Prompts the user for more details regarding who starts"""
        if showMessage:
            response = CardGameDialog(self.canvas, "startingPlayer",
                                    seedText=self.playerWhoStartsText).result
            self.playerWhoStartsText = [""] if response == None else response
        try:
            if self.playerWhoStartsText == [""]: 
                self.dragAndDrops.pop("playerWhoStarts")
                self.redrawAll()
            else: 
                keywords=self.parseUserCardInput(self.playerWhoStartsText[0])[0]
                if "winner" in keywords:self.rules["playerWhoStarts"] = "winner"
                elif "dealer" in keywords:self.rules["playerWhoStarts"]="dealer"
                else:
                    suit = self.convertSuitToInt(keywords[0])
                    value = self.convertValueToInt(keywords[-1])
                    self.rules["playerWhoStarts"] = tuple((suit, value))
                    print self.rules["playerWhoStarts"]
        except Exception,e:
            print str(e)
            tkMessageBox.showwarning("Invalid Message",
                        "There was an error processing your instructions. \
                         Please modify them and try again.")

    def winner(self, showMessage=True):
        """Prompts the user for more details regarding how one wins"""
        if showMessage:
            response = CardGameDialog(self.canvas, "winner",
                                        seedText=self.winnerText).result
            self.winnerText = [""] if response == None else response
        try:
            if self.winnerText == [""]: 
                self.dragAndDrops.pop("winner")
                self.redrawAll()
            else: 
                winnerTypes = ['leastPoints', 'mostPoints', 'points>=Bid', 
                               'points<=Bid', 'points==Bid', 'mostTricks', 
                               'leastTricks', 'tricks==bid', 'tricks>=bid', 
                               'tricks<=bid']
                timesSeen = 0
                for winType in winnerTypes:
                    if winType.lower() in self.winnerText[0].lower():
                        self.rules["winner"] = winType
                        timesSeen += 1
                if timesSeen != 1: raise Exception()
                else: print self.rules["winner"]
        except Exception,e:
            print str(e)
            tkMessageBox.showwarning("Invalid Message",
                        "There was an error processing your instructions. \
                         Please modify them and try again.")

    def trump(self, showMessage=True):
        """Prompts the user for more details regarding trump"""
        if showMessage:
            response = CardGameDialog(self.canvas, "pickTrump",
                                            seedText=self.trumpText).result
            self.trumpText = [""] if response == None else response
        try:
            if self.trumpText == [""]: 
                self.dragAndDrops.pop("trump")
                self.redrawAll()
            else: 
                if "winner" in self.trumpText[0] or "rand" in self.trumpText[0]: 
                    self.rules["trump"] = self.trumpText[0]
                    print self.rules["trump"]
                else: 
                    trump = self.convertSuitToInt(self.trumpText[0])
                    if trump: self.rules["trump"] = trump
                    print self.rules["trump"]
        except Exception,e:
            print str(e)
            tkMessageBox.showwarning("Invalid Message",
                        "There was an error processing your instructions. \
                         Please modify them and try again.")

    def bid(self, showMessage=True):
        """Prompts the user for more details regarding a bid"""
        if showMessage:
            response = CardGameDialog(self.canvas, "pickBid",
                                        seedText=self.bidText).result
            self.bidText = ["","","","",""] if response == None else response
        try:
            for text in self.bidText:
                if text == "": 
                    self.dragAndDrops.pop("bid")
                    self.redrawAll()
                    break
            else:
                (minBid,maxBid,bidType,canPass,canMatch) = self.bidText
                if "before" in canMatch: canMatch = -1
                elif "after" in canMatch: canMatch = 1
                elif "no" in canMatch: canMatch = 0
                elif "every" in canMatch: canMatch = 2
                (minBid,maxBid) = (int(minBid),int(maxBid))
                canPass = True if (canPass.lower()[0] == "y" or 
                                   canPass.lower()[0] == "t") else False
                self.rules["bid"] = (True,minBid,maxBid,bidType,canPass,
                                     "redeal",canMatch)
                print self.rules["bid"]
        except Exception,e:
            print str(e)
            tkMessageBox.showwarning("Invalid Message",
                        "There was an error processing your instructions. \
                         Please modify them and try again.")

    def suitsLegalityDict(self, showMessage=True):
        """Prompts the user for more details regarding what suits are legal to 
        play"""
        if showMessage:
            response = CardGameDialog(self.canvas, "illegalSuits",
                                seedText=self.suitsLegalityDictText).result
            self.suitsLegalityDictText = [""] if response == None else response
        try:
            if self.suitsLegalityDictText == [""]: 
                self.dragAndDrops.pop("suitsLegalityDict")
                self.redrawAll()
            else: 
                suits = self.parseUserCardInput(self.suitsLegalityDictText[0])
                illegalSuits = {}
                for suit in suits:
                    suitNum = self.convertSuitToInt(suit[0])
                    if (suitNum is False): raise Exception()
                    illegalSuits[suitNum] = False
                for num in xrange(0,4):
                    if num not in illegalSuits: illegalSuits[num] = True
                self.rules["suitsLegalityDict"] = illegalSuits
                print self.rules["suitsLegalityDict"]
        except Exception,e:
            print str(e)
            tkMessageBox.showwarning("Invalid Message",
                        "There was an error processing your instructions. \
                         Please modify them and try again.")

    def omitCards(self, showMessage=True):
        """Prompts the user for more details regarding what cards to omit"""
        if showMessage:
            response = CardGameDialog(self.canvas, "omitCards",
                                        seedText=self.omitCardsText).result
            self.omitCardsText = [""] if response == None else response
        try:
            if self.omitCardsText == [""]: 
                self.dragAndDrops.pop("omitCards")
                self.redrawAll()
            else: 
                keywordsList = self.parseUserCardInput(self.omitCardsText[0])
                cardsToOmit = []
                for keywords in keywordsList:
                    suit = self.convertSuitToInt(keywords[0])
                    if suit: keywords.pop(0)
                    if len(keywords) == 0 and suit:
                        # Only suit
                        for value in xrange(2,15): 
                            if (suit): cardsToOmit.append((suit, value))
                            else: 
                                for suitNum in xrange(0,4): 
                                    cardsToOmit.append((suitNum, value))
                    elif "-" in keywords:
                        # Two Values
                        firstValue = self.convertValueToInt(keywords[0])
                        secondValue = self.convertValueToInt(keywords[2])
                        for value in xrange(firstValue,secondValue+1): 
                            if (suit): cardsToOmit.append((suit, value))
                            else: 
                                for suitNum in xrange(0,4): 
                                    cardsToOmit.append((suitNum, value))
                    elif "-" in keywords[0]:
                        # Two Values
                        val = keywords[0][:keywords[0].index("-")]
                        firstValue = self.convertValueToInt(val)
                        val = keywords[0][keywords[0].index("-")+1:]
                        secondValue = self.convertValueToInt(val)
                        print firstValue, secondValue
                        for value in xrange(firstValue,secondValue+1): 
                            if (suit): cardsToOmit.append((suit, value))
                            else: 
                                for suitNum in xrange(0,4): 
                                    cardsToOmit.append((suitNum, value))
                    elif self.convertValueToInt(keywords[0]):
                        # Only one value
                        firstValue = self.convertValueToInt(keywords[0])
                        if (suit): cardsToOmit.append((suit, firstValue))
                        else: 
                            for suit in xrange(0,4): 
                                cardsToOmit.append((suit, firstValue))
                    else: raise Exception("Invalid suit/value")
                self.rules["omitCards"] = cardsToOmit
                print self.rules["omitCards"]
        except Exception,e:
            print str(e)
            tkMessageBox.showwarning("Invalid Message",
                        "There was an error processing your instructions. \
                         Please modify them and try again.")

    def points(self, showMessage=True):
        """Prompts the user for details regarding which cards have points"""
        if showMessage:
            response = CardGameDialog(self.canvas, "points",
                                        seedText=self.pointsText).result
            self.pointsText = [""] if response == None else response
        try:
            if self.pointsText == [""]: 
                self.dragAndDrops.pop("points")
                self.redrawAll()
            else: 
                keywordsList = self.parseUserCardInput(self.pointsText[0])
                points = {}
                for keywords in keywordsList:
                    suit = self.convertSuitToInt(keywords[0])
                    point = int(keywords.pop(-1))
                    if suit: keywords.pop(0)
                    if len(keywords) == 0 and suit:
                        # Only suit
                        for value in xrange(2,15): 
                            if (suit): points["(%d, %d)" % (suit, value)]=point
                            else: 
                                for suitNum in xrange(0,4): 
                                    points["(%d, %d)" % (suitNum, value)] =point
                    elif "-" in keywords:
                        # Two Values
                        firstValue = self.convertValueToInt(keywords[0])
                        secondValue = self.convertValueToInt(keywords[2])
                        for value in xrange(firstValue,secondValue+1): 
                            if (suit): points["(%d, %d)" % (suit, value)] =point
                            else: 
                                for suitNum in xrange(0,4): 
                                    points["(%d, %d)" % (suitNum, value)] =point
                    elif "-" in keywords[0]:
                        # Two Values
                        val = keywords[0][:keywords[0].index("-")]
                        firstValue = self.convertValueToInt(val)
                        val = keywords[0][keywords[0].index("-")+1:]
                        secondValue = self.convertValueToInt(val)
                        print firstValue, secondValue
                        for value in xrange(firstValue,secondValue+1): 
                            if (suit): points["(%d, %d)" % (suit, value)] =point
                            else: 
                                for suitNum in xrange(0,4): 
                                    points["(%d, %d)" % (suitNum, value)] =point
                    elif self.convertValueToInt(keywords[0]):
                        # Only one value
                        value = self.convertValueToInt(keywords[0])
                        if (suit): points["(%d, %d)" % (suit, value)] = point
                        else: 
                            for suitNum in xrange(0,4): 
                                points["(%d, %d)" % (suitNum, value)] = point
                    else: raise Exception("Could not understand message")
                self.rules["points"] = points
                print self.rules["points"]
        except Exception,e:
            print str(e)
            tkMessageBox.showwarning("Invalid Message",
                        "There was an error processing your instructions. \
                         Please modify them and try again.")

    def convertSuitToInt(self, suit):
        """Converts suit text to an integer"""
        if "diamond" in suit: return 0
        elif "club" in suit: return 1
        elif "heart" in suit: return 2
        elif "spade" in suit: return 3
        else: 
            return False

    def convertValueToInt(self, value):
        """Converts a value string to an integer"""
        valueList = ["2","3","4","5","6","7","8","9","10","j","q","k","a"]
        if value.lower()in valueList:
            return valueList.index(value.lower())+2
        else: return False

    def parseUserCardInput(self, text):
        """Takes in user input from omitCards, points, etc. options and turns them into lists"""
        text = text.strip()
        if text == None or text == "": return []
        keywords = text.split(",")
        finalList = []
        for phrase in keywords:
            phrase = phrase.strip()
            finalList.append(phrase.split(" "))
        return finalList

    def startGame(self):
        """Starts the game when the user clicks the startGame button"""
        thread = Thread(target = lambda: self.checkIfSubviewIsDone())
        thread.start()
        self.subview = CardGame(self.canvas,self.root,self.rules,self.names)

    def clear(self):
        """Clears the rules when the user clicks the clear button"""
        self.dragAndDrops = {}
        print self.rules

    def back(self):
        """Goes back to menu when the user clicks back"""
        self.canvas.delete(ALL)
        self.buttons = self.dragAndDrops = {}
        self.done = True

    def checkIfSubviewIsDone(self):
        """Continually checks if the subview (the DefineRulesMenu) is done, and 
        if so, removes them and re-draws the menu"""
        try:
            if (self.subview.done):
                self.subview = None
                self.done = True
            else:
                thread = Thread(target = lambda: self.checkIfSubviewIsDone())
                thread.start()
        except Exception,e: 
            #print str(e)
            thread = Thread(target = lambda: self.checkIfSubviewIsDone())
            thread.start()



class CardGame(object):
    """The class that displays and coordinates the actual card game play"""
    def __init__(self, canvas, root, rulesDict, playerNames):
        """Initializes the class"""
        self.rules = Rules(**rulesDict)
        print self.rules
        self.rules.updateGamePhase()
        self.width = canvas.winfo_width()
        self.height = canvas.winfo_height()
        self.playerNames = playerNames
        self.trick = []
        self.buttons = dict()
        self.createPlayers()
        self.createDeck()
        self.canvas = canvas
        self.root = root
        self.initAnimation()

    def eventHandler(self, event):
        """Handles all mouse events"""
        self.rules.updateGamePhase()
        if event.type == '4': # ButtonPress
            self.onMousePressed(event)
        elif event.type == '5': # ButtonRelease
            self.onMouseReleased(event)
        elif event.type == '6': # MouseMotion
            self.mouseMotion(event)

    def createDeck(self):
        """Creates the 52 card deck, omitting cards specified by the user"""
        deck = []
        for suit in xrange(4):
            for value in xrange(2,15):
                if (suit,value) not in self.rules.omitCards:
                    card = Card(suit,value,self.rules.valueOrder)
                    if repr(card) in self.rules.points: 
                        card.points = self.rules.points[repr(card)]
                        print card.points
                    deck.append(card)
        self.deck = deck

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.deck)

    def createPlayers(self):
        """Creates the players"""
        players = []
        for num in xrange(self.rules.numberOfPlayers):
            players.append(Player(self.playerNames[num], len(players)))
        self.players = players

    def deal(self):
        """Deals the cards according to the user-specified parameters"""
        while (self.players[0].numberOfCards() != 
            sum(self.rules.dealOrder[:self.rules.timesCardHaveBeenDealt+1]) or
            not self.playersHaveEqualCards()):
        playerI = len(self.deck) % self.rules.numberOfPlayers
            self.players[playerI].getsDealtCard(self.deck.pop(0))
        self.rules.timesCardHaveBeenDealt += 1
        for player in self.players: print player

    def playersHaveEqualCards(self):
        """Checks whether players have equal cards or not"""
        numOfCards = self.players[0].numberOfCards()
        if numOfCards == 0: return False
        for player in self.players:
            if numOfCards != player.numberOfCards(): return False
        return True

    def initAnimation(self):
        """Called every time the game starts/restarts"""
        self.timerDelay = 10
        scaleFactor = sf = 3
        if self.rules.cardsPerPlayer > 13: sf = 4
        self.imageDict = {0:PhotoImage(file='diamonds.gif').subsample(sf,sf),
                          1:PhotoImage(file='clubs.gif').subsample(sf,sf),
                          2:PhotoImage(file='hearts.gif').subsample(sf,sf),
                          3:PhotoImage(file='spades.gif').subsample(sf,sf)}
        self.hoverCard = None
        self.isDisplayingMessage = True
        if (type(self.rules.isTrumpHidden) == bool): 
            self.rules.isTrumpHidden = True
        self.rules.lastPlayedCard = None
        self.rules.gamePhase = 0
        self.rules.haveCardsPassed = False
        self.rules.timesCardHaveBeenDealt = 0
        self.rules.haveBidsHappened = False
        print repr(self.rules.trumpPick), repr(self.rules.trump)
        if (self.rules.trumpPick != None and "random" in self.rules.trumpPick): 
            self.rules.trump = random.randint(0,3)
        elif (self.rules.trumpPick != None): self.rules.trump = None
        print repr(self.rules.trumpPick), repr(self.rules.trump)
        self.shuffle()
        self.deal()
        print "yay"
        for player in self.players:
            player.partnerPoints = 0
            player.bid = False
        self.buttons = {}
        # Each element of the callback queue will be a list of the form:
        # [interval, function, timesToRepeat=1, endFunction, timeSinceLastCall=0]
        # EX: [100, self.animateMove,10,self.isTrickOver(),50]
        self.callbackQueue = []
        self.playerWhoseTurnItIs = -1
        self.root.bind("<Button>", lambda event: self.eventHandler(event))
        self.root.bind("<ButtonRelease-1>",
                        lambda event: self.eventHandler(event))
        self.canvas.bind("<Motion>", lambda event: self.eventHandler(event))
        self.onTimerFired()
        self.rules.updateGamePhase()
        self.nextPlayer()

    def mouseMotion(self, event):
        """Checks whether the user is hovering over a card"""
        if not self.isDisplayingMessage:
            (x,y) = (event.x, event.y)
            try:
                if (self.players[self.playerWhoseTurnItIs].hand[0].bbox != None):
                    if (self.isXYWithinCard(x,y) is not False): 
                        self.hoverCard = self.isXYWithinCard(x,y)
                        self.redrawAll()
                    elif type(self.hoverCard) == int:
                        self.hoverCard = None
                        self.redrawAll()
            except Exception,e: print str(e)

    def onMousePressed(self, event):
        """Checks if user clicked a card or button"""
        (x,y) = (event.x, event.y)
        if (self.isXYWithinCard(x,y) is not False):
            cardI = self.isXYWithinCard(x,y)
            playerI = self.playerWhoseTurnItIs
            if  self.rules.gamePhase == 0:
                card = self.players[playerI].hand[cardI]
                if card.aboutToPass:
                    card.aboutToPass = not card.aboutToPass
                    self.players[playerI].passCardIndices.remove(cardI)
                elif len(self.players[playerI].passCardIndices) < 
                     self.rules.passCards[0]:
                    card.aboutToPass = not card.aboutToPass
                    self.players[playerI].passCardIndices.append(cardI)
            elif self.rules.gamePhase == 1:
                card = self.players[playerI].hand[cardI]
                if self.rules.isCardLegal(card,self.trick,self.players[playerI]):
                    self.trick.append(self.players[playerI].playsCardAtIndex(cardI))
                    self.lastPlayedCard = card
                    (x0,y0) = (card.bbox[0],card.bbox[1])
                    interval=10
                    repeat=50
                    function = lambda timesToRepeat: self.moveCard(self.lastPlayedCard, timesToRepeat)
                    endFunction=lambda: self.playerPlayed(self.lastPlayedCard)
                    self.callbackQueue.append([interval,function,repeat,endFunction,0])
        try:
            for key in self.buttons:
                button = self.buttons[key]
                if (button.isClickInsideBox(x,y)): button.clicked()
        except Exception,e: print str(e)


    def onMouseReleased(self, event):
        """Unhighlights the buttons"""
        (x,y) = (event.x, event.y)
        for key in self.buttons:
            button = self.buttons[key]
            button.highlighted = False
        

    def passButtonClicked(self):
        """Passes cards if the user has designate enough"""
        currentPlayer = self.players[self.playerWhoseTurnItIs]
        if (len(currentPlayer.passCardIndices) == self.rules.passCards[0]):
            playerToRecieve = self.rules.whoToPassTo(self.playerWhoseTurnItIs)
            playerToRecieve = self.players[playerToRecieve]
            self.deleteCards(self.playerWhoseTurnItIs)
            playerToRecieve.recievesCards(currentPlayer.passCards())
            for player in self.players:
                if player.recievedCards == []: 
                    self.nextPlayer()
                    return
            for player in self.players:
                player.addCardsToHand()
            self.rules.haveCardsPassed = True
            self.rules.updateGamePhase()
            self.startGame()       

    def isBidOver(self):
        """Determines whether the bid is over or not"""
        number = 0
        print "isBidOver"
        for player in self.players:
            if type(player.bid) == int: number += 1
            if not (type(player.bid) == int or player.bid == None):
                return False
        print "number", number
        if (self.rules.bid[3] == "oneByOne" and (number == len(self.players) or 
            self.rules.bid[4] == True)): 
            self.rules.haveBidsHappened = True
            return True
        if (number == 1 and (self.rules.bid[3] == "round" or 
            self.rules.bid[3] == "faceOff")): 
            print "hi"
            self.rules.haveBidsHappened = True
            print "bye"
            return True
        if (number == 0):
            if (self.rules.bid[5] == "redeal"):return self.rules.numberOfPlayers
            elif (self.rules.bid[5] == "round"): return False

    def nextPlayer(self):
        """Moves on to the next player"""
        print "nextPlayer"
        self.deleteCards(self.playerWhoseTurnItIs)
        if self.playerWhoseTurnItIs == -1 and self.rules.gamePhase == 1: 
            self.startGame()
        elif self.playerWhoseTurnItIs == -1:
            self.playerWhoseTurnItIs = (self.rules.round+1) % self.rules.numberOfPlayers
            if self.rules.bid[0]:
                self.playerWhoStartsBid = self.playerWhoseTurnItIs
                self.playerWhoIsFacingOff = (self.playerWhoseTurnItIs+1)%self.rules.numberOfPlayers
                self.previousBid = self.rules.bid[1]-1
            name = self.players[self.playerWhoseTurnItIs].name
            self.displayPassComputerMessage(name)
        else:
            self.playerWhoseTurnItIs += 1
            self.playerWhoseTurnItIs %= self.rules.numberOfPlayers
            name = self.players[self.playerWhoseTurnItIs].name
            self.displayPassComputerMessage(name)
        self.rules.updateGamePhase()
        self.redrawAll()
        self.preGame()

    def preGame(self):
        """Coordinates the bidding process, if applicable"""
        if (self.rules.gamePhase == 0):
            if (self.rules.bid[0] == True and not self.isBidOver() and 
                not self.rules.trumpPick == "bid"):
                self.minBid = self.previousBid + 1
                if (self.playerWhoseTurnItIs == self.playerWhoStartsBid and 
                    self.rules.bid[6] == -1): 
                    self.minBid -= 1
                elif (self.playerWhoseTurnItIs != self.playerWhoStartsBid and 
                    self.rules.bid[6] == 1):
                    self.minBid -= 1
                elif self.rules.bid[6] == 2: self.minBid = self.rules.bid[1]
                bid = None
                if not self.rules.bid[4]:
                    while bid == None:
                        bid = CardGameDialog(self.canvas,"bid",
                            (self.minBid,self.rules.bid[2]),
                            self.rules.bid[4]).result
                        if bid == None: 
                            tkMessageBox.showwarning("Cannot Pass",
                                                    "You cannot pass.")
                else: 
                    bid = CardGameDialog(self.canvas,"bid",
                                        (self.minBid,self.rules.bid[2]),
                                        self.rules.bid[4]).result
                if bid == None:
                    self.players[self.playerWhoseTurnItIs].bid = bid
                else: 
                    self.players[self.playerWhoseTurnItIs].bid = int(bid[0])
                    self.previousBid = int(bid[0])
                if not self.isBidOver():
                    self.nextPlayerInBid()
                else:
                    if type(self.isBidOver()) == int: 
                        tkMessageBox.showwarning("Redeal!","Since every \
                                        player passed, there will be a redeal.")
                        self.redeal()
                    else: self.startGame()

    def whoHasStartCard(self):
        """Detemrines which palyer has the starting card"""
        startCard = self.rules.playerWhoStarts
        for index in xrange(len(self.players)):
            player = self.players[index]
            for card in player.hand:
                if card == startCard:
                    return index

    def displayPassComputerMessage(self, name):
        """Tells the user to pass the computer to the next player"""
        self.isDisplayingMessage = True
        tkMessageBox.showwarning("Next Player","Pass the computer to %s." %name)
        self.isDisplayingMessage = False

    def startGame(self):
        """Start gameplay, called after passing/bidding are done"""
        print "startGame"
        self.deleteCards(self.playerWhoseTurnItIs)
        if type(self.rules.playerWhoStarts) == tuple:
            playerWithCard = self.whoHasStartCard()
            if playerWithCard != None:
                self.playerWhoseTurnItIs = playerWithCard
            else: 
                print "No player has the starting card."
                self.playerWhoseTurnItIs=(self.rules.round+1)%self.rules.numberOfPlayers
        elif self.rules.playerWhoStarts == "winner":
            self.playerWhoseTurnItIs = self.maxBidPlayer()
        else:
            self.playerWhoseTurnItIs=(self.rules.round+1)%self.rules.numberOfPlayers
        name = self.players[self.playerWhoseTurnItIs].name
        self.displayPassComputerMessage(name)
        self.deal()
        self.redrawAll()
        if (self.rules.bid[0] == True and self.rules.haveBidsHappened and 
            self.rules.trumpPick == "winner" and self.rules.trump == None):
            trump = CardGameDialog(self.canvas,"trump").result[0][0].lower()
            self.rules.trump = ["d","c","h","s","n"].index(trump)
            print self.rules.trump

    def maxBidPlayer(self):
        """Detemrines which player bid the most"""
        (maxBid, maxBidPlayer) = (None, None)
        for playerI in xrange(len(self.players)):
            player = self.players[playerI]
            if (player.bid > maxBid):
                maxBid = player.bid
                self.maxBidPlayer = playerI
        if self.rules.partners == "across":
            partnerI = (self.maxBidPlayer + self.rules.numberOfPlayers/2) % self.rules.numberOfPlayers
            self.players[partnerI].bid = self.players[self.maxBidPlayer].bid
        return self.maxBidPlayer


    def nextPlayerInBid(self):
        """Detemrines which user is next in the bidding process"""
        print self.playerWhoseTurnItIs
        self.deleteCards(self.playerWhoseTurnItIs)
        if self.rules.bid[3] == "round" or self.rules.bid[3] == "oneByOne":
            self.playerWhoseTurnItIs += 1
        elif self.rules.bid[3] == "faceOff":
            if self.players[self.playerWhoseTurnItIs].bid == None:
                if self.playerWhoseTurnItIs == self.playerWhoStartsBid: 
                    if (self.players[self.playerWhoIsFacingOff].bid==False):
                        self.playerWhoStartsBid = self.playerWhoIsFacingOff
                        self.playerWhoseTurnItIs = self.playerWhoStartsBid
                        self.playerWhoIsFacingOff = self.playerWhoseTurnItIs+1

                    else:
                        self.playerWhoStartsBid = self.playerWhoIsFacingOff
                        self.playerWhoseTurnItIs = self.playerWhoStartsBid + 1
                        self.playerWhoIsFacingOff = self.playerWhoseTurnItIs
                elif self.playerWhoseTurnItIs == self.playerWhoIsFacingOff:
                    self.playerWhoseTurnItIs += 1
                    self.playerWhoIsFacingOff = self.playerWhoseTurnItIs
            else:
                if self.playerWhoseTurnItIs == self.playerWhoStartsBid:
                    self.playerWhoseTurnItIs = self.playerWhoIsFacingOff
                else:
                    self.playerWhoseTurnItIs = self.playerWhoStartsBid
        self.playerWhoseTurnItIs %= self.rules.numberOfPlayers
        self.playerWhoIsFacingOff %= self.rules.numberOfPlayers
        self.playerWhoStartsBid %= self.rules.numberOfPlayers
        name = self.players[self.playerWhoseTurnItIs].name
        self.isDisplayingMessage = True
        tkMessageBox.showwarning("Next Player","Pass the computer to %s." %name)
        self.isDisplayingMessage = False
        self.rules.updateGamePhase()
        self.redrawAll()
        self.preGame()

    def playerPlayed(self, card):
        """Called once a player plays a card"""
        self.hoverCard = None
        print self.trick
        if len(self.trick) == self.rules.numberOfPlayers: 
            self.endTrick()
        else:
            print card
            self.nextPlayer()

    def moveCard(self,card,steps):
        """Animates the motion of a card to the center"""
        (cxf,cyf) = self.cardCenters()[len(self.trick)-1]
        (x0,y0) = (card.bbox[0],card.bbox[1])
        (xf,yf) = (cxf-card.width/2,cyf-card.height/2)
        (dx,dy) = ((xf-x0)/float(steps),(yf-y0)/float(steps))
        (dx,dy) = (int(round(dx)),int(round(dy)))
        (x,y) = (x0+dx,y0+dy)
        card.adjustPosition(x,y)
        card.drawCard(self.canvas,self.imageDict)

    def onTimerFired(self):
        """If something is in the callback queue, calls that every 
        specified-interval"""
        if not self.isDisplayingMessage: self.redrawAll()
        completedCallbackIndices = []
        for index in xrange(len(self.callbackQueue)):
            callback = self.callbackQueue[index]
            (interval,function,timesToRepeat,endFunction,timeSinceLastCall)=callback
            timeSinceLastCall += self.timerDelay
            if timeSinceLastCall >= interval:
                function(timesToRepeat)
                timeSinceLastCall = 0
                timesToRepeat -= 1
                if timesToRepeat > 0:
                    (callback[2],callback[4])=(timesToRepeat,timeSinceLastCall)
                else: 
                    print "motionEnded"
                    endFunction()
                    completedCallbackIndices.append(index)
        for index in xrange(len(completedCallbackIndices)):
            self.callbackQueue.pop(completedCallbackIndices[index]-index)
        if self.timerDelay:self.canvas.after(self.timerDelay, self.onTimerFired) 

        def moveTrick(self,playerI,steps):
        """Animates the motion of a trick to the palyer who won it"""
        minx0 = maxx0 = self.trick[0].bbox[0]
        miny0 = maxy0 = self.trick[0].bbox[1]
        for card in self.trick:
            if card.bbox[0] < minx0: minx0 = card.bbox[0]
            if card.bbox[0] > maxx0: maxx0 = card.bbox[0]
            if card.bbox[1] < miny0: miny0 = card.bbox[1]
            if card.bbox[1] > maxy0: maxy0 = card.bbox[1]
        (cx,cy) = self.playerLocation(playerI)
        if cx == self.width/2: xi = cx
        elif minx0 > cx: xi = maxx0
        elif minx0 < cx: xi = minx0
        if cy == self.height/2: yi = cy
        elif miny0 > cy: yi = maxy0
        elif miny0 < cy: yi = miny0
        offset = 400
        if cx < self.width/2: xf = -offset
        elif cx == self.width/2: xf = self.width/2
        elif cx > self.width/2: xf = self.width+offset
        if cy < self.height/2: yf = -offset
        elif cy == self.height/2: yf = self.height/2
        elif cy > self.height/2: yf = self.height+offset
        (dx,dy) = ((xf-xi)/float(steps),(yf-yi)/float(steps))
        (dx,dy) = (int(round(dx)),int(round(dy)))
        for card in self.trick:
            (x0,y0) = (card.bbox[0],card.bbox[1])
            (x,y) = (x0+dx,y0+dy)
            card.adjustPosition(x,y)
            card.drawCard(self.canvas,self.imageDict)

    def endTrick(self):
        """Called once a trick ends"""
        playerWhoWinsTrick = self.rules.whoGetsTrick(self.trick)
        interval=10
        repeat=50
        function = lambda timesToRepeat: self.moveTrick(playerWhoWinsTrick, timesToRepeat)
        endFunction = lambda: self.trickEnded(playerWhoWinsTrick)
        self.callbackQueue.append([interval,function,repeat,endFunction,0])

    def trickEnded(self, playerWhoWinsTrick):
        """Called once the end trick animation is finished"""
        self.players[playerWhoWinsTrick].tricks.append(self.trick)
        self.trick = []
        self.deleteCards(self.playerWhoseTurnItIs)
        self.playerWhoseTurnItIs = playerWhoWinsTrick
        name = self.players[self.playerWhoseTurnItIs].name
        self.displayPassComputerMessage(name)
        self.updatePoints()
        if len(self.players[0].hand) == 0: self.gameOver()

    def updatePoints(self):
        """If a user has a partner, updates the partner's points"""
        if self.rules.partners == "across":
            playerI = self.playerWhoseTurnItIs
            partnerI = (self.playerWhoseTurnItIs+self.rules.numberOfPlayers/2)%self.rules.numberOfPlayers
            self.players[playerI].partnerPoints=self.players[partnerI].pointsInTricks()
            self.players[partnerI].partnerPoints=self.players[playerI].pointsInTricks()

    def endGameMessage(self):
        """Creates the message to display once the game ends"""
        message = "Game Summary:"
        if "bid" in self.rules.winner.lower():
            message += "\nBids:"
            if (self.rules.bid[3] == "oneByOne"):
                for player in self.players:
                    message += "\n%s: %d" %(player.name,player.bid)
            elif (self.rules.bid[3] == "round" or self.rules.bid[3]=="faceOff"):
                if self.rules.partners == "across":
                    for playerI in xrange(len(self.players)):
                        player = self.players[playerI]
                        partner = self.players[(playerI+self.rules.numberOfPlayers/2)%self.rules.numberOfPlayers]
                        if type(player.bid) == int:
                            message += "\n%s-%s: %d" %(player.name,partner.name,player.bid)
                            break
                else: message += "\n%s: %d" %(player.name,player.bid)
        if "points" in self.rules.winner.lower():
            message += "\nPoints:"
            if self.rules.partners == "across":
                for playerI in xrange(self.rules.numberOfPlayers/2):
                    player = self.players[playerI]
                    partner = self.players[(playerI + self.rules.numberOfPlayers/2)%self.rules.numberOfPlayers]
                    message += "\n%s-%s: %d" %(player.name,partner.name,player.points())
            else:
                for player in self.players:
                    message += "\n%s: %d" %(player.name,player.points())
        if "tricks" in self.rules.winner.lower():
            message += "\nTricks:"
            if self.rules.partners == "across":
                for playerI in xrange(self.rules.numberOfPlayers/2):
                    player = self.players[playerI]
                    partner = self.players[(playerI + self.rules.numberOfPlayers/2)%self.rules.numberOfPlayers]
                    message += "\n%s-%s: %d" %(player.name,partner.name,len(player.tricks)+len(partner.tricks))
            else:
                for player in self.players:
                    message += "\n%s: %d" %(player.name,len(player.tricks))
        winners = self.determineWinners()
        message += "\nWinner: " 
        if len(winners) > 0:
            for name in winners: message += "%s, " % name
            message = message [:-2] # remove ending comma space
        else: meaasge += "None"
        return message

    def determineWinners(self):
       """Determines the winners of the game"""
        winners = []
        if self.rules.winner == "leastPoints":
            minPoints = sys.maxint
            for player in self.players:
                if player.points() < minPoints:
                    minPoints = player.points()
                    winners = [player.name]
                elif player.points() == minPoints:
                    winners.append(player.name)
        elif self.rules.winner == "mostPoints":
            maxPoints = -1
            for player in self.players:
                if player.points() > maxPoints:
                    maxPoints = player.points()
                    winners = [player.name]
                elif player.points() == maxPoints:
                    winners.append(player.name)  
        elif self.rules.winner == "points>=Bid":
            for player in self.players:
                bid = player.bid
                if bid != None and player.points() >= bid:
                    winners.append(player.name)
        elif self.rules.winner == "points<=Bid":
            for player in self.players:
                bid = player.bid
                if bid != None and player.points() <= bid:
                    winners.append(player.name)
        elif self.rules.winner == "points==Bid":
            for player in self.players:
                bid = player.bid
                if bid != None and player.points() == bid:
                    winners.append(player.name)
        elif self.rules.winner == "mostTricks":
            maxTricks = -1
            for player in self.players:
                if len(player.tricks) > maxTricks:
                    maxTricks = len(player.tricks)
                    winners = [player.name]
                elif len(player.tricks) == maxTricks:
                    winners.append(player.name)
        elif self.rules.winner == "leastTricks":
            minTricks = sys.maxint
            for player in self.players:
                if len(player.tricks) < minTricks:
                    minTricks = len(player.tricks)
                    winners = [player.name]
                elif len(player.tricks) == minTricks:
                    winners.append(player.name)
        elif self.rules.winner == "tricks==bid":
            for player in self.players:
                bid = player.bid
                if bid != None and len(player.tricks) == bid:
                    winners.append(player.name)
        elif self.rules.winner == "tricks>=bid":
            for player in self.players:
                bid = player.bid
                if bid != None and len(player.tricks) >= bid:
                    winners.append(player.name)
        elif self.rules.winner == "tricks<=bid":
            for player in self.players:
                bid = player.bid
                if bid != None and len(player.tricks) <= bid:
                    winners.append(player.name)
        return winners

    def gameOver(self):
        """Called once the game is over, displays a summary of the game"""
        self.rules.newGame()
        message = self.endGameMessage()
        tkMessageBox.showwarning("Game Over",message)
        self.redeal()

    def redeal(self):
        """Redealsthe cards, ussually to starts a new round"""
        # Return all cards to the deck
        for player in self.players:
            for trick in player.tricks:
                for index in xrange(len(trick)):
                    card = trick.pop()
                    card.resetCard()
                    self.deck.append(card)
            for index in xrange(len(player.hand)):
                card = player.hand.pop()
                card.resetCard()
                self.deck.append(card)
            for index in xrange(len(player.recievedCards)):
                card = player.recievedCards.pop()
                card.resetCard()
                self.deck.append(card)
            for index in xrange(len(self.trick)):
                card = self.trick.pop()
                card.resetCard()
                self.deck.append(card)
            player.resetPlayer()
        print self.deck
        self.initAnimation()

    def isXYWithinCard(self,x,y):
        """Determines whetehr a user's click/hover is inside a card"""
        hand = self.players[self.playerWhoseTurnItIs].hand
        for index in xrange(len(hand)):
            card = hand[index]
            if card.bbox == None: return False
            if card.isXYInsideCard(x,y): 
                return index
        return False
        
    def redrawAll(self):
        """Redraws the canvas after every event, if it is not animating the 
        motion of cards"""
        if len(self.callbackQueue) == 0 and not self.isDisplayingMessage:
            #print "willRedraw"
            self.canvas.delete(ALL)
            self.drawCards(self.playerWhoseTurnItIs)
            self.drawOtherPlayers()
            self.drawTrick()
            if (type(self.rules.trump) == int): self.drawTrump()
            self.drawButtons()

    def drawButtons(self):
        """Creates and draws the buttons in this view"""
        if ("menu" not in self.buttons):
            (width,height) = (200,50)
            offset = 20
            self.buttons["menu"] = Button((offset,offset,width+offset,
                                height+offset),lambda:self.menu(),"Menu","green")
        height = self.cardHeight
        if self.rules.gamePhase == 0:
            if (self.rules.passCards[0] != 0 and "pass" not in self.buttons): 
                self.buttons["pass"] = Button((75,self.height-height-75,200,
                                        self.height-height-25),
                                        lambda:self.passButtonClicked(),
                                        "Pass Cards","green")
        elif self.rules.gamePhase == 1:
            if ("pass" in self.buttons): self.buttons.pop("pass")
            if (self.rules.isTrumpHidden == True):
                self.buttons["revealTrump"] = Button((self.width-230,
                                self.height-height-80,self.width-50,
                                self.height-height-10),lambda:self.revealTrump(),
                                "Reveal Trump","green")
            else:
                if("revealTrump" in self.buttons):self.buttons.pop("revealTrump")
        for key in self.buttons:
            self.buttons[key].draw(self.canvas)

    def menu(self):
        """Processes when the suer clicks the button to return to the menu"""
        confirmation = tkMessageBox.askyesno("Are you sure?", "Are you sure \
            you would like to return to menu?  The current game will quit.")
        if confirmation:
            self.canvas.delete(ALL)
            self.timerDelay = None
            self.done = True

    def revealTrump(self):
        """Processes when the user clicks the revealTrump button"""
        if (len(self.trick) > 0 and 
            self.trick[0].suit not 
            in self.players[self.playerWhoseTurnItIs].suitsInHand()):
            self.rules.isTrumpHidden = False

    def drawCards(self,playerNum):
        """Draws the hand of the player whose turn it is, and the player's info"""
        if self.players[playerNum].numberOfCards() > 0:
            tempCard = self.players[playerNum].hand[0]
            if tempCard.bbox == None:
                width = self.width/self.players[playerNum].numberOfCards()
                height = Card.heightFromWidth(width)
                (width, height) = (min(tempCard.maxWidth,width),
                                   min(tempCard.maxHeight,height))
                self.cardHeight = height
            else: (width,height) = (tempCard.width,tempCard.height)
            xOffset=(self.width-self.players[playerNum].numberOfCards()*width)/2
            for index in xrange(len(self.players[playerNum].hand)):
                (x0,y0) = (xOffset+index*width,self.height-height)
                card = self.players[playerNum].hand[index]
                if (card.bbox == None): card.setDimensions(x0,y0,width)
                else: card.adjustPosition(x0,y0)
                card.drawCard(self.canvas,self.imageDict)
            if type(self.hoverCard) == int: 
                card = self.players[playerNum].hand[self.hoverCard]
                card.drawCard(self.canvas,self.imageDict, True)
            text = self.players[playerNum].name
            if (self.rules.bid[0]): 
                bid = "0" if not self.players[playerNum].bid else str(self.players[playerNum].bid)
                text += "\nBid: " + bid
            if (len(self.rules.points) > 0): text += "\nPoints: " + str(self.players[playerNum].points())
            text += "\nTricks: " + str(len(self.players[playerNum].tricks))
            (cx,cy) = self.playerLocation(playerNum)
            self.canvas.create_text(cx,cy,text=text,font="Arial 20 bold")

    def deleteCards(self, playerI):
        """Deletes a palyer's cards before moving to the next one"""
        for card in self.players[playerI].hand:
            tag=str(card) + str(card.ID)
            self.canvas.delete(tag)

    def drawTrick(self):
        """Draws a trick in the middle of the screen"""
        for card in self.trick:
            card.drawCard(self.canvas, self.imageDict)

    def drawOtherPlayers(self):
        """Draws the names and info of the other players"""
        for playerI in xrange(self.rules.numberOfPlayers):
            if playerI != self.playerWhoseTurnItIs: 
                (cx,cy) = self.playerLocation(playerI)
            else: continue
            text = self.players[playerI].name
            if (self.rules.bid[0]): 
                bid = "0" if not self.players[playerI].bid else str(self.players[playerI].bid)
                text += "\nBid: " + bid
            if (len(self.rules.points) > 0): text += "\nPoints: " + str(self.players[playerI].points())
            text += "\nTricks: " + str(len(self.players[playerI].tricks))
            self.canvas.create_text(cx,cy,text=text,font="Arial 20 bold")

    def playerLocation(self,playerI):
        """Determines where on the screen the players will be located"""
        if playerI == self.playerWhoseTurnItIs:
            height = self.cardHeight
            return (self.width/2, self.height-height-50)
        if self.rules.numberOfPlayers == 4:
            if ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 1):
                return (60,self.height/2)
            elif ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 2):
                return (self.width/2,50)
            elif ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 3):
                return (self.width-60,self.height/2)
        elif self.rules.numberOfPlayers == 3:
            if ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 1):
                return (60,self.height/2)
            elif ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 2):
                return (self.width-60,self.height/2)
        elif self.rules.numberOfPlayers == 5:
            if ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 1):
                return (60,self.height/2)
            elif ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 2):
                return (self.width/2,50)
            elif ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 3):
                return (self.width-100,50)
            elif ((playerI-self.playerWhoseTurnItIs) % self.rules.numberOfPlayers == 4):
                return (self.width-60,self.height/2)

    def drawTrump(self):
        """Displays what the trump is, if applicable"""
        canvas = self.canvas
        height = self.cardHeight
        (x0,x1,y)=(self.width-125,self.width-75,self.height-height-40)
        self.canvas.create_text(x0,y,text="Trump:",font="Arial 30 bold",
            anchor=E)
        if (0<=self.rules.trump<=3):
            suitImage = self.imageDict[self.rules.trump]
            canvas.create_image(x1, y, image=suitImage, anchor=E)
        elif (self.rules.trump==4):
            self.canvas.create_text(x1,y,text="NT",font="Arial 30 bold",
            anchor=E)

    def cardCenters(self):
        """Determines where the cards will be located depending on the size 
        of the trick"""
        (width,height) = (self.trick[0].width,self.trick[0].height)
        offset = 5
        (cx,cy) = (self.width/2, 2*self.height/5)
        if self.rules.numberOfPlayers == 1: return [(cx,cy)]
        elif self.rules.numberOfPlayers == 2: 
            return [(cx-width/2-offset,cy),(cx+width/2+offset,cy)]
        elif self.rules.numberOfPlayers == 3:
            return [(cx,cy-height/2-offset),
                    (cx-width/2-offset,cy+height/2+offset),
                    (cx+width/2+offset,cy+height/2+offset)]
        elif self.rules.numberOfPlayers == 4:
            return [(cx-width/2-offset,cy-height/2-offset),
                    (cx+width/2+offset,cy-height/2-offset),
                    (cx-width/2-offset,cy+height/2+offset),
                    (cx+width/2+offset,cy+height/2+offset)]
        elif self.rules.numberOfPlayers == 5:
            return [(cx-width/2-offset,cy-height/2-offset),
                    (cx+width/2+offset,cy-height/2-offset),
                    (cx-width-offset*2,cy+height/2+offset),
                    (cx,cy+height/2+offset),
                    (cx+width+offset*2,cy+height/2+offset)]
        else:
            raise Exception("Too many cards in trick...")

class Rules(object):
    """Keeps track of the rules the user specified and how the game works"""
    round = 0
    def __init__(self,**options):
        """Initializes the rules based on what the user specified"""
        # gamePhase: 0 = before, 1 = during gameplay, 2 = after
        self.gamePhase = 0
        self.timesCardHaveBeenDealt = 0
        if "suitsLegalityDict" in options:
            self.suitsLegalityDict = options["suitsLegalityDict"]
        else: self.suitsLegalityDict = {0:True,1:True,2:True,3:True}
        if "omitCards" in options:
            self.omitCards = options["omitCards"]
        else: self.omitCards = []
        if "numberOfDecks" in options:
            self.numberOfDecks = options["numberOfDecks"]
        else: self.numberOfDecks = 1
        if "numberOfPlayers" in options:
            self.numberOfPlayers = options["numberOfPlayers"]
        else: self.numberOfPlayers = 4
        if "cardsPerPlayer" in options:
            self.cardsPerPlayer = options["cardsPerPlayer"]
            if (not self.cardsPerPlayer <= (52-len(self.omitCards))/self.numberOfPlayers):
                raise Exception("You want to deal more cards than there are in the deck")
        else: self.cardsPerPlayer = (52-len(self.omitCards))/self.numberOfPlayers
        if "trump" in options:
            # 0 - 3 correspond to suits, 4 = no trump
            self.trump = options["trump"]
            self.trumpPick = None if type(self.trump)==int else options["trump"]
        else: self.trump = self.trumpPick = None
        if "points" in options:
            self.points = options["points"]
        else: self.points = {}
        if "passCards" in options:
            # Tuple, first element is number of cards, 
            # second is a tuple of directions to pass in
            self.passCards = options["passCards"]
            self.haveCardsPassed = False
        else: self.passCards = (0,("n"))
        if "valueOrder" in options:
            self.valueOrder = options["valueOrder"]
        else: self.valueOrder = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,
                                "9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
        if "dealOrder" in options:
            self.dealOrder = options["dealOrder"]
        else: self.dealOrder = [self.cardsPerPlayer]
        if "bid" in options:
            # Tuple of form (isThereBidBool, min, max, bidType,canPassBool,ifAllPlayersPass,canMatchBid)
            # bidType can be "oneByOne", "round", or "faceOff"
            # ifAllPlayersPass can be "redeal", "round"
            # canMatchBid can be -1 (earlier player can match), 1 (later player can), 0 (no one can), or 2 (everyone can)
            self.bid = options["bid"]
            self.haveBidsHappened = False
        else: self.bid = (False,0,0,"","",2)
        if "playerWhoStarts" in options:
            self.playerWhoStarts = options["playerWhoStarts"]
        else: self.playerWhoStarts = None
        if "partners" in options:
            self.partners = options["partners"]
        else: self.partners = None
        if "isTrumpHidden" in options:
            self.isTrumpHidden = options["isTrumpHidden"]
        else: self.isTrumpHidden = None
        print self.isTrumpHidden
        if "afterRound" in options:
            self.afterRound = options["afterRound"]
        else: self.afterRound = 0
        if "winner" in options:
            # Winner Types: "leastPoints", "mostPoints", "points>=Bid", "points<=Bid", "points==Bid", "mostTricks", "leastTricks", "tricks==bid", "tricks>=bid", "tricks<=bid"
            self.winner = options["winner"]
        else: self.winner = "mostTricks"

    def newGame(self):
        """Initializes a new game"""
        self.round += 1
        self.cardsPerPlayer += self.afterRound
        self.dealOrder[-1] += self.afterRound

    def isSuitLegal(self, card, trick, player):
        """Detemriens whether a suit is legal or not"""
        if len(trick) == 0:
            if self.suitsLegalityDict[card.suit] == True  or len(player.suitsInHand()) == 1: return True
            else: return False
        if trick[0].suit == card.suit:
            return True
        if trick[0].suit not in player.suitsInHand():
            self.suitsLegalityDict[card.suit] = True
            return True
        return False

    def whoGetsTrick(self, trick):
        """Determines which player won a given trick"""
        leadingSuit = trick[0].suit
        maxCardI = 0
        for index in xrange(len(trick)):
            card = trick[index]
            maxCard = trick[maxCardI]
            print repr(card), repr(maxCard), self.trump, self.isTrumpHidden
            cardVal = card.valueOrder[card.valueConversion[card.value]]
            maxCardVal = card.valueOrder[card.valueConversion[maxCard.value]]
            if ((card.suit == leadingSuit and maxCard.suit != self.trump and 
                cardVal > maxCardVal) or (card.suit == self.trump 
                and (trick[maxCardI].suit != self.trump or 
                     (trick[maxCardI].suit == self.trump and cardVal > maxCardVal)) and self.isTrumpHidden != True)):
                maxCardI = index
        playerWhoWinsTrick = trick[maxCardI].playerWhoOwnsTheCard
        print playerWhoWinsTrick
        return playerWhoWinsTrick

    def isStartCardLegal(self, card, trick, player):
        """Determines whetehr a start card is legal or not"""
        if type(self.playerWhoStarts) == tuple:
            startCard = self.playerWhoStarts
        else: startCard = None
        if len(trick) == 0 and len(player.hand) == self.cardsPerPlayer:
            return (card.suit == startCard[0] and card.value == startCard[1]) or Card(*startCard) not in player.hand
        else: return True

    def isCardLegal(self, card, trick, player):
        """Detemrines whether it is legal to play a card or not"""
        if type(self.playerWhoStarts) == tuple:
            startCard = self.playerWhoStarts
        else: startCard = None
        if self.isSuitLegal(card,trick,player):
            if startCard == None or (startCard != None and self.isStartCardLegal(card,trick,player)):
                return True
        return False

    def updateGamePhase(self):
        """Updates the game phase"""
        if self.gamePhase == 0:
            if ((self.passCards[0] == 0 or self.haveCardsPassed or 
                self.passCards[1][self.round%len(self.passCards[1])].lower() == "n") and
                (self.bid[0] == False or self.haveBidsHappened == True)):
                self.gamePhase = 1

    def beforeGameStarts(self, players): pass

    def whoToPassTo(self, playerWhoseTurnItIs):
        """Detemrines who players will pass to"""
        directionI = self.round % len(self.passCards[1])
        direction = self.passCards[1][directionI]
        if (direction[0].lower() == "l"):
            playerToRecieve = playerWhoseTurnItIs + 1
            return playerToRecieve % self.numberOfPlayers
        elif (direction[0].lower() == "r"):
            playerToRecieve = playerWhoseTurnItIs - 1
            return playerToRecieve % self.numberOfPlayers
        elif (direction[0].lower() == "a"):
            if (self.numberOfPlayers % 2 == 0):
                playerToRecieve = playerWhoseTurnItIs + self.numberOfPlayers/2
                return playerToRecieve % self.numberOfPlayers
            else:
                raise Exception("Cannot pass across with an odd number of players")
        else: raise Exception("Unrecognized pass direction")


menu = Menu()
menu.run()
