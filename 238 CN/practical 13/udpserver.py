import sys
from socket import *
ECHO_PORT = 55555
BUFSIZE = 1024
s = socket(AF_INET, SOCK_DGRAM)
s.bind((&#39;&#39;, ECHO_PORT))
print (&#39;udp echo server ready&#39;)
while 1:
data, addr = s.recvfrom(BUFSIZE)
print( &#39;server received %r from %r&#39; % (data, addr))
s.sendto(data, addr)