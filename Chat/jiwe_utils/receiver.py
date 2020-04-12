"""
Receiver class implementation to keep server running 
and handle messages from clients
"""
import pickle
import struct
import select

class Receiver:

    def __init__(self, conn):
        self.conn = conn

    def deserialize(self, obj_in_bytes):
        return pickle.loads(obj_in_bytes)

    def recv_indicator(self):
        self.conn.setblocking(True)
        ready = select.select([self.conn], [], [])
        if ready[0]:
            buf = self.conn.recv(4)
        else:
            return None

        return struct.unpack('!I', buf[:4])[0]

    def recv_obj(self, buff_size, obj_size):
        chunks = []
        bytes_recd = 0
        self.conn.setblocking(False)
        while bytes_recd < obj_size:
            ready = select.select([self.conn], [], [], 1)
            if ready[0]:
                data = self.conn.recv(min(obj_size - bytes_recd, buffer_size))
            else:
                return None

            chunks.append(data)
            bytes_recd = bytes_recd + len(data)

        return deserialize(''.join(chunks))
