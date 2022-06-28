import usocket as socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = addr = socket.getaddrinfo('127.0.0.1:1880', 4445)[0][-1]

message = 'hello world'.encode()
s.sendto(message, addr)
print('message sent')

response = s.recv(1024)
print('Message received:', response)
