import cardLogic
import random


def makeDeck():
    hearts = [str(i) + ' H' for i in range(2, 11)]
    hearts += ['A H', 'J H', 'Q H', 'K H']
    clubs = [str(i) + ' C' for i in range(2, 11)]
    clubs += ['A C', 'J C', 'Q C', 'K C']
    spades = [str(i) + ' S' for i in range(2, 11)]
    spades += ['A S', 'J S', 'Q S', 'K S']
    diamonds = [str(i) + ' D' for i in range(2, 11)]
    diamonds += ['A D', 'J D', 'Q D', 'K D']
    deck = hearts + clubs + diamonds + spades
    return deck


class dealer:
    # ['2H,2C,2D,2S']
    onHand = []
    total = 0

    def __init__(self, decks):
        self.deck = makeDeck() * decks
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def collect(self, cards):
        self.deck += cards + self.deck

    def deckShuffle(self):
        random.shuffle(self.deck)

    def dealSelf(self):
        self.onHand.append(self.deal())
        self.total = cardLogic.cardTotal(self.onHand)

    def showCards(self):
        for card in self.onHand:
            print(card, '\t', end='\t')
        print()

    def showStats(self):
        print('Dealer cards are: ')
        self.showCards()
        print('Dealer total = ', self.total)
