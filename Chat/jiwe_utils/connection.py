"""
Connection class
"""
class Connection:

    CONST_BUFFER_SIZE = 4096

    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def fileno(self):
        return self.conn.fileno()

    # supposed to analyze the msg and relay to some other user
    def on_read(self):
        msg_buff = self.conn.recv(Connection.CONST_BUFFER_SIZE)
        # only strings for now
        msg = msg_buff.decode('utf8')
        print('<' + self.addr[0] + '> ' + msg, end='')

    def send(self):
        pass

    def close():
        self.conn.close()
