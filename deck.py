from random import shuffle


SUITE ='H D S C'.split(' ')
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split(' ')


class Deck:
    def __init__(self):
        self.full_deck = [(s, r) for r in RANKS for s in SUITE]

    def shuffle(self):
        shuffle(self.full_deck)

    def cut_on_half(self):
        first_half = [self.full_deck[d] for d in range(26)]
        second_half = [self.full_deck[d] for d in range(26, 52)]
        return first_half, second_half
