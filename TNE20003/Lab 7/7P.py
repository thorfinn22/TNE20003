import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server = 'www.google.com'
port = 80
server_ip = socket.gethostbyname(server)
s.connect((server_ip, port))

# Construct the HTTP request string
request = 'GET / HTTP/1.0\r\nHost: ' + server + '\r\n\r\n'
s.send(request.encode())

# Receive the response
buffer_size = 4096
response = b''
while True:
    data = s.recv(buffer_size)
    if not data:
        break
    response += data

# Close the connection
s.close()

# Print the response
print(response.decode())
