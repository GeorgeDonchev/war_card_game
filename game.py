from project.deck import Deck, RANKS
from project.hand import Hand
from project.player import Player

d = Deck()
d.shuffle()
half1, half2 = d.cut_on_half()

comp = Player('comp', Hand(half1))

name = input('Type your name plaes: ')
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.check_available_cards() and comp.check_available_cards():
    total_rounds+=1
    print('Time for a new round')
    print('here are the current status')
    print(f'{user.name} has the count: {len(user.hand.cards)}')
    print(f'{comp.name} has the count: {len(comp.hand.cards)}')
    print()

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card [1]:
        war_count+=1
        print('War!')

        table_cards.extend(user.war())
        table_cards.extend(comp.war())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add_card(table_cards)
        else:
            comp.hand.add_card(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add_card(table_cards)
        else:
            comp.hand.add_card(table_cards)

