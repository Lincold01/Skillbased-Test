#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
    int client_socket;
    struct sockaddr_in server_address;

    // Create client socket
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket < 0) {
        printf("Error creating client socket\n");
        return 1;
    }

    // Connect to server
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = inet_addr("192.168.56.103");
    server_address.sin_port = htons(1234);
    if (connect(client_socket, (struct sockaddr *) &server_address, sizeof(serv>
        printf("Error connecting to server\n");
        return 1;
    }

    // Receive random number from server
    int random_num;
    recv(client_socket, &random_num, sizeof(random_num), 0);

    // Display received random number
    printf("Received random number: %d\n", random_num);

    // Close client socket
    close(client_socket);
    return 0;

}
