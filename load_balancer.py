import socket
import threading

# Daftar server (Server 1 pada port 8080 dan Server 2 pada port 8081)
servers = [('localhost', 8080), ('localhost', 8081)]
server_index = 0

def handle_client(client_socket):
    global server_index
    # Round-robin server selection
    server_address = servers[server_index]
    server_index = (server_index + 1) % len(servers)
    
    # Menghubungkan ke server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(server_address)
    
    # Menerima pesan dari client dan meneruskannya ke server
    message = client_socket.recv(1024)
    server_socket.send(message)
    
    # Menerima balasan dari server
    response = server_socket.recv(1024)
    
    # Mengirim balasan dari server ke client
    client_socket.send(response)
    
    # Tutup koneksi
    server_socket.close()
    client_socket.close()

def load_balancer_program(port):
    balancer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    balancer.bind(('0.0.0.0', port))
    balancer.listen(5)
    print(f"[LOAD BALANCER] Listening on port {port}")
    
    while True:
        client_socket, addr = balancer.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    # Load balancer akan berjalan pada port 8000
    load_balancer_program(8000)
