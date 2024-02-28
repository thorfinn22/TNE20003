import socket
import re
import os
from urllib.parse import urlparse

def fetch_url(url):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    parsed_url = urlparse(url)
    server = parsed_url.netloc
    port = 80
    server_ip = socket.gethostbyname(server)
    s.connect((server_ip, port))

    request = f'GET {parsed_url.path} HTTP/1.0\r\nHost: {server}\r\n\r\n'
    s.send(request.encode())

    buffer_size = 4096
    response = b''
    while True:
        data = s.recv(buffer_size)
        if not data:
            break
        response += data

    s.close()
    return response

def extract_image_tags(html_content):
    img_tags = re.findall(r'<img .*?src=["\'](.*?)["\'].*?>', html_content)
    return img_tags

def download_images(img_tags, base_url, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for img_tag in img_tags:
        img_url = img_tag
        if not img_url.startswith('http'):
            img_url = base_url + img_url

        response = fetch_url(img_url)

        parsed_img_url = urlparse(img_url)
        img_filename = os.path.basename(parsed_img_url.path)

        # Construct the full path to save the image
        save_path = os.path.join(output_directory, img_filename)

        with open(save_path, 'wb') as img_file:
            img_file.write(response)

        print(f'Downloaded image: {img_filename} and saved to {save_path}')

if __name__ == "__main__":
    # Your existing code here...
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = 'www.google.com'
    port = 80
    server_ip = socket.gethostbyname(server)
    s.connect((server_ip, port))

    request = 'GET / HTTP/1.0\r\nHost: ' + server + '\r\n\r\n'
    s.send(request.encode())

    buffer_size = 4096
    response = b''
    while True:
        data = s.recv(buffer_size)
        if not data:
            break
        response += data

    s.close()

    response_str = response.decode('utf-8')
    response_lines = response_str.split('\r\n\r\n', 1)
    header_lines = response_lines[1:]
    header_dict = {}
    for line in header_lines:
        key, value = line.split(': ', 1)
        header_dict[key] = value

    response_code_line = response_lines[0].split(' ', 2)
    response_code = response_code_line[1]
    response_message = response_code_line[2]

    print(f'HTTP Response code ({response_code}) with message: {response_message}')

    print('Server HTTP Parameter Values:')
    for key, value in header_dict.items():
        print(f' {key.ljust(30)} : {value}')

    if response_code != '200':
        print(f'Error: HTTP Response Code {response_code}')
    else:
        html_content = response_lines[1]
        img_tags = extract_image_tags(html_content)

        # Specify the output directory to save images
        output_directory = 'images'
        download_images(img_tags, 'http://www.google.com', output_directory)
