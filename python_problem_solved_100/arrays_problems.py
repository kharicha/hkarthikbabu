'''
This contains all the array challenges with multiple possible algorithms each
'''

'''
1, Implement an algorithm to determine if a string has all unique characters.
Test Cases
None -> False
'' -> True
'foo' -> False
'bar' -> True
'''

# My OWN Brute force

# def st(s):
#     n = ''
#     if s is None:
#         return False
#     elif s is '':
#         return True
#     else:
#         for c in s:
#             if c in n:
#                 return False
#             else:
#                 n += c
#         return True
#
# print(st("foo"))
# print(st("bar"))
# print(st(""))

#Algorithm 1: Sets and Length Comparison

# def st(s):
#     if s is None:
#         return False
#     return len(set(s)) == len(s)
#
# print(st("foo"))
# print(st("bar"))
# print(st(""))

#Algorithm 2: Hash Map Lookup

# def st(s):
#     d = dict()
#     if s is None:
#         return False
#     else:
#         for c in s:
#             if c in d:
#                 return False
#             else:
#                 d[c] = 1
#         return True
#
# print(st("foo"))
# print(st("bar"))
# print(st(""))

'''
2, Determine if a string is a permutation of another string.¶
One or more None inputs -> False
One or more empty strings -> False
'Nib', 'bin' -> False
'act', 'cat' -> True
'a ct', 'ca t' -> True
'dog', 'doggo' -> False
'''

# def st(s1, s2):
#     d = {}
#     if s1 is None and s2 is None:
#         return False
#     elif s1 is None or s2 is None:
#         return False
#     elif s1 is "" or s2 is '':
#         return False
#     else:
#         for c in s1:
#             if c in s2:
#                 continue
#             else:
#                 return False
#         return True
#
#
# print(st('Nib','bin'))
# print(st('act','cat'))
# print(st('a ct','ca t'))
#

#Algorithm: Compare Sorted Strings¶

# def st(s1, s2):
#     if s1 is None or s2 is None:
#         return False
#     else:
#         return sorted(s1) == sorted(s2)
#
# print(st('Nib','bin'))
# print(st('act','cat'))
# print(st('a ct','ca t'))
# print(st('dog','doggo'))

'''
3, Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring.¶

Any strings that differ in size -> False
None, 'foo' -> False (any None results in False)
' ', 'foo' -> False
' ', ' ' -> True
'foobarbaz', 'barbazfoo' -> True
'''

# class Rotation(object):
#     def is_substring(self, s1, s2):
#         return s1 in s2
#
#     def st(self, s1,s2):
#         if len(s1) != len(s2):
#             return False
#         elif s1 is None or s2 is None:
#             return False
#         elif s1 is '' and s2 is not None:
#             return False
#         elif s1 is '' and s2 is '':
#             return True
#         else:
#             return self.is_substring(s1, s2 + s2)
#
# s = Rotation()
# print(s.st('barbazfoo','foobarbaz'))
# print(s.st('foobarbaz','barbazfoobarbazfoo'))

'''
4, Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. 
None -> None
'' -> ''
'AABBCC' -> 'AABBCC'
'AAABCCDDDD' -> 'A3BC2D4'
'''
############ TBD

'''
5, Implement a function to reverse a string (a list of characters), in-place.
None -> None
[''] -> ['']
['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']
'''

# class ReverseString(object):
#
#     def reverse(self, chars):
#         if chars:
#             size = len(chars)
#             for i in range(size // 2):
#                 chars[i], chars[size - 1 - i] = \
#                     chars[size - 1 - i], chars[i]
#         return chars

#NEW

'''
# Q - Find a number in the array such that all the elements
# in the array are divisible by it
'''

# p1 = re.compile(r'.*active(\s+)(?P<port1>(\S+).{1}).*’)
#
# p1 = re.compile(r'.*active(\s+)(?P<port1>(\S+)).*(?P<port2>(\S+)).*')

'''
Python program to print a list of possible ipv4 addresses from a given CIDR
'''

import ipaddress

