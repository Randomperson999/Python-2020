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
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.isBusted and player.isHitting():
            self.deck.deal([player], 1)
            print(player)
            if player.isBusted():
                player.bust()
    def play(self):
        # deal 2 cards to all players and dealer
        self.deck.deal(self.players+[self.dealer], 2)
        self.dealer.flip_first_card()
        print(self.dealer)

        for player in self.players:
            print(player)
            self.__additional_cards(player)

        # reveal dealer's first card
        self.dealer.flip_first_card()
        if not self.stillPlaying:
            # Since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.isBusted():
                for player in self.stillPlaying:
                    player.win()
            else:
                for player in self.stillPlaying:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\t\tWelcome to Blackjack!\n\t(Don't Gamble with real money)")
    names = []
    num_players = gf.getNum("How many players? (1 - 7):\n", 1, 8)
    for i in range(num_players):
        name = gf.getInput("What is your name?", 3, 13)
        names.append(name)
    game = Game(names)

    play = None
    while play != "n":
        game.play()
        play = gf.yesOrNo("You want to play again", 1, 5)


main()
