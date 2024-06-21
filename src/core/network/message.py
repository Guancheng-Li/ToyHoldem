"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The message definition between each role.
"""

import enum
from typing import Dict, List

class MessageType(enum.Enum):
    CONNECT = 0
    RECONNECT = 1
    DISCONNECT = 2
    ACK = 3

class Message():
    def __init__(
        self,
        message_type: MessageType,
        content: Dict[str, str],
        sender: str,  # client id, '-1' for server.
        receiver: List[str],
        # client id list, '-1' for server, none for broadcast.
        need_ack: bool = False,
    ):
        self._type = message_type
        self._content = content
        self._sender = sender
        self._receiver = receiver
        self._need_ack = need_ack