# Splitting the obtained IP with dot and verifying each part is an integer between 0-255
# def validate_ip(s):
#     a = s.split('.')
#     if len(a) != 4:
#         return False
#     for x in a:
#         if not x.isdigit():
#             return False
#         i = int(x)
#         if i < 0 or i > 255:
#             return False
#     return True
#
# # Verifying whether the received mask is valid
# def validate_mask(s):
#     if (len(s) < 0 and len(s) > 2):
#         return False
#     if not s.isdigit():
#         return False
#     i = int(s)
#     if i < 0 or i > 32:
#         return False
#     return True
#
# # Receiving the input from the user
# subnet = input("Enter your subnet: ")
#
# # Verifying the received input is valid or not
# (ipv4, mask) = subnet.split('/')
# valid_ipv4 = validate_ip(ipv4)
# valid_mask = validate_mask(mask)
#
# # if the received input is valid print all the possible ip address
# if valid_ipv4 and valid_mask:
#     print ([str(ip) for ip in ipaddress.IPv4Network(subnet)])
# # Declare the received input is invalid
# elif valid_ipv4 and not valid_mask:
#     print("In the given subnet  - mask %s is not valid" %mask)
# elif valid_mask and not valid_ipv4:
#     print("In the given subnet  - ipv4 address %s is not valid" % ipv4)
# else:
#     print("In the given subnet both ipv4 address %s and mask %s is not valid" % (ipv4, mask))
#
#
#
#
#
#


# vlan : 100
# ip add : 1.1.1.1
# ipv6 add: 2001:db8:0:1::/64
# mask: 24
# int name: gig1/0
#
#
#
#
# vlan : 200
# ip add : 1.1.1.1
# ipv6 add: 2001:db8:0:2::/64
# mask: 24
# int name: gig2/0

# from _collections import defaultdict
#
# lst = [('input1', 'vlan:100'), ('input2', 'vlan:200'), ('input1', 'ip add : 1.1.1.1'),('input2', 'ip add : 1.1.1.2'), ('input1', 'ip add : 1.1.1.3') ]
# d = defaultdict(list)
#
# for key, val in lst:
#     d[key].append(val)
#
# print(d['input1'])

# {'input1': [vlan:100], 'input2': [vlan:200]}

# def ipRange(s_ip, e_ip):
#     start = list(map(int, s_ip.split('.')))
#     end = list(map(int, e_ip.split('.')))
#
#     t = start
#     ips = []
#
#     ips.append(s_ip)
#     while t != end:
#         start[3] += 1
#         for i in (3, 2, 1):
#             if t[i] == 256:
#                 t[i] = 0
#                 t[i-1] += 1
#         ips.append(".".join(map(str, t)))
#     return ips
#
# ip_range = ipRange("192.168.1.0", "192.171.1.0")
# for ip in ip_range:
#     print(ip)




'''
Problem-2:

OSPF DR/BDR selection problem:
For a given network setup, Find the DR and BDR routers.
The DR and BDR are selected in the following way:

1. Choose the highest OSPF priority
2. Choose the highest router-id
3. Choose the highest loopback interface
4. Choose the highest configured physical interface

Input would be a dict with all required information:
[
{“Name”: “R1P1”, “ospf-priority”: 10, “router-id”: “10.10.1.1”, “loopback”: “11.11.11.11”, “intf”: “eth0”},
{“Name”: “R2P1”, “ospf-priority”: 2, “router-id”: “11.11.1.1”, “loopback”: “1.1.11.11”, “intf”: “eth1” },
{“Name”: “R3P1”, “ospf-priority”: 1, “router-id”: “1.1.1.1”, “loopback”: “11.11.11.11”, “intf”: “eth2” }
]
Output would be: The DR and BDR selected from the list
Please note the following: 
 1. You need to validate the input before analysis.
 2. You need to ensure that all negative cases are covered. 
 3. You can use standard python sort methods. 
 4. Run time for the script would be of utmost importance
'''
# import ipaddress
#
# #Splitting the obtained IP with dot and verifying each part is an integer between 0-255
# def valid_ip(s):
#     a = s.split('.')
#     if len(a) != 4:
#         return False
#     for x in a:
#         if not x.isdigit():
#             return False
#         i = int(x)
#         if i < 0 or i > 255:
#             return False
#     return True
#
# # Initializing list of dictionaries with given input of the network setup
# lis = [{"name": "R1P1", "ospf-priority": 10, "router-id": "10.10.1.1", "loopback": "11.11.11.11", "intf": "eth0"},
#        {"name": "R2P1", "ospf-priority": 2, "router-id": "11.11.1.1", "loopback": "1.1.11.11", "intf": "eth1"},
#        {"name": "R3P1", "ospf-priority": 1, "router-id": "1.1.1.1", "loopback": "11.11.11.11", "intf": "eth2"}]
#
# # Validate the given input and append it to the new list only when all the input values are valid
# valid_lis = []
# for l in lis:
#     if ('ospf-priority' in l.keys() and 'router-id' in l.keys() and 'loopback' in l.keys() and 'intf' in l.keys()):
#         if (int(l['ospf-priority']) >= 0 and int(l['ospf-priority'] < 256) and valid_ip(l['router-id']) and valid_ip(l['loopback'])):
#             valid_lis.append(l)
#
# print('Valid Input Values:')
# print(valid_lis)
# print('\r')
# # Sort the valid input in the order - highest OSPF Priority if they are equal - highest router-id if they are equal -
# # highest loopback ip if they are equal highest physical interface
# kar = (sorted(valid_lis, key=lambda i: (i['ospf-priority'],i['router-id'],i['loopback'],i['intf']), reverse=True))
#
# # From the sorted list - Print the first value as DR and second value as BDR
# count = 0
# for i in kar:
#     if count == 0:
#         print("The DR selected from the given list is  %s"%i)
#         count += 1
#     elif count == 1:
#         print("The BDR selected from the given list is %s" % i)
#         count += 1







