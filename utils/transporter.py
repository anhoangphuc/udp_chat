import socket


class Transporter(object):
    '''
    Supply numerous methods for a UDP socket send and receive data
    '''
    PACKET_SIZE = 1024
    def __init__(self, sock: socket.socket):
        self.sock = sock

    def send_byte_stream(data: bytes):

