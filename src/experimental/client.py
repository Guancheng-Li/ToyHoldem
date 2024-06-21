import socket
import threading
import time
import sys

def receive_messages(client_socket):
    first = True
    while True:
        if first:
            first = False
            message = client_socket.recv(1024).decode()
            if message:
                print("Received:", message)
            print('first')
            continue
        user_input = input("Enter your response (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        client_socket.send(user_input.encode())
        message = client_socket.recv(1024).decode()
        if message:
            print("Received:", message)

# 创建 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
port = None
with open('port.txt', 'r') as f:
    port = int(f.read())
print(f'Connecting port {port}...')
server_address = ('127.0.0.1', port)
print(server_address)
client_socket.connect(server_address)

# # 启动接收消息的线程
# receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
# receive_thread.start()

# 这里可以添加一些其他的逻辑，比如主线程的一些操作或者等待接收线程结束等

# 关闭连接
# client_socket.close()



def handle_server(server_socket):
    # 接收服务器消息的线程
    def receive():
        while True:
            try:
                message = server_socket.recv(1024).decode()
                if message:
                    print("Received from server:", message)
                else:
                    # 服务器关闭连接
                    server_socket.close()
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                server_socket.close()
                break

    # 发送消息给服务器的线程
    def send():
        while True:
            message = input("Enter message to send to server: ")
            server_socket.send(message.encode())

    # 启动接收和发送线程
    receive_thread = threading.Thread(target=receive)
    send_thread = threading.Thread(target=send)
    receive_thread.start()
    send_thread.start()

# 处理与服务器的通信
handle_server(client_socket)