# using sorted and lambda to print list sorted
# by age
# print ('The list printed sorting by age: ')
# kar = (sorted(lis, key=lambda i: (i['ospf-priority'],i['router-id'],i['loopback'],i['intf']), reverse=True))
#
# count = 0
# for i in kar:
#     if count == 0:
#         print("The DR selected from the given list is %s"%i)
#         count += 1
#     elif count == 1:
#         print("The BDR selected from the given list is %s" % i)
#         count += 1

# '''
# Problem - 1
#
# IP address range: Write a program which takes in two inputs, starting-vlan and number-of-vlans from
# the user and outputs a range of ipv4 and ipv6 addresses which has a set association with the vlan-id.
# You can have the predefined mapping. Based on inputs given from user as above, fetch the values
# and return the output. Also, demonstrate your solution with a good scale.
#
# For example : input number-of-vlans = 100, and starting-vlan = 100. Output we should get a list of ipv4 and ipv6 addresses.
# '''
#
# # Generate vlan (1 - 4094) and for each vlan generate an ipv4/ipv6 address and associate it with the vlan
# vlan = 1
# d = dict()
# for i in range(1,18):
#     for j in range(1,255):
#         d[vlan] = []
#         d[vlan] = ['10.1.{}.{}'.format(str(i), str(j)), '2002:{}::{}'.format(str(i), str(j))]
#         if (vlan == 4094):
#             break
#         vlan += 1
#
# # Get the User input - number of vlans/starting vlan number
# # Verify the user input received for both the values within the vlan range (1-4094)
#
# while True:
#    try:
#        num = int(input("Enter total number-of-vlans : "))
#    except ValueError: # just catch the exceptions you know!
#        print ('That\'s not a number!')
#    else:
#        if 1 <= num <= 4094: # this is faster
#            break
#        else:
#            print('Out of vlan (1-4094) range. Try again')
#
# while True:
#    try:
#        sta = int(input("Enter the starting-vlan     : "))
#    except ValueError: # just catch the exceptions you know!
#        print ('That\'s not a number!')
#    else:
#        if 1 <= sta <= 4094: # this is faster
#            break
#        else:
#            print('Out of vlan (1-4094) range. Try again')
#
# # Based on the input fetch the ipv4/ipv6v address associated with the each vlan in the user input range
# print('\r')
# print("Total Number of VLAN Data needs to be displayed: {}".format(str(num)))
# print("Starting to display Vlan Data from this given VLAN: {}".format(str(sta)))
# print('\r')
#
# for i in range(sta, sta+num):
#     print ('VLAN {} - IPv4/IPv6 - {}'.format(str(i), d[i]))
#

