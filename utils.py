import sys


def generate_card_stack_arr():
    stack = []


    # Normal
    colours = ["red", "green", "yellow", "blue"]
    for colour in colours:

        for x in range(10):
            sys.stdout.write( f"NormalCard(\"{colour}\", {x}), " )

        for x in range(1,10):
            sys.stdout.write( f"NormalCard(\"{colour}\", {x}), " )

    # Reverse
    for colour in colours:
        sys.stdout.write( f"ReverseCard(\"{colour}\"), " )
        sys.stdout.write( f"ReverseCard(\"{colour}\"), " )

    # Pick 2
    for colour in colours:
        sys.stdout.write(f"Pick2Card(\"{colour}\"), ")
        sys.stdout.write(f"Pick2Card(\"{colour}\"), ")

    # Null Cards
    for colour in colours:
        sys.stdout.write(f"NullCard(\"{colour}\"), ")
        sys.stdout.write(f"NullCard(\"{colour}\"), ")

    # Wilds
    for x in range(4):
        sys.stdout.write("WildCard(), ")
        sys.stdout.write("Wild4Card(), ")


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

def allocSingerPlayerCards(stack):
    hand = []

    for x in range(7):
        hand.append(stack.pop(0))

    return hand

def sendAllPlayers(active_clients, msg):
    for client in active_clients:
        client.conn.send(msg)