import sys
from socket import *
import time
start=time.time()
ECHO_PORT = 55555
BUFSIZE = 1024
host = &quot;172.16.8.101&quot;
addr = host, ECHO_PORT
s = socket(AF_INET, SOCK_DGRAM)
s.bind((&#39;&#39;, 0))
print (&#39;udp echo client ready, reading stdin&#39;)
while 1:
line = sys.stdin.readline()
if not line:

break
s.sendto(line.encode(), addr)
data, fromaddr = s.recvfrom(BUFSIZE)
print (&#39;client received %r from %r&#39; % (data, fromaddr))
end=time.time()
rtt=abs(start-end)
print(f&quot;RTT={rtt}&quot;)