'''
Problem-3:

Packet Capture Utility:
Write a program which will take the following inputs from the user:
    a. Port to capture packets at
    b. Type of packet to be captured (L2, L3, IPv4/v6, TCP etc). You can add as many options here as required.
    c. output should be presented as.
        A: a running table displayed in the shell with a set header.
        sr. srcMac dstMac SrcIP etc etc
        “1”. 11:11:11:11:00:00 11:11:11:11:00:00 1.2.3.4 .....
    d. On doing a ctrl+c (sigkill), the script should display the stats on the total number of packets captures in the run.

As a pointer, please take a look at the following python module. https://scapy.net
'''
# from scapy.all import *
# import socket
# import datetime
# import os
# import time
# from signal import signal, SIGINT
# from sys import exit
#
# # Capture the total packet counts number
# in_count = 0
# out_count = 0
# sr_count = 0
# fil = ''
#
# # Verify and check the user input for the port and the traffic type to be captured
# while True:
#     try:
#         por = raw_input("Enter the port to capture : ")
#     except ValueError:  # just catch the exceptions!
#         print('That\'s not a valid string!')
#     else:
#         # Match the obtained string for at least one letter, at least one digit and no spaces
#         if (re.match('\S*(\S*([a-zA-Z]\S*[0-9])|([0-9]\S*[a-zA-Z]))\S*', por)):
#             break
#         else:
#             print('Please enter a valid port name eg; eth0. Try again')
#
# while True:
#     try:
#         typ = raw_input("Enter the type of packet to capture : ")
#     except ValueError:  # just catch the exceptions!
#         print('That\'s not a valid string!')
#     else:
#         if typ == 'l2' or typ == 'l3' or typ == 'arp' or \
#                 typ == 'tcp' or typ == 'udp' or typ == 'ipv6' or \
#                 typ == 'icmp':
#             break
#         else:
#             print('Please enter a valid traffic types, valid types are l2/l3/icmp/arp/tcp/udp/ipv6. Try again')
#
# # Process the packet capture
# def process_packet(pkt):
#     global in_count
#     global out_count
#     global sr_count
#     time = datetime.datetime.now()
#
#     # classifying packets into TCP
#     if pkt.haslayer(TCP):
#         if typ.upper() == 'TCP':
#             if socket.gethostbyname(socket.gethostname()) == pkt[IP].dst:
#                 print(str("[") + str(time) + str("]") + "  " + "TCP-IN:{}".format(
#                     len(pkt[TCP])) + " Bytes" + "    " + "SRC-MAC:" + str(pkt.src) + "    " + "DST-MAC:" + str(
#                     pkt.dst) + "    " + "SRC-PORT:" + str(pkt.sport) + "    " + "DST-PORT:" + str(
#                     pkt.dport) + "    " + "SRC-IP:" + str(pkt[IP].src) + "    " + "DST-IP:" + str(
#                     pkt[IP].dst) + "  ")
#                 in_count += 1
#
#             if socket.gethostbyname(socket.gethostname()) == pkt[IP].src:
#                 print(str("[") + str(time) + str("]") + "  " + "TCP-OUT:{}".format(
#                     len(pkt[TCP])) + " Bytes" + "    " + "SRC-MAC:" + str(pkt.src) + "    " + "DST-MAC:" + str(
#                     pkt.dst) + "    " + "SRC-PORT:" + str(pkt.sport) + "    " + "DST-PORT:" + str(
#                     pkt.dport) + "    " + "SRC-IP:" + str(pkt[IP].src) + "    " + "DST-IP:" + str(
#                     pkt[IP].dst) + "  ")
#                 out_count += 1
#
#     # classifying packets into UDP
#     if pkt.haslayer(UDP):
#         if typ.upper() == 'UDP':
#             print(str("[") + str(time) + str("]") + "  " + "UDP:{}".format(
#                 len(pkt[UDP])) + " Bytes " + "    " + "SRC-MAC:" + str(pkt.src) + "    " + "DST-MAC:" + str(
#                 pkt.dst) + "    " + "SRC-PORT:" + str(pkt.sport) + "    " + "DST-PORT:" + str(
#                 pkt.dport) + "    " + "SRC-IP:" + str(pkt[IP].src) + "    " + "DST-IP:" + str(
#                 pkt[IP].dst) + "  ")
#             in_count += 1
#
#     # classifying packets into ICMP
#     if pkt.haslayer(ICMP):
#         if typ.upper() == 'ICMP':
#             # classyfying packets into ICMP Incoming packets
#             if socket.gethostbyname(socket.gethostname()) == pkt[IP].src:
#                 print(str("[") + str(time) + str("]") + "  " + "ICMP-OUT:{}".format(
#                     len(pkt[ICMP])) + " Bytes" + "    " + "IP-Version:" + str(
#                     pkt[IP].version) + "    " * 1 + " SRC-MAC:" + str(pkt.src) + "    " + "DST-MAC:" + str(
#                     pkt.dst) + "    " + "SRC-IP: " + str(pkt[IP].src) + "    " + "DST-IP:  " + str(
#                     pkt[IP].dst) + "  ")
#                 in_count += 1
#
#             if socket.gethostbyname(socket.gethostname()) == pkt[IP].dst:
#                 print(str("[") + str(time) + str("]") + "  " + "ICMP-IN:{}".format(
#                     len(pkt[ICMP])) + " Bytes" + "    " + "IP-Version:" + str(
#                     pkt[IP].version) + "    " * 1 + "	 SRC-MAC:" + str(pkt.src) + "    " + "DST-MAC:" + str(
#                     pkt.dst) + "    " + "SRC-IP: " + str(pkt[IP].src) + "    " + "DST-IP:  " + str(
#                     pkt[IP].dst) + "  ")
#                 out_count += 1
#
#                 # classifying packets into IPv6
#         if IPv6 in pkt:
#             if typ.upper() == 'IPV6':
#                 print(str("[") + str(time) + str("]") + "  " + "IPv6:{}".format(
#                     len(pkt[IPv6])) + " Bytes" + "    " + "IP-Version:" + str(
#                     pkt[IPv6].version) + "    " * 1 + " SRC-MAC:" + str(pkt.src) + "    " + "DST-MAC:" + str(
#                     pkt.dst) + "    " + "SRC-IP: " + str(pkt[IPv6].src) + "    " + "DST-IP:  " + str(
#                     pkt[IPv6].dst) + "  ")
#                 in_count += 1
#
#         # classifying packets into ARP
#         if pkt.haslayer(ARP):
#             if typ.upper() == 'ARP':
#                 if pkt[ARP].op == 1:  # who-has (request)
#                     print(str("[") + str(time) + str("]") + "  " + "ARP Request:" + str(
#                         pkt[ARP].psrc) + "is asking about" + str(pkt[ARP].pdst))
#                     in_count += 1
#                 if pkt[ARP].op == 2:  # is-at (response)
#                     print(str("[") + str(time) + str("]") + "  " + "ARP Request:" + str(
#                         pkt[ARP].hwsrc) + "is asking about" + str(pkt[ARP].psrc))
#                     out_count += 1
#
#         # classifying packets into L3
#         if pkt.haslayer(IP):
#             if typ.upper() == 'L3':
#                 sr_count += 1
#                 print(str("[") + str(time) + str("]") + "  " + "L2-ETHER:{}".format(
#                     len(pkt[Ether])) + " Bytes" + "    " + " SR " + str(sr_count) + "    " + "SRC-IP: " + str(
#                     pkt[IP].src) + "    " + "DST-IP:  " + str(pkt[IP].dst) + "  ")
#                 in_count += 1
#
#         # classifying packets into L2
#         if pkt.haslayer(Ether):
#             if typ.upper() == 'L2':
#                 sr_count += 1
#                 print(str("[") + str(time) + str("]") + "  " + "L2-ETHER:{}".format(
#                     len(pkt[Ether])) + " Bytes" + "    " + " SR " + str(sr_count) + "    " + " SRC-MAC:" + str(
#                     pkt.src) + "    " + "DST-MAC:" + str(
#                     pkt.dst) + "    ")
#                 in_count += 1
#
#
# # Handle the CTRL + C
# def handler(signal_received, frame):
#     # Handle any cleanup here
#     print('SIGINT or CTRL-C detected. Exiting gracefully')
#     print('Packet capture is exiting now\n')
#     print('Packet Type {} - Captured IN PKTS - {} Captured OUT PKTS - {}'.format(typ.upper(), in_count, out_count))
#     exit(0)
#
#
# # MAIN
# if __name__ == '__main__':
#     # Tell Python to run the handler() function when SIGINT is recieved
#     signal(SIGINT, handler)
#     # Capture the packet
#     if typ.upper() == 'TCP':
#         fil = 'port 80'
#     elif typ.upper() == 'ICMP' or typ.upper() == 'L2' or typ.upper() == 'L3':
#         fil = 'icmp'
#     elif typ.upper() == 'UDP':
#         fil = 'udp'
#     elif typ.upper() == 'IPV6':
#         fil = 'ip6'
#     elif typ.upper() == 'ARP':
#         fil = 'arp'
#
#     sniff(filter=fil, prn=process_packet, iface=por, store=False)
#
#     while True:
#         # Do nothing and capture forever until SIGINT received.
#         pass
#
# def bitExtracted(number, k, p):
#     return (((1 << k) -1) & (number >> (p -1)))


