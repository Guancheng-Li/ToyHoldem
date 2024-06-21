"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The client based on socket connection.
"""

import socket
import time

from core.network.message import Message


MESSAGE_LIMIT = 1024


class SocketClient:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._validate()
        self._client_socket = None

    def _validate(self):
        assert self._port < 65535 and self._port > 1024, \
            'The port is not valid.'

    def connect(self):
        self.close()
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self._host, self._port)
        self._client_socket.connect(server_address)

    def close(self):
        if self._client_socket is not None:
            self._client_socket.close()
            self._client_socket = None

    def send_message(self, message: Message):
        message_bytes = message.json().encode()
        self._client_socket.send(message_bytes)

    def run(self):
        while True:
            received_message = self._client_socket.recv(MESSAGE_LIMIT).decode()
            print("Received:", received_message)

            time.sleep(5)
            self._client_socket.send(b'Heartbeat')

