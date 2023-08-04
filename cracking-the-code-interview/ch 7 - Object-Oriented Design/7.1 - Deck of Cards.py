# Question: Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack.
import random


# General Deck
class Deck:
    def __init__(self):
        self.cards = []
        self.dealIdx = 0

    def deal(self):
        if self.dealIdx >= len(self.cards):
            raise ValueError("No more cards available")
        else:
            card = self.cards[self.dealIdx]
            card.setAvailability(False)
            self.dealIdx += 1
            return card

    def dealHand(self, numCards):
        if self.dealIdx + numCards > len(self.cards):
            raise ValueError("Not enough cards available")
        else:
            hand = []
            for i in range(numCards):
                hand.append(self.deal())
            return hand

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self):
        for i in range(self.dealIdx):
            self.cards[i].setAvailability(True)
        self.dealIdx = 0
        self.shuffle()

    def remainingCards(self):
        return len(self.cards) - self.dealIdx

    def addCard(self, card):
        self.cards.append(card)


# General Card
class Card:
    def __init__(self, face, suit, value, available=True):
        self.face = face
        self.suit = suit
        self.value = value
        self.available = available

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getFace(self):
        return self.face

    def setAvailability(self, availability):
        self.available = availability

    def isAvailable(self):
        return self.available


# General Hand
class Hand:
    def __init__(self):
        self.cards = []

    def getScore(self):
        score = 0
        for card in self.cards:
            score += card.getValue()
        return score

    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, idx=0):
        if len(self.cards) <= 0:
            raise ValueError("Cannot remove a card. There are no cards in your hand.")
        self.cards.pop(idx)


# Blackjack Card
class BlackJackCard(Card):
    def __init__(self, face, suit, value, available=True):
        super().__init__(face, suit, value, available)

    def isAce(self):
        return self.value == 14

    def isFaceCard(self):
        return self.value > 10 and self.value < 14

    def getValue(self):
        if self.isFaceCard():
            return 10
        if self.isAce():
            return [1, 11]
        return self.value


class BlackJackHand(Hand):
    def score(self):
        result = 0
        ace = None
        for card in self.cards:
            if card.isAce():
                ace = card
            else:
                result += card.getValue()

        if ace:
            max = result + ace.getValue()[1]
            min = result + ace.getValue()[0]
            if max > 21:
                return min
            else:
                return max

        return result

    def is21(self):
        return self.score() == 21

    def busted(self):
        return self.score() > 21

    def possibleScores(self):
        result = 0
        ace = None
        for card in self.cards:
            if card.isAce():
                ace = card
            else:
                result += card.getValue()

        if ace:
            max = result + ace.getValue()[1]
            min = result + ace.getValue()[0]
            return [min, max]

        return result

    def isBlackJack(self):
        firstTwoCards = len(self.cards) == 2
        return firstTwoCards and self.is21()


cards = [
    BlackJackCard("Ten", "Clubs", 10),
    BlackJackCard("Ace", "Hearts", 14),
    BlackJackCard("Two", "Hearts", 2),
    BlackJackCard("Queen", "Diamonds", 12),
    BlackJackCard("Eight", "Clubs", 8),
    BlackJackCard("King", "Spades", 13),
]
myDeck = Deck()

for card in cards:
    myDeck.addCard(card)

myBlackJackHand = BlackJackHand()

for i in range(2):
    dealtCard = myDeck.deal()
    myBlackJackHand.addCard(dealtCard)

print(myBlackJackHand.isBlackJack())
