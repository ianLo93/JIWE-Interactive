"""
Connection class
"""
class Connection:

    BUFFERSIZE = 2048 
    MAXOBJECTSIZE= 10 * 1024 * 1024

    def __init__(self, sock, addr):
        self.sock = sock 
        self.addr = addr

    def fileno(self):
        return self.sock.fileno()

    def on_read(self):
        print(self.sock.recv(1024).decode('utf8'), end='') # echo for now
        pass

    def send(self):
        pass

    def receive(self):
        pass

    def close():
        self.conn.close()