# def bitExtracted(num, k, p):
#     # # convert number into binary first
    # print(num)
    # binary = bin(num)
    # print(binary)
    #
    # # remove first two characters
    # binary = binary[2:]
    # print(binary)
    #
    # end = len(binary) - p
    # print(end)
    # start = end - k + 1
    # print(start)
    #
    # # extract k  bit sub-string
    # kBitSubStr = binary[start: end + 1]
    # print(kBitSubStr)
    #
    # # convert extracted sub-string into decimal again
    # print(int(kBitSubStr, 2))
    # return(int(kBitSubStr, 2))

#     binary = bin(number)
#     binary = binary[2:]
#
#     end = len(binary) - p
#     start = end - k + 1
#
#     new = binary[start: end+1]
#     return (int(new,2))
#
#
#
# number = 72
# k = 5
# p = 1
# print("The extracted number is ", bitExtracted(number, k, p))



# def isPalindrome(string):
#     # Write your code here.
#     # reversestring = ''
#     # for ch in reversed(range(len(string))):
#     #     print(ch)
#     #     reversestring += string[ch]
#     # return string == reversestring
#
#     left = 0
#     right = len(string)-1
#     print(left)
#     print(right)
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
# def isPalindrome(string):
#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             ss = string[i: j+1]
#             print(ss)
#
#
#
#
# string = 'abaxyzzyxf'
# print(isPalindrome(string))





