import socket

def main():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address
    server_address = (socket.gethostbyname(socket.gethostname()), 12345)

    try:
        # Connect to the server
        client_socket.connect(server_address)

        # Prepare at least two messages
        messages = [
            'TNE20003:Hello Leo!',
            'TNE20003:Harry Wo',
            'Sadia',
            ''
        ]

        for message in messages:
            # Send the message to the server
            client_socket.send((message + '\n').encode('utf-8'))

            # Receive the response from the server
            response = client_socket.recv(1024)
            response = response.decode('utf-8').strip()

            # Print the server's response
            print(f'Server Response: {response}')

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    main()
