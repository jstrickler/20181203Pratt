#!/usr/bin/env python
import random

# self == 'this'

class CardDeck():
    SUITS = 'clubs diamonds hearts spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    # constructor
    def __init__(self, dealer_name):
        self._dealer_name = None

        self.dealer_name = dealer_name
        self._create_cards()

    def _create_cards(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    # don't use this (probably)
    def get_dealer(self):  # getter method
        return self._dealer_name

    @property
    def dealer_name(self):  # getter property
        return self._dealer_name

    # dealer_name = property(dealer_name)

    @dealer_name.setter
    def dealer_name(self, dealer_name): # setter property
        if isinstance(dealer_name, str):
            self._dealer_name = dealer_name
        else:
            raise TypeError("Dealer must be a string")


    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({len(self)})"

    def __add__(self, other):
        tmp = type(self)(self.dealer_name)
        tmp._cards = self.cards + other.cards
        return tmp


