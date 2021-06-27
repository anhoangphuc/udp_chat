import socket


UDP_HOST = '127.0.0.1'
UDP_PORT = 5005
MESSAGE = b'Hello world'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_HOST, UDP_PORT))
data, addr = sock.recvfrom(1024)
print(data)