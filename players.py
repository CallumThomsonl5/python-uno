from card_definitions import *

def allocPlayerCards(n_players, stack):
    if n_players < 2: return

    players_cards = {}

    # create entries for all players
    for player in range(n_players):
        players_cards[player] = []

    # deal each player 7 cards from the stack
    for x in range(7):
        # loop each player
        for player in range(len(players_cards)):
            players_cards[player].append(stack.pop(0))

    return players_cards

class Player:
    def __init__(self, conn, hand, number) -> None:
        self.conn = conn
        self.hand = hand
        self.number = number

    def pick_up(self, cards_to_add):
        for card in cards_to_add:
            self.hand.append(card)

    def place(self, index_to_remove):
        return self.hand.pop(index_to_remove)