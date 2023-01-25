import socket

# Create a TCP socket
conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
conn_socket.connect(("192.168.56.103", 1234))

# Get temperature in Fahrenheit from user
temp_f = input("Enter temperature in Fahrenheit: ")

# Send the temperature to the server
conn_socket.send(temp_f.encode())

# Receive the converted temperature from the server
temp_c = conn_socket.recv(1024).decode()

# Display the temperature in Celsius
print("Temperature in Celsius: " + temp_c)

# Close the connection
conn_socket.close()