# import sys
# print(sys.version)

#
# S = "bad is good"
#
# s = S.split(" ")
# print(s)
# f = ""
# for c in s:
#     f += c[0]
# print(f)

# def removeKthNodeFromEnd(head, k):
#     # Write your code here.
#     first = head
#     second = head
#     count = 1
#
#     while count <= 4:
#         second = second.next
#         count += 1
#
#     if second is None:
#         head.value = head.next.value
#         head.next = head.next.next
#         return
#
#     while second.next is not None:
#         second = second.next
#         first = first.next
#
#     first.next = first.next.next
#     return head
#
# print(removeKthNodeFromEnd(0, ))


# def maximizeMoney(n, k):
#     for i in range(1, n,):
#         print(i)
#         if i%2:
#             return (n/2)*k
#         else:
#             return (n/2+1)*k
#
#
# n = 10
# k= 1000
# print(maximizeMoney(n, k))

# def fiundlopp(head):
#     first = head.next
#     second = head.next.next
#
#     while first != second:
#         first = first.next
#         second = second.next.next
#     first = head
#     while head != second:
#         first = first.next
#         second = second.next
#     return first

# def revll(string):
#     pn = None
#     cn = head
#
#     while cn is not None:
#         nn = cn.next
#         cn.next = pn
#         pn = cn
#         cn = nn
#     return pn


# def bs(array):
#     isSorted = False
#     count = 0
#     while not isSorted:
#         isSorted = True
#         for i in range(len(array) -1 - count):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#                 isSorted = False
#         count += 1
#     return array

# def iso(array):
#     for i in range(1, len(array)):
#         j = i
#         while j > 0 and array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#             j -= 1
#     return array

# def ss(array):
#     ci = 0
#     while ci < len(array) -1:
#         si = ci
#         for i in range(ci+1, len(array)):
#             if array[si] > array[i]:
#                 si = i
#         array[ci], array[si] = array[si], array[ci]
#         ci += 1
#     return array
#
#
# print(ss([8, 3, 9, 5, 4, 7, 5]))


# class Item():
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#
# class hm():
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _  in range(self.size)]
#
#     def hash_value(self, key):
#         return key % self.size
#
#     def set(self, key, value):
#         hash_index = self.hash_value(key)
#         for item in self.table[hash_index]:
#             if item.key == key:
#                 item.value = value
#         self.table[hash_index].append(item(key, value))
#
#     def get(self, key):
#         hash_index = self.hash_value(key)
#         for item in self.table[hash_index]:
#             if item.key == key:
#                 return item.value
#         raise KeyError()
#
#     def remove(self,key):
#         hash_index = self.hash_value(key)
#         for index, item in enumerate(self.table[hash_index]):
#             if item.key == key:
#                 del self.table[hash_index][index]
#                 return
#             raise KeyError('Key not found')
#
#


# n = 13
# if n > 1:
#     for i in range(2, n):
#         if n%i == 0:
#             print('{} is not a prime'.format(n))
#             break
#     else:
#         print('{} is a PRIME'.format(n))
# else:
#     print('{} is not a prime'.format(n))

'''
Given list of ints, return True if any two nums sum to 0.
    >>> add_to_zero([])
    False
    >>> add_to_zero([1])
    False
    >>> add_to_zero([1, 2, 3])
    False
    >>> add_to_zero([1, 2, 3, -2])
    True
'''

# def add_to_zero(nums):
#     if len(nums) < 2:
#         return False
#
#     for i in range(len(nums) -1):
#         fn = nums[i]
#         for j in range(i+1, len(nums)):
#             sn = nums[j]
#             if fn + sn == 0:
#                 return True
#     return False

