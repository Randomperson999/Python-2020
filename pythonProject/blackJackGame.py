# Caleb Keller
# Black Jack Game
# 1/21/2020
import game_functions as gf
import playingCards as pc

class BJ_Card(pc.PosCard):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.faceUp:
            v = BJ_Card.RANKS.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v
class BJ_Deck(pc.Deck):
    def populate(self):
        for suit in pc.Card.SUITS:
            for rank in pc.Card.RANKS:
                self.add(BJ_Card(rank,suit))

class BJ_Hand(pc.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        print("|-----------------------------------------------------------------------|")
        for i in range(len(self.cards)):
            print(self.cards[i])
        rep = "|-----------------------------------------------------------------------|"
        rep += "\n "+ self.name
        rep += "\n"+ self.total
        return rep
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        #Add card values.
        t = 0
        for card in self.cards:
            t= card.value

        #If an ace in hand.
        hasAce = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                hasAce == True
        #If it has an ace and is low enough, treat it like an ace.
        if hasAce and self.total <=  11:
            t+= 10 # Add only 10 since we've already added 1 for the Ace.
        return t
    def isBusted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):

    def bust(self):
        print(self.name, "busts")
        
    def lose(self):
        print(self.name, "loses")
        
    def win(self):
        print(self.name, "wins")
        
    def push(self):
        print(self.name,  "pushes")
        
    def isHitting(self):
        response = gf.yesOrNo("\n"+self.name+", do you want a hit?")
        return response == "Y"
    
class BJ_Dealer(BJ_Hand):
    def isHitting(self):
        return self.total < 17
    
    def bust(self):
        print(self.name, "busts.")
        
    def flip_first_card(self):
        self.cards[0].flip()
class Game(object):
    def __init__(self, names):
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BJ_Dealer("Dealer Tim")
        self.players = []
        for name in names:
            player  = BJ_Player(name)
            self.players.append(player)
    @property
    def stillPlaying():
        sp = []
        for player in self.players:
            sp.append(player)
        return sp
            
#Testing Area:
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
