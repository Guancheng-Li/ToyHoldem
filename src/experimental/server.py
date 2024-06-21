import socket
import time
import threading
import random


# 接收客户端消息的线程
def receive(client_socket):
    while True:
        # try:
        message = client_socket.recv(1024).decode()
        if message:
            print("Received from client:", message)
        #     else:
        #         # 客户端关闭连接
        #         client_socket.close()
        #         break
        # except Exception as e:
        #     print(f"Error receiving message: {e}")
        #     client_socket.close()
        #     break

# 发送消息给客户端的线程
def send():
    while True:
        message = input("Enter message to send to client: ")
        client_socket.send(message.encode())

def handle_client(client_socket):
    receive_thread = threading.Thread(target=receive, args=(client_socket,))
    send_thread = threading.Thread(target=send)
    receive_thread.start()
    send_thread.start()

def get_random_port():
    port = random.randint(5000, 50000)
    print(f'using port  {port}')
    with open('port.txt', 'w') as f:
        f.write(str(port))
    return port

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = get_random_port()

# 绑定地址和端口
server_address = ('127.0.0.1', port)
server_socket.bind(server_address)

# 监听连接
client_num = 1
server_socket.listen(client_num)

# 用于存储客户端连接
client_sockets = []

client_sockets
while True:
    if len(client_sockets) < client_num:
        client_socket, client_address = server_socket.accept()
        client_sockets.append((client_socket, client_address))
        print(f"Accepted connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
        client_socket.send(f'Connection established: {time.strftime("%Y-%m-%d %H:%M:%S")}'.encode())
        continue
    # else:
    #     print('Client is full')
    # 循环等待接收客户端消息
    # while True:
    #     received_message = client_socket.recv(1024).decode()
    #     if received_message:
    #         print("Received from client:", received_message)
    #         client_socket.send(f"Message received {received_message}".encode())