# def add_to_zero(nums):
#     if len(nums) < 2:
#         return False
#     num_set = set(nums)
#     print(num_set)
#
#     for num in nums:
#         print(num)
#         if -num in num_set:
#             return True
#     return False
#
# print(add_to_zero([1,2,3,-2]))

'''
Using recursion, return the sum of numbers in a list.
    >>> sum_list([5, 5])
    10
    >>> sum_list([-5, 10, 4])
    9
    >>> sum_list([20])
    20
    >>> sum_list([])
    0
'''
# def sum_list(nums):
#
#     if not nums:
#         return 0
#     return nums[0] + sum_list(nums[1:])

# def sum_list(nums):
#
#     num = 0
#     if not nums:
#         return 0
#     for num in nums:
#         num += num
#     return num
#
# print(sum_list([5, 5]))

'''
 >>> rev_str('hello')
    'olleh'
    >>> rev_str('1234h')
    'h4321'
    >>> rev_str('')
    ''
'''

# def rev_str(string):
#     rev_str = ''
#     for ch in string[::-1]:
#         rev_str += ch
#     return rev_str


# def rev_str(string):
#     return string[::-1]

# def rev_str(string):
#     rev_str = ''
#     list_str = list(string)
#     for l in range(len(list_str)):
#         le = list_str.pop()
#         rev_str += le
#     return rev_str

# def rev_str(string):
#
#     if len(string) == 0:
#         return string
#     return string[-1] + rev_str(string[:-1])
#
# print(rev_str('hello'))

'''

Takes a list of integers and returns the highest product of three of the integers. The input list_of_ints will always have at least three integers.
    >>> highest_product_of_three([1,2,3,4,5])
    60
    >>> highest_product_of_three([1,2,3,4,-5])
    24
    >>> highest_product_of_three([-10,-10,1,3,2])
    300
    >>> highest_product_of_three([10,2,5])
    100
    >>> highest_product_of_three([5,4,3,2,1])
    60

'''

# def highest_product_of_three(list_of_ints):
#     high_prod = 0
#     for i in range(len(list_of_ints) -2):
#         j = i + 1
#         k = i + 2
#         pr = abs(list_of_ints[i] * list_of_ints[j] * list_of_ints[k])
#         if pr > high_prod:
#             high_prod = pr
#     return high_prod

# def highest_product_of_three(list_of_ints):
#     list_of_ints.sort()
#     print(list_of_ints)
#
#     # Consider maximum of last three elements or
#     # first two element and last element
#
#     if list_of_ints[-1] * list_of_ints[-2] * list_of_ints[-3] > list_of_ints[0] * list_of_ints[1] * list_of_ints[-1]:
#         prod = list_of_ints[-1] * list_of_ints[-2] * list_of_ints[-3]
#     else:
#         prod = list_of_ints[0] * list_of_ints[1] * list_of_ints[-1]
#     return prod
#
#
# print(highest_product_of_three([10,2,5]))

# def longestpal(string):
# # #     lo = ""
# # #     for i in range(len(string)):
# # #         for j in range(i, len(string)):
# # #             ss = string[i: j+1]
# # #             print(ss)
# # #             if len(ss) > len(lo) and ispal(ss):
# # #                 lo = ss
# # #     return lo
# # #
# # # def ispal(string):
# # #     left = 0
# # #     right = len(string) -1
# # #
# # #     while left < right:
# # #         if string[left] != string[right]:
# # #             return False
# # #         left += 1
# # #         right -= 1
# # #     return True
# # #
# # #
# # # print(longestpal('abaxyzzyxf'))

# array = [1,2,3,4,5,6,7]
# ma = array[:]
# print(ma)
# n=10
# ways = [0 for amount in range( n + 1)]
# ways[0] = 1
# print(ways)

# def numberOfWaysToMakeChange(n, denoms):
#     ways = [0 for amount in range(n+1)]
#     ways[0] = 1
#     for denom in denoms:
#         for amount in range(1, n+1):
#             if denom <= amount:
#                 ways[amount] += ways[amount - denom]
#     return ways[n]
#
#
#
# print (numberOfWaysToMakeChange(10, [1,5,10,25]))

# words =["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# ana = {}
# for word in words:
# 	sword = "".join(sorted(word))
# 	if sword in ana:
# 		ana[sword].append(word)
# 	else:
# 		ana[sword] = [word]
# print( list(ana.values()))
# print( list(ana.keys()))

