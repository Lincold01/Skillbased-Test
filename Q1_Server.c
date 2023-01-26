#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_address, client_address;
    int server_address_length = sizeof(server_address);
    int client_address_length = sizeof(client_address);

    // Create server socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        printf("Error creating server socket\n");
        return 1;
    }

    // Bind server socket to local address and port
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = INADDR_ANY;
    server_address.sin_port = htons(1234);
    if (bind(server_socket, (struct sockaddr *) &server_address, server_address>
        printf("Error binding server socket\n");
        return 1;
    }

    // Listen for incoming connections
    listen(server_socket, 5);

    while (1) {
        // Accept incoming connection
        client_socket = accept(server_socket, (struct sockaddr *) &client_addre>
        if (client_socket < 0) {
            printf("Connection error\n");
            return 1;
        }

        // Generate random number between 100 and 999
        int random_num = rand() % 900 + 100;

        // Send random number to client
        send(client_socket, &random_num, sizeof(random_num), 0);
        printf("Random number sent to client\n");

        // Close client socket
        close(client_socket);
    }

    // Close server socket
    close(server_socket);
    return 0;
}
