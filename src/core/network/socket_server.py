"""
Authors: guanchenglichina@qq.com (Guancheng Li)

The server based on socket connection.
"""

import socket
import time
import logging

MAX_CLIENT_NUM = 12
MIN_CLIENT_NUM = 2

class SocketServer:
    def __init__(self, host: str, port: int, client_num: int):
        self._host = host
        self._port = port
        self._client_num = client_num
        self._validate()
        self.server_socket = None
        self._client_socket = []

    def _validate(self):
        assert self._port < 65535 and self._port > 1024, \
            'The port is not valid.'
        assert self._client_num <= MAX_CLIENT_NUM and \
            self._client_num >= MIN_CLIENT_NUM, \
                'The client number is not valid.'

    def _create_socket(self):
        if self.server_socket is not None:
            # NOTE: Maybe need to add try.
            self.server_socket.close()
            for client_socket in self._client_socket:
                client_socket.close()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self._host, self._port)
        self.server_socket.bind(server_address)
        self.server_socket.listen(self._client_num)

    def _wait_for_client(self):
        while len(self._client_socket) < self._client_num:
            client_socket, client_address = self.server_socket.accept()
            client_socket.send('Welcome to the server!'.encode())
            self._client_socket.append(client_socket)

    def send_message_to_all_clients(self, message: str):
        pass

    def send_message_to_client(self, client_id: int, message: str):
        pass

    def run(self):
        self._create_socket()

# # 用于存储客户端连接
# client_sockets = []

# while True:
#     # 接受新的连接
#     client_socket, client_address = server_socket.accept()
#     client_sockets.append(client_socket)

#     # 向客户端发送数据
#     for client in client_sockets:
#         message = f"Server time: {time.strftime('%Y-%m-%d %H:%M:%S')}"
#         client.send(message.encode())

#     # 处理客户端断开连接
#     for client in client_sockets:
#         if client.fileno() == -1:
#             client_sockets.remove(client)