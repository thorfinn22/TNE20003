import socket

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server address (replace SERVER_IP and SERVER_PORT)
    server_address = (socket.gethostbyname(socket.gethostname()), 12345)

    # Prepare at least two messages
    messages = [
        'TNE20003:Hello Leo!',
        'TNE20003:Harry Wo',
        'Sadia',
        ''
    ]

    for message in messages:
        # Send the message to the server
        client_socket.sendto(message.encode('utf-8'), server_address)

        # Receive the response from the server
        response, server_address = client_socket.recvfrom(1024)
        response = response.decode('utf-8')

        # Print the server's response
        print(f'Server Response: {response}')

if __name__ == '__main__':
    main()
