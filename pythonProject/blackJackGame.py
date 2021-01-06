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
#Testing Area:
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)