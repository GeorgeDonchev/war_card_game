class Hand():
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, add_card):
        self.cards.extend(add_card)

    def remove_card(self):
        return self.cards.pop()
