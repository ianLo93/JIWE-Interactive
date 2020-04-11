"""
Connection class,
"""
class Connection:

    CONST_BUFFER_SIZE = 4096

    def __init__(self, conn, addr):
        self.conn_ = conn
        self.addr_ = addr

    def fileno(self):
        return self.conn_.fileno()

    # supposed to analyze the msg and relay to some other user
    def on_read(self):
        # only string for now
        msg = self.conn_.recv(Connection.CONST_BUFFER_SIZE).decode('utf8')
        print(msg, end='')

    def send(self):
        pass

    def close():
        self.conn_.close()