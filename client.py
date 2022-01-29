from socket import socket
from threading import Thread
from os import system, get_terminal_size
from card_definitions import *
import pickle

class GameConnection(Thread):
    def __init__(self, host, port, display_name):
        super().__init__()
        self.host = host
        self.port = port
        self.display_name = display_name
        self.hand = None

        self.s = socket()

    def send(self, msg):
        self.s.sendall(msg.encode("utf-8"))

    def run(self):
        self.s.connect((self.host, self.port))

        # send required inital data
        self.send(self.display_name)

        # receive hand
        self.hand = pickle.loads(self.s.recv(1024))

        # receive facing up
        self.facing_up = pickle.loads(self.s.recv(1024))

def create_padding(cols):
    padding = ""
    for x in range(cols):
        padding += " "

    return padding

# test vars
current_turn = 0

con = GameConnection("localhost", 57244, "calluj")
con.start()

while not con.hand:
    pass

hand = con.hand
up_card = con.facing_up

# create screen
system("cls")

print(f"turn: {current_turn}")
print(f"facing up: {up_card}")

print("\n\n\n\n\n\n")
for card in hand:
    print(f"{create_padding(10)} {card}")

for x in range(get_terminal_size().lines - 30):
    print("\n")

print("command")
input("> ")