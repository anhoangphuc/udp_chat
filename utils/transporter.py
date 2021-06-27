import socket
import math


class Transporter(object):
    '''
    Supply numerous methods for a UDP socket send and receive data
    '''
    PACKET_SIZE = 1024
    CHUNK_SIZE = PACKET_SIZE - 2     # Packet_size minus 2 for checksum byte
    TER_CHAR = '\xff'
    def __init__(self, sock: socket.socket):
        self.sock = sock

    def send_byte_stream(self, data: bytes, addr):
        # Add terminators characters
        data = data + Transporter.TER_CHAR.encode()
        number_of_chunks = len(data) - 1 / Transporter.CHUNK_SIZE + 1
        set_of_chunks = set(range(number_of_chunks))
        processed_chunk = {}

        # There are some chunks left
        while (len(set_of_chunks) > 0):
            ind = set_of_chunks.pop()
            if ind not in processed_chunk:
                processed_chunk[ind] = self._process(data[Transporter.CHUNK_SIZE * ind: 
                    min(Transporter.CHUNK_SIZE * (ind + 1), len(data))])
    
    def _process(self, chunk: bytes):
        '''
        Process chunk of data to send
        '''
        # First, calculate the checksum
        checksum = calculate_checksum(chunk)

    @staticmethod
    def calculate_checksum(chunk: bytes):
        '''
        Calculate checksum for a specific chunk of data
        '''
        # Add 0 padding to the right if len(chunk) is odd
        if len(chunk) % 2 != 0:
            chunk += b'0'
        checksum = 0
        for i in range(0, len(checksum), 2):
            w = (chunk[i] << 8) + chunk[i + 1]
            checksum += w
        
        checksum = (checksum >> 16) + (checksum & 0xFFFF)
        checksum =  ~checksum & 0xFFFF
        return checksum

