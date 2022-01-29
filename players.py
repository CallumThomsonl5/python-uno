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
