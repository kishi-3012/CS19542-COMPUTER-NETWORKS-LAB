from socket import*
s=socket(AF_INET,SOCK_STREAM)
s.connect((&quot;127.0.0.1&quot;,8000))
print(&quot;=========================ChatApp========================&quot;)
while True:
msg=input(&quot;--&gt;&quot;,)
s.send(msg.encode(&#39;utf-8&#39;))
data=s.recv(100).decode()
print(&quot;&lt;--&quot;,data)