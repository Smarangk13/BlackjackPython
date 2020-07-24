from dealer import dealer
from player import Player
import time


class gameController:
    currentRound = 0
    players = []
    john = dealer(2)
    totalPlayers = 0
    totalRounds = 0

    def __init__(self):
        self.startGame()

    def startGame(self):
        n = int(input('Enter number of players \n'))
        self.totalPlayers = n

        for i in range(n):
            print('Enter name for player ', i+1)
            name = input()
            print('Enter starting funds for ', name)
            money = int(input())
            player = Player(name, money)
            self.players.append(player)

        print('How many rounds to play?')
        rounds = int(input())
        self.totalRounds = rounds
        self.john.deckShuffle()

    def dealerAi(self):
        bustedCount = 0
        for actor in self.players:
            if actor.status == 'bust':
                bustedCount +=1

        if bustedCount == len(self.players):
            print('Dealer stands- all players bust')
            return

        while self.john.total < 17:
            self.john.dealSelf()
            self.john.showStats()
            time.sleep(3)

    def takeBets(self):
        # take bets
        for actor in self.players:
            print('Player: ', actor.name)
            print('You have $', actor.money)
            bet = int(input('How much do you want to bet: \n'))

            if bet > actor.money:
                bet = actor.money
                print('Insufficient Funds! Betting with ', bet)

            elif bet < 10:
                bet = 10
                print('Minimum bet is 10. Your bet is 10')

            actor.currentBet = bet
            actor.money -= bet

        print('Bets Closed')
        print()

    def dealCards(self):
        print('Dealing Cards')
        time.sleep(2)
        for actor in self.players:
            card = self.john.deal()
            actor.addCard(card)
            card = self.john.deal()
            actor.addCard(card)

            print('Player ', actor.name)
            actor.showStats()
            if actor.total == 21:
                actor.status = 'stand'
                print('Congrats 21!')

            print()
            time.sleep(5)

    def returnCards(self, cards):
        self.john.collect(cards)
        cards.clear()

    def getResults(self):
        self.returnCards(self.john.onHand)
        if self.john.total > 21:
            print('Dealer Bust!')

        # Check winners and give money
        for actor in self.players:
            print(actor.name)
            self.returnCards(actor.cards)
            if actor.status == 'bust':
                print('Sorry you lost', actor.currentBet)

            else:
                if actor.total > self.john.total or self.john.total > 21:
                    print('You won $', actor.currentBet)
                    actor.money += actor.currentBet * 2

                elif actor.total == self.john.total:
                    print('Draw! No money gained')
                    actor.money += actor.currentBet

                else:
                    print('You lose', actor.currentBet)

            if actor.money < 10:
                print('Insufficient funds, you lose')
                self.players.remove(actor)
                continue

            actor.status = 'playing'

    # Checks if all players are playing
    def checkPlayersStopped(self):
        for actor in self.players:
            if actor.status == 'playing':
                return False
        return True

    def gamePlay(self):
        while self.currentRound < self.totalRounds:
            self.currentRound += 1
            print('ROUND ', self.currentRound, '/', self.totalRounds)

            self.takeBets()

            # Setup Give dealer cards
            self.john.dealSelf()
            self.john.dealSelf()

            print('Dealers 1st Card = ', self.john.onHand[0])
            print()
            time.sleep(2)

            # Deal all players cards
            self.dealCards()

            # Allow players to make actions
            while not self.checkPlayersStopped():
                for actor in self.players:
                    if actor.status != 'playing':
                        continue

                    print('Player ', actor.name)
                    actor.showStats()
                    action = actor.actions()

                    if action == 'H':
                        newCard = self.john.deal()
                        actor.addCard(newCard, notify=True)

                        if actor.total > 21:
                            actor.status = 'bust'
                            print('Sorry, you are bust')

                        elif actor.total == 21:
                            print('Total 21!')
                            actor.status = 'stand'

                        print()
                        time.sleep(2)

                    elif action == 'S':
                        actor.status = 'stand'

                    elif action == 'D':
                        if actor.money < actor.currentBet:
                            print('Not enough money to double')
                            continue

                        actor.currentBet *= 2
                        actor.money -= actor.currentBet
                        actor.status = 'stand'
                        print('Doubling bet and standing')
                        actor.showMoney()

                        newCard = self.john.deal()
                        actor.addCard(newCard, notify=True)

                        if actor.total > 21:
                            actor.status = 'bust'
                            print('Sorry, you are bust')

                        print()
                        time.sleep(2)

            print()
            print('Dealer Turn')
            print()
            time.sleep(1)

            # All players done, reveal cards for dealer
            self.john.showStats()
            time.sleep(2)
            self.dealerAi()

            print()
            self.getResults()
            time.sleep(5)
            print('----------------------------------------------------------')
            print()

            if len(self.players) == 0:
                print('House wins')
                return

        print('Game over')
        for actor in self.players:
            print(actor.name)
            print('You are left with $', actor.money)


if __name__ == '__main__':
    gc = gameController()
    gc.gamePlay()
