from socket import socket
from binascii import unhexlify
from threading import Thread

active_clients = []

class ClientHandle(Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.player = None

    def run(self):
        # grab display name
        self.display_name = self.conn.recv(1024).decode("utf-8")
        print("got " + self.display_name)

        # listen for data
        while True:
            data = self.conn.recv(1024)
            if data:
                print(data.decode("utf-8"))
    

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
        

