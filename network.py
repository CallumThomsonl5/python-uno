from socket import socket
from binascii import unhexlify
from threading import Thread
import pickle

active_clients = []

class ClientHandle(Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.hand = None
        self.facing_up = None
        self.number = len(active_clients) - 1

    def run(self):
        # grab display name
        self.display_name = self.conn.recv(1024).decode("utf-8")
        print("got " + self.display_name)

        # send hand
        while True:
            if self.hand:
                self.conn.sendall(pickle.dumps(self.hand))
                self.conn.sendall(pickle.dumps(self.facing_up))
                break

        


        
        # send facing up


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
        

