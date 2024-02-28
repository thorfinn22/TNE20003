import socket
import threading

def parse_message(data):
    header, message = data.split(':', 1)
    return header, message

def generate_response(message):
    return f'TNE20003:A:{message}'

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        
        data = data.decode('utf-8').strip()
        
        # Split data into individual messages using '\n' as a delimiter
        messages = data.split('\n')
        
        for message in messages:
            # Parse the message
            try:
                header, msg = parse_message(message)
                if header != 'TNE20003':
                    raise ValueError('Invalid header')
                if not msg:
                    raise ValueError('Empty message')
                
                response = generate_response(msg)
            except Exception as e:
                response = f'TNE20003:E:{str(e)}'
            
            # Send response back to the client
            client_socket.send(response.encode('utf-8') + b'\n')

    client_socket.close()

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = (socket.gethostbyname(socket.gethostname()), 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(5)
    print(f'Server is listening on {server_address[0]}:{server_address[1]}...')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
        
        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()
