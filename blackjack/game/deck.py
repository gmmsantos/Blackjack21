from blackjack.game.card import Card
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)


class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                # Create the card Object
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp = deck_comp + "\n" + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()
