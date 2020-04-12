"""
Sender implementation to relay messages
"""
from connection import Connection
import struct
import pickle
import threading

class Sender:

    def __init__(self, conn):
        self.conn = conn
        self.lock = threading.Lock()

    def serialize(self, obj):
        return pickle.dumps(obj)

    def send_obj(self, obj, max_obj_size):
        self.lock.acquire()
        try:
            obj_in_bytes = self.serialize(obj)
            obj_in_bytes = struct.pack('!I', len(obj_in_bytes)) + obj_in_bytes
            self.conn.sendall(obj_in_bytes)
            print("object sent")
        except:
            print("object send failed")
        finally:
            self.lock.release()
