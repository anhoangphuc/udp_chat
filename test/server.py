import socket

UDP_HOST = "127.0.0.1"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_HOST, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024)
    print(f'Server received message from {addr}')
    print(f'received message {data}')
    sock.sendto(data, addr)