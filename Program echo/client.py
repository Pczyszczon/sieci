import socket
import sys

def receive():
    data = s.recv(1024).decode("utf-8")
    print('Received: {}'.format(data))
    return data

def send():
    message = input().encode()
    print('Sending {}'.format(message))
    s.sendall(message)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 50018)
print('Connecting to {}'.format(server_address))
s.connect(server_address)

data = receive()

while not data == 'Bye':
    send()
    data = receive()

s.close()