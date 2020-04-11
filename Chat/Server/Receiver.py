"""
Receiver class implementation to keep server running 
and relay messages between clients
"""
from User import User, Connection
# from Message import Message
import socket
import select
from _thread import *
import sys

class Receiver:

    server = None
    connections = []

    @staticmethod
    def setUp():
        Receiver.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Receiver.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        Receiver.connections.append(Receiver.server)

    @staticmethod
    def bind(ip, port):
        Receiver.server.bind((ip, port))

    # Max number of connections listening
    @staticmethod
    def listen(n):
        Receiver.server.listen(n)

    @staticmethod
    def accept():
        return Receiver.server.accept()

    @staticmethod
    def close():
        Receiver.server.close()

    @staticmethod
    def run():

        while True:
            read_sockets, _, _ = select.select(Receiver.connections, [], [])

            for read_socket in read_sockets:

                if read_socket == Receiver.server:
                    conn, addr = Receiver.accept()
                    connection = Connection(conn, addr)
                    Receiver.connections.append(connection)
                    print(addr[0] + " connected")
                else:
                    try: 
                        read_socket.on_read()
                    except:
                        print("receive() exiting...")
                        exit()

        Receiver.close()
                        
if __name__ == '__main__':
    
    if (len(sys.argv) != 3):
        print("Error input\nUsage: server IP_address port")
        sys.exit()

    Receiver.setUp()
    Receiver.bind(sys.argv[1], int(sys.argv[2]))
    Receiver.listen(5)

    Receiver.run()
