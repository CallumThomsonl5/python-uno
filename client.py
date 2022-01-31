from socket import socket
from threading import Thread, Event
from os import system
from card_definitions import *
from time import sleep
import pickle

class GameConnection(Thread):
    def __init__(self, host, port, display_name):
        super().__init__()
        self.host = host
        self.port = port
        self.display_name = display_name
        self.number = None
        self.hand = None
        self.started = False

        self.s = socket()

    def send(self, msg):
        self.s.sendall(msg.encode("utf-8"))

    def run(self):
        self.s.connect((self.host, self.port))

        # send required inital data
        self.send(self.display_name)

        # receive hand and facing up
        initial_data = pickle.loads(self.s.recv(1024))
        self.hand = initial_data[0]
        self.facing_up = initial_data[1]
        self.number = initial_data[2]

        # wait for start signal
        while True:
            data = self.s.recv(1024).decode("utf-8")
            if data == "START":
                self.started = True
                game_started_event.set()
                break

conn = GameConnection("localhost", 57244, "calluj")
conn.start()

game_started_event = Event()

hand = conn.hand
up_card = conn.facing_up
current_turn = 0

# wait for game start
game_started_event.wait()

# create screen
system("cls")

print(f"turn: {current_turn}")
print(f"facing up: {up_card}")

for card in hand:
    print(card)

print("command")
input("> ")