"""
Receiver class implementation to keep server running 
and handle messages from clients
"""
import socket

class Receiver:

    def __init__(self):
        self.server = None

    def setUp(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, ip, port):
        self.server.bind((ip, port))

    def listen(self, n):
        self.server.listen(n)

    def accept(self):
        return self.server.accept()

    def close(self):
        self.server.close()

    def run(self):
        pass
                        
if __name__ == '__main__':
    
    if (len(sys.argv) != 3):
        print("Error inputs\nUsage: Receiver IP_address Port")
        sys.exit()

    try:
        receiver = Receiver()

        receiver.setUp()
        receiver.bind(sys.argv[1], int(sys.argv[2]))
        receiver.listen(5)
        print("Receiver set up successfully")
    except:
        print("Caught Exception")
