from socket import socket
from binascii import unhexlify
from threading import Thread
import pickle
from uno import face_down_stack, face_up_stack

active_clients = []

class ClientHandle(Thread):
    def __init__(self, conn, started):
        super().__init__()
        self.conn = conn
        self.started = started
        self.number = len(active_clients) - 1

        self.hand = []
        for x in range(7):
            self.hand.append(face_down_stack.pop(0))

    def run(self):
        # grab display name
        self.display_name = self.conn.recv(1024).decode("utf-8")
        print(self.display_name + " connected")

        # send hand and facing up and first turn
        self.conn.sendall(pickle.dumps((self.hand, face_up_stack[-1], self.number)))

        # listen for data
        while True:
            data = self.conn.recv(1024)
            if data:
                print(data.decode("utf-8"))

    def pick_up(self, cards_to_add):
        for card in cards_to_add:
            self.hand.append(card)

    def place(self, index_to_remove):
        return self.hand.pop(index_to_remove)

    def send_facing_up(self, card):
        self.conn.sendall(pickle.dumps(card))

    def send(self, msg):
        self.conn.sendall(msg.encode("utf-8"))
    

class ServerThread(Thread):
    def __init__(self, host, port, started):
        super().__init__()
        self.host = host
        self.port = port
        self.started = started
        self.s = socket()
        self.s.settimeout(1)
        self.s.bind((host,port))
    
    def run(self):
        self.s.listen()

        while not self.started:
            try:
                conn, addr = self.s.accept()
                handler_th = ClientHandle(conn)
                active_clients.append(handler_th)
                handler_th.start()
            except:
                pass
        

