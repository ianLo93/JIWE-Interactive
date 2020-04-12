"""
Receiver class implementation to keep server running 
and handle messages from clients
"""
from jiwe_utils.application import Application
from jiwe_utils.connection import Connection
import socket
import select
import sys

class ServerApplication(Application):

    def __init__(self):
        super().__init__()
        self.connections = []

    def setUp(self, sock = None):
        super().setUp(sock)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connections.append(self.sock)

    def accept(self):
        return self.sock.accept()

    def close(self):
        self.sock.close()

    def run(self):

        while True:
            read_socks, _, _ = select.select(self.connections, [], [])

            for sock in read_socks:
                if sock == self.sock:
                    conn, addr = self.accept()
                    self.connections.append(Connection(conn, addr))
                    print(addr[0] + " connected")
                else:
                    try: 
                        sock.on_read()
                    except:
                        print("receive() exiting...")
                        exit()

        self.close()
                        
if __name__ == '__main__':
    
    if (len(sys.argv) != 3):
        print("Error input\nUsage: server IP_address port")
        sys.exit()

    try:
        app = ServerApplication()

        app.setUp()
        app.bind(sys.argv[1], int(sys.argv[2]))
        app.listen(5)

        app.run()
    except:
        print("Caught Exception")
