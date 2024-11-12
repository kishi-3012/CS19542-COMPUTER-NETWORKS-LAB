from socket import*
s=socket(AF_INET,SOCK_STREAM)
s.bind((&quot;&quot;,8000))
s.listen(5)
print(&quot;=================ChatApp================&quot;)
c,a=s.accept()
while True:
data=c.recv(100).decode()
print(&quot;&lt;--&quot;,data)
if (data==&quot;bye&quot; or &#39;&#39;):
p=&quot;bye&quot;
c.send(p.encode(&#39;utf-8&#39;))
print(&quot;Chat End&quot;)
break
msg=input(&quot;--&gt;&quot;,)
c.send(msg.encode(&#39;utf-8&#39;))