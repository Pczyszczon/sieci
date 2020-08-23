#Autor: Paweł Czyszczoń
#email: 290425@uwr.edu.pl

import socket

class Mode:
    QUIT = 'QUIT'
    UPPER = 'UPPER'
    LOWER = 'LOWER'

ESCAPE_SYMBOLS = ('\r', '\n', '.', '\r', '\n')

HOST = 'localhost'
PORT = 50018
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

mode = None
conn = None
addr = None

while True:
    if not conn:
        conn, addr = s.accept()
        print('Connected by {}'.format(addr))
        modes_info = 'Aviable commands: {}, {}, {}'.format(Mode.QUIT, Mode.UPPER, Mode.LOWER).encode()
        conn.sendall(modes_info)
    else:
        data = conn.recv(1024).decode("utf-8")

        print('Received data: {}'.format(data))
        if data in [Mode.LOWER, Mode.UPPER, Mode.QUIT]: 
            mode = data
        else:
            conn.sendall('Try again'.encode())

        if mode == Mode.LOWER:
            conn.sendall('LOWER mode selected'.encode())
            while not data.endswith(ESCAPE_SYMBOLS):
                data = conn.recv(1024).decode("utf-8")
                conn.sendall(data.lower().encode())
            mode = None

        if mode == Mode.UPPER:
            conn.sendall('UPPER mode selected'.encode())
            while not data.endswith(ESCAPE_SYMBOLS):
                data = conn.recv(1024).decode("utf-8")
                conn.sendall(data.upper().encode())
            mode = None

        if mode == Mode.QUIT:
            conn.sendall('Bye'.encode())
            conn.close()
            mode = None
            conn = None
            addr = None
