# Question: Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack.
import random


class Deck:
    def __init__(self):
        self.cards = [
            Card("Ace", "Hearts", 14),
            Card("Two", "Hearts", 2),
            Card("Queen", "Diamonds", 12),
            Card("Eight", "Clubs", 8),
            Card("King", "Spades", 13),
            Card("Ten", "Clubs", 10),
        ]
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
