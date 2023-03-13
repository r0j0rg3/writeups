from scapy.all import *

packets = rdpcap("./What's your gender .pcap")

count=0
string=""

for packet in packets:
    if(packet[IP].src!="1.2.3.4"):
        string+=packet[IP].dst[-3]+packet[IP].dst[-1]
        count+=1
        if(count%4==0):
            string+=" "

print(string)
# Now write this string on cybercheff and choose the "from binary" option:
# https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDEwMTAwMTAgMDEwMTAxMDEgMDEwMTAwMTEgMDEwMDEwMDAgMDExMTEwMTEgMDEwMTAxMDAgMDEwMDEwMDAgMDAxMTAwMDEgMDEwMTAwMTEgMDEwMTAwMDAgMDAxMTAxMDAgMDEwMDAwMTEgMDEwMDEwMTEgMDEwMDAxMDEgMDEwMTAxMDAgMDAxMTAwMDEgMDEwMTAwMTEgMDEwMDAxMTEgMDAxMTAwMTEgMDEwMDExMTAgMDEwMDAxMDAgMDEwMDAxMDEgMDEwMTAwMTAgMDEwMDExMTAgMDEwMDAxMDEgMDEwMTAxMDEgMDEwMTAxMDAgMDEwMTAwMTAgMDAxMTAxMDAgMDEwMDExMDAgMDExMTExMDEg
