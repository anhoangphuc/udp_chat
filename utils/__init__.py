import socket


class Transporter(object):
    '''
    Supply numerous methods for a UDP socket send and receive data
    '''
    def __init__(self, sock: socket.socket):
        self.sock = sock
