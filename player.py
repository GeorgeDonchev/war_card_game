class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f'{self.name} has placed {drawn_card}. ')
        print()
        return drawn_card

    def war(self):
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            war_deck = [self.hand.remove_card() for _ in range(3)]
            return war_deck

    def check_available_cards(self):
        return len(self.hand.cards)!=0

