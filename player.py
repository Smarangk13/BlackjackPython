import cardLogic


class Player:
    name = ''
    currentBet = 0
    action = ''
    status = 'playing'  # playing or stopped or bust
    total = 0

    def __init__(self, name, money):
        self.money = money
        self.name = name
        self.cards = []

    def showMoney(self):
        print('Your money is', self.money)

    def showCards(self):
        print('Your cards on hand are- ')
        for card in self.cards:
            print(card, '\t', end='')
        print()
        print('Card total = ', self.total)

    def showStats(self):
        self.showMoney()
        self.showCards()

    def actions(self):
        print('S to stand')
        print('H to hit')
        print('D to double down')
        self.action = input('Select action\n')

        self.action = self.action.upper()
        if self.action not in ['S', 'D', 'H']:
            return self.actions()

        return self.action

    def addCard(self, card, notify=False):
        self.cards.append(card)
        self.total = cardLogic.cardTotal(self.cards)
        if notify:
            print('Your new card is ', card)
            print('Your new total us ', self.total)
