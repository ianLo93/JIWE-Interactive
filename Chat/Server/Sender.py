"""
Sender implementation to relay messages
"""
from User import User

class Sender:
    def __init__(self, username):
        self.conn_ = User.user
