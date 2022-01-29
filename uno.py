from card_definitions import *
from random import shuffle
from time import sleep
from network import ServerThread, active_clients
from utils import allocPlayerCards

face_down_stack = [NormalCard("red", 0), NormalCard("red", 1), NormalCard("red", 2), NormalCard("red", 3), NormalCard("red", 4), NormalCard("red", 5), NormalCard("red", 6), NormalCard("red", 7), NormalCard("red", 8), NormalCard("red", 9), NormalCard("red", 1), NormalCard("red", 2), NormalCard("red", 3), NormalCard("red", 4), NormalCard("red", 5), NormalCard("red", 6), NormalCard("red", 7), NormalCard("red", 8), NormalCard("red", 9), NormalCard("green", 0), NormalCard("green", 1), NormalCard("green", 2), NormalCard("green", 3), NormalCard("green", 4), NormalCard("green", 5), NormalCard("green", 6), NormalCard("green", 7), NormalCard("green", 8), NormalCard("green", 9), NormalCard("green", 1), NormalCard("green", 2), NormalCard("green", 3), NormalCard("green", 4), NormalCard("green", 5), NormalCard("green", 6), NormalCard("green", 7), NormalCard("green", 8), NormalCard("green", 9), NormalCard("yellow", 0), NormalCard("yellow", 1), NormalCard("yellow", 2), NormalCard("yellow", 3), NormalCard("yellow", 4), NormalCard("yellow", 5), NormalCard("yellow", 6), NormalCard("yellow", 7), NormalCard("yellow", 8), NormalCard("yellow", 9), NormalCard("yellow", 1), NormalCard("yellow", 2), NormalCard("yellow", 3), NormalCard("yellow", 4), NormalCard("yellow", 5), NormalCard("yellow", 6), NormalCard("yellow", 7), NormalCard("yellow", 8), NormalCard("yellow", 9), NormalCard("blue", 0), NormalCard("blue", 1), NormalCard("blue", 2), NormalCard("blue", 3), NormalCard("blue", 4), NormalCard("blue", 5), NormalCard("blue", 6), NormalCard("blue", 7), NormalCard("blue", 8), NormalCard("blue", 9), NormalCard("blue", 1), NormalCard("blue", 2), NormalCard("blue", 3), NormalCard("blue", 4), NormalCard("blue", 5), NormalCard("blue", 6), NormalCard("blue", 7), NormalCard("blue", 8), NormalCard("blue", 9), ReverseCard("red"), ReverseCard("red"), ReverseCard("green"), ReverseCard("green"), ReverseCard("yellow"), ReverseCard("yellow"), ReverseCard("blue"), ReverseCard("blue"), Pick2Card("red"), Pick2Card("red"), Pick2Card("green"), Pick2Card("green"), Pick2Card("yellow"), Pick2Card("yellow"), Pick2Card("blue"), Pick2Card("blue"), NullCard("red"), NullCard("red"), NullCard("green"), NullCard("green"), NullCard("yellow"), NullCard("yellow"), NullCard("blue"), NullCard("blue"), WildCard(), Wild4Card(), WildCard(), Wild4Card(), WildCard(), Wild4Card(), WildCard(), Wild4Card(),]
# shuffle stack
shuffle(face_down_stack)

# create face up
face_up_stack = [face_down_stack.pop(0)]

# important vars
number_of_players = 2
game_running = False

# setup server for listening
server = ServerThread("localhost", 57244, game_running)
server.start()

print("Waiting for players")
while len(active_clients) < number_of_players:
    pass

# deal with player setup
# create dict holding players cards
player_card_data = allocPlayerCards(number_of_players, face_down_stack)
# add hands to players
for player in range(len(active_clients)):
    active_clients[player].hand = player_card_data[player]
    active_clients[player].facing_up = face_up_stack[-1]
    

# Game Loop
turn = 0
print(face_up_stack[-1])
while game_running:
    

    if turn == number_of_players - 1:
        turn = 0
    else:
        turn += 1