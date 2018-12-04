#!/usr/bin/env python

from carddeck import CardDeck

class Dog():
    def bark(self):
        print("Woof! woof!")

class JokerDeck(CardDeck, Dog):
    SUITS = 'SPOCKS KIRKS UHURUS'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A Joker'.split()

    # def _create_cards(self):
    #     super()._create_cards()
    #     self._cards.append((1, 'Joker'))
    #     self._cards.append((2, 'Joker'))


