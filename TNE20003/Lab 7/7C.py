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

# Decode the response
response_str = response.decode('utf-8')

# Split the response into HTTP header and HTML content
header, html_content = response_str.split('\r\n\r\n', 1)

# Parse and display HTTP response code and message
response_lines = header.split('\r\n', 1)
response_code_line = response_lines[0].split(' ', 2)
response_code = response_code_line[1]
response_message = response_code_line[2]
print(f'HTTP Response code ({response_code}) with message: {response_message}')

# Parse and display HTTP headers
header_lines = response_lines[1:]
header_dict = {}
for line in header_lines:
    key, value = line.split(': ', 1)
    header_dict[key] = value
print('Server HTTP Parameter Values:')
for key, value in header_dict.items():
    print(f' {key.ljust(30)} : {value}')

# If the HTTP response is NOT 200, display an error message
if response_code != '200':
    print(f'Error: HTTP Response Code {response_code}')
else:
    # Print the HTML content
    print('Downloaded Web Page contents:')
    print(html_content)
