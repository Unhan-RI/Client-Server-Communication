import threading
import time
import client

def run_client_instances(num_clients, message):
    threads = []
    for _ in range(num_clients):
        thread = threading.Thread(target=client.send_message, args=(message,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    num_clients = int(input("Enter the number of clients: "))
    message = input("Enter the message to send: ")
    
    start_time = time.time()
    run_client_instances(num_clients, message)
    end_time = time.time()
    
    total_time = end_time - start_time
    print(f"Total time for {num_clients} clients: {total_time:.6f} seconds")
    print(f"Throughput: {num_clients / total_time:.6f} clients/second")
10