# sortedwo = ["".join(sorted(w)) for w in words]
#
# ind = [i for i in range(len(words))]
# ind.sort()
# print(ind)

# array = [1, 3, 5 ,7]
# p = [1 for i in range(len(array))]
# print(p)


# array = 'karthikbabu'
# # print(array[1::-1])

# def zizagorder():
#     if root is None:
#         return []
#     stack = [root]
#     left = True
#     res = []
#
#     while stack:
#         tmp = []
#         tmp_stack =[]
#         for i in range(len(stack)):
#             node = stack.pop()
#             tmp.append(node.val)
#             if left:
#                 if node.left:
#                     tmp_stack.append(node.left)
#                 if node.right:
#                     tmp_stack.append(node.right)
#             else:
#                 if node.right:
#                     tmp_stack.append(node.right)
#                 if node.left:
#                     tmp_stack.append(node.left)
#         res.append(tmp)
#         stack = tmp_stack
#         left = False
#     return res

# word = 'kucgAwkuf3e'
# words = list(word)
# new = []
# print(words)
# for i in words:
#     if i.upper() == 'A':
#         pass
#     else:
#         new.append(i)
# print(''.join(new))
#
# vowels = set('AEIOU')
# new = [letter for letter in word if letter not in vowels]
# print(''.join(new))

#
# response = [
#         {
#             "DATA": {},
#             "MESSAGE": "",
#             "METHOD": "DELETE",
#             "REQUEST_PATH": "https://10.122.197.6:443/appcenter/Cisco/elasticservice/elasticservice-api/fabrics/external/service-nodes/SN-11",
#             "RETURN_CODE": 200
#         },
#         {
#             "DATA": {
#                 "attachedFabricName": "Fabric1",
#                 "attachedSwitchInterfaceName": "vPC1",
#                 "attachedSwitchSn": "SAL1820SDPP,SAL1819S6K3",
#                 "fabricName": "external",
#                 "formFactor": "Physical",
#                 "interfaceName": "svc12",
#                 "lastUpdated": 1612372914205,
#                 "linkTemplateName": "service_link_trunk",
#                 "linkUuid": "LINK-UUID-207570,LINK-UUID-207680",
#                 "name": "SN-12",
#                 "nvPairs": {
#                     "ADMIN_STATE": "true",
#                     "ALLOWED_VLANS": "none",
#                     "BPDUGUARD_ENABLED": "no",
#                     "MTU": "jumbo",
#                     "PORTTYPE_FAST_ENABLED": "true",
#                     "SPEED": "Auto"
#                 },
#                 "type": "ADC",
#                 "vpcSwitchesAttached": "true"
#             },
#             "MESSAGE": "",
#             "METHOD": "POST",
#             "REQUEST_PATH": "https://10.122.197.6:443/appcenter/Cisco/elasticservice/elasticservice-api/fabrics/external/service-nodes",
#             "RETURN_CODE": 200
#         }
#
# ]
#
# #(result.response[0].DATA|dict2items)[0].value == "SUCCESS"
#
# print(response[1]['DATA']['attachedFabricName'])
# #
# # DATA|dict2items)[0].value


# quote = '''
#   When I see a bird
#    that walks like a duck
#    and swims like a duck
#    and quacks like a duck,
#    I call that bird a duck
#    '''
#
# def quote_words(quote):
#     d = {}
#
#     for word in quote.split():
#         print(word)
#         if word in d:
#             d[word] += 1
#         else:
#             d[word] = 1
#     return d


res = "Directory of flash:guest-share/ddr/chaos/

303320  -rw-            91303  May 24 2021 20:04:02 +05:30  ?
303319  -rw-         43276386  May 24 2021 20:02:47 +05:30  ddmi-9500-2_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_17162_20210524-191633-IST.core.gz
303318  -rw-         43279742  May 24 2021 20:02:47 +05:30  ddmi-9500-2_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_15403_20210524-191603-IST.core.gz
303317  -rw-         43276593  May 24 2021 20:02:47 +05:30  ddmi-9500-2_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_14665_20210524-191534-IST.core.gz
303313  -rw-            91303  May 24 2021 19:14:47 +05:30  rp_base.cdb
303314  drwx             4096  May 24 2021 15:20:36 +05:30  __pycache__
303312  -rw-             1743  May 24 2021 15:16:11 +05:30  chaos.py
303310  -rw-            58128  May 24 2021 15:15:55 +05:30  genie_parsers.py
303311  -rw-            23817  May 24 2021 15:15:53 +05:30  ddrlib.py
"

print(res)