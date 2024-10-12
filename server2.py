import socket
import threading

def handle_client(client_socket, addr):
    print(f"[SERVER 2] Accepted connection from {addr}")
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(f"[SERVER 2] Received: {message.decode('utf-8')} from {addr}")
        client_socket.send(f"ACK from Server 2".encode('utf-8'))
    client_socket.close()

def server_program(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[SERVER 2] Listening on port {port}")
    
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    server_program(8081)  # Port server 2 adalah 8081
