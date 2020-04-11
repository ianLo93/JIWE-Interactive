"""
This files declares Message Objects
"""


import json
from enum import Enum

class Type:
    SIGNUP = 1
    LOGIN = 2
    TEXT = 3
    LOGFF = 4
    ACK_SIGNUP = 5
    ACK_LOGIN = 6
    ACK_TEXT = 7
    ACK_LOGFF = 8

class Message:
    def __init__(self, sender, receiver, body, group=False):
        self._sender = sender
        self._receiver = receiver
        self._group_ = group
        self._body = body
        self.delivered = False

    @property
    def sender(self):
        return self._sender

    @property
    def receiver(self):
        return self._receiver

    @property
    def body(self):
        return self._body
