import socket

def parse_message(data):
    header, message = data.split(':', 1)
    return header, message

def generate_response(message):
    return f'TNE20003:A:{message}'

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific port
    server_port = 12345
    server_socket.bind((socket.gethostbyname(socket.gethostname()), server_port))

    print(f'Server is listening on port {server_port}...')

    while True:
        # Receive data from client
        data, client_address = server_socket.recvfrom(1024)
        data = data.decode('utf-8')
        
        # Parse the message
        try:
            header, message = parse_message(data)
            if header != 'TNE20003':
                raise ValueError('Invalid header')
            if not message:
                raise ValueError('Empty message')
            
            response = generate_response(message)
        except Exception as e:
            response = f'TNE20003:E:{str(e)}'

        # Send response back to client
        server_socket.sendto(response.encode('utf-8'), client_address)

if __name__ == '__main__':
    main()
