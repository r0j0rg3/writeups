# What's your gender?
## Description
Solves: 12  Easy

I identify as Binary Packetsexual!

Can you look at this pcap file and help me find the flag?

Flag: RUSH{ALLCAPSMESSAGE}

## Files
1. What's your gender.pcap - A PCAP file

## Analysing
If we open the pcap file with wireshark we can see that all traffic is DNS and from 2 IP addresses, the "1.2.3.4" and the "192.168.0.1". All the traffic from the 1.2.3.4 is just noise, we can ignore it.

To have something to work with, I saved all the DNS a queries into a file with tshark
```bash
$ tshark -r What\'s\ your\ gender\ .pcap -Tfields -e dns.qry.name > names.txt
```
Now I cleaned all the dirty stuff from 1.2.3.4 and if we merge all the single chars we get this phrase: "well i think that this is quite a fun way for you to learn more about fake packet creation using python to get her wih scapy they can be quite powerful". So I suppose that the scapy python library could help me to solve the challenge

I obtained a text, but that wasn't the flag, after trying to see where it was (for example the packets lenght converted to ascii) I remember the description, it mentions the word "Binary", so I must be looking for a binary code, but where?

I was looking at whireshark when I saw that the source addres was always the same, but there was 4 different destinations:
1. 192.168.0.0
2. 192.168.0.1
3. 192.168.1.0
4. 192.168.1.1

We have it!

## Solve
To make the script, we must choose all the packets that are not noise, and write the last two octets on a string that will let us convert the binary code into ascii.
```python
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
# Now write this string on cybercheff and choose the "from binary" option
```
If we run it this is what we obtain:
```bash
$ python3 solve.py 
01010010 01010101 01010011 01001000 01111011 01010100 01001000 00110001 01010011 01010000 00110100 01000011 01001011 01000101 01010100 00110001 01010011 01000111 00110011 01001110 01000100 01000101 01010010 01001110 01000101 01010101 01010100 01010010 00110100 01001100 01111101
```
Now we just have to decode it "from binary" using [cybercheff](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDEwMTAwMTAgMDEwMTAxMDEgMDEwMTAwMTEgMDEwMDEwMDAgMDExMTEwMTEgMDEwMTAxMDAgMDEwMDEwMDAgMDAxMTAwMDEgMDEwMTAwMTEgMDEwMTAwMDAgMDAxMTAxMDAgMDEwMDAwMTEgMDEwMDEwMTEgMDEwMDAxMDEgMDEwMTAxMDAgMDAxMTAwMDEgMDEwMTAwMTEgMDEwMDAxMTEgMDAxMTAwMTEgMDEwMDExMTAgMDEwMDAxMDAgMDEwMDAxMDEgMDEwMTAwMTAgMDEwMDExMTAgMDEwMDAxMDEgMDEwMTAxMDEgMDEwMTAxMDAgMDEwMTAwMTAgMDAxMTAxMDAgMDEwMDExMDAgMDExMTExMDEg) and this will give us the flag :)

RUSH{TH1SP4CKET1SG3NDERNEUTR4L}
