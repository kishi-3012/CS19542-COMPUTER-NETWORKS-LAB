from scapy all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
def packet callback(packet):
if IP in packet:
ip_layer packet[IP]
protocol ip layer.proto
src_ip = ip_layer.src
dst_ipip layer.dst
#Determine the protocol
protocol name = ""
if protocol 1:
protocol name = "ICMP"
elif protocol 6:
protocol name = "TCP"
elif protocol=175
protocol name = "UDP"
else: protocol_name = "Unknown Protocol"
#Print packet details
print("Protocol: (protocol_name}")
print(f"Source IP: (src_ip}")
print(f Destination IP: (dst_ip)")
print("-"*50)
def main():
#Capture packets on the default network interface
sniff(iface-'Wi-Fi',prn-packet_callback, filter="ip", store-0)
if_name="main":
main()