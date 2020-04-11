"""
Receiver class implementation to keep server running 
and handle messages from clients
"""
from user import User
from connection import connection
from message import Message
import socket
import select
from _thread import *
import sys

class Receiver:

    def __init__(self):
        self.server_ = None
        self.connections_ = []

    def setUp(self):
        self.server_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connections_.append(self.server_)

    def bind(self, ip, port):
        self.server_.bind((ip, port))

    # Max number of connections listening
    def listen(self, n):
        self.server_.listen(n)

    def accept(self):
        return self.server_.accept()

    def close(self):
        self.server_.close()

    def run(self):

        while True:
            read_sockets, _, _ = select.select(self.connections_, [], [])

            for read_socket in read_sockets:

                if read_socket == self.server_:
                    conn, addr = self.accept()
                    connection = Connection(conn, addr)
                    self.connections_.append(connection)
                    print(addr[0] + " connected")
                else:
                    try: 
                        read_socket.on_read()
                    except:
                        print("receive() exiting...")
                        exit()

        self.close()
                        
if __name__ == '__main__':
    
    if (len(sys.argv) != 3):
        print("Error input\nUsage: server IP_address port")
        sys.exit()

    receiver = Receiver()

    receiver.setUp()
    receiver.bind(sys.argv[1], int(sys.argv[2]))
    receiver.listen(5)

    receiver.run()
