import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.56.103", 8888))
client_socket.send("Hello Server".encode())

received_data = client_socket.recv(1024)
print(received_data.decode())
client_socket.close()

