import random
import socket
import threading

# list of quotes
quotes = ["Life is like a camera, focus on the good times, develop from the negati>
          "The greatest glory in living lies not in never falling, but in rising e>
          "The power of imagination makes us infinite.",
          "The best way to predict the future is to create it."]

def handle_client(client_socket):
    """Handles a client connection"""
    request = client_socket.recv(1024)
    print(f"[*] Received: {request}")
    if request.decode().strip() == 'exit':
        client_socket.close()
        return
    # send a random quote
    quote = random.choice(quotes)
    client_socket.send(quote.encode())
    client_socket.close()

def start_server():
"""Starts the server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8888))
    server.listen(5)
    print(f"[*] Listening on 0.0.0.0:8888")
    
    while True:
        client, addr = server.accept()
        print(f"[*] Connection from {addr[0]}:{addr[1]}")
        
        # start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()

