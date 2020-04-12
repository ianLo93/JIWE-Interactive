"""
Application abstract class, set up socket
"""
import socket
import sys

class Application:

    def __init__(self):
        self.sock = None

    def setUp(self, sock = None):
        if sock == None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def bind(self, ip, port):
        self.sock.bind((ip, port))

    def listen(self, n):
        self.sock.listen(n)

    def close(self):
        self.sock.close()

    def run(self):
        pass
                        
if __name__ == '__main__':
    
    if (len(sys.argv) != 3):
        print("Error inputs\nUsage: Receiver IP_address Port")
        sys.exit()

    try:
        app = Application()

        app.setUp()
        app.bind(sys.argv[1], int(sys.argv[2]))
        app.listen(5)
        print("Application set up successfully")
    except:
        print("Caught Exception")
