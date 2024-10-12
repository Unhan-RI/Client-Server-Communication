import socket
import time
from log_manager import log_connection, log_message_sent, log_message_received

def send_message(message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8000))
    
    start_time = time.time()
    log_connection()  # Log waktu koneksi
    
    client.send(message.encode('utf-8'))
    log_message_sent(message)  # Log waktu pengiriman pesan
    
    # Menerima balasan dari server
    response = client.recv(1024)
    end_time = time.time()
    log_message_received(response.decode('utf-8'))  # Log waktu penerimaan balasan
    
    print(f"[CLIENT] Received: {response.decode('utf-8')}")
    
    # Waktu respon
    response_time = end_time - start_time
    print(f"Response time: {response_time:.6f} seconds")
    
    client.close()

if __name__ == "__main__":
    message = input("Enter the message to send: ")
    send_message(message)
