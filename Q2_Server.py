import socket

# Create a TCP socket
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
serv_socket.bind(("0.0.0.0", 1234))

# Listen for incoming connections
serv_socket.listen(5)

print("Server is still running...")

while True:
    # Accept a connection from a client
    cli_socket, addr = serv_socket.accept()
    print(f"\nSocket connected from the client {addr[0]}:{addr[1]}")

    #Receive temperature in Fahrenheit from client
    temp_f = cli_socket.recv(1024).decode()

    # Convert temperature to Celsius
    temp_c = (float(temp_f) - 32) * (5/9)
    print(f">Converting {temp_f} Fahrenheit into Celcius")

    # Send the converted temperature to the client
    cli_socket.send(str(temp_c).encode())
    print(">The temprature is sent......")

    # Close the connection
    cli_socket.close()
