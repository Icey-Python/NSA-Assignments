# Server
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 7999))
server_socket.listen(4) 

print("""<<<GLOBAL CHAT>>>>>""")

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Received {message} from client")
        message = input("Enter message to send: ")
        client_socket.send(message.encode())

while True:
    client_socket, address = server_socket.accept()
    print(f'Got connection from {address}')
    client_handler = threading.Thread(
        target=handle_client, args=(client_socket,))
    client_handler.start()

