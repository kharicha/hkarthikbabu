# '''
# Input
# # An input contains 2 integers A and B.
# #
# # Output
# # Print a wrong answer of A-B. Your answer must be a positive integer containing the same number of digits
# # as the correct answer, and exactly one digit must differ from the correct answer. Leading zeros are not
# # allowed. If there are multiple answers satisfying the above conditions, anyone will do.
# '''
#
# n = input().split(' ')
# s = int(n[0]) - int(n[1])
# print(s)
#
# si = str(s)
# for i in range(len(si)):
#

# quote = '''
#   When I see a bird
#    that walks like a duck
#    and swims like a duck
#    and quacks like a duck,
#    I call that bird a duck
#    '''


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
# print(quote_words(quote))
#
# cities = [1,2,3,4,5]
# print(len(cities))

# name = 'karthik babu hari babu'
# print(name[0].split())

# def convert(name):
#     print (' '.join(name).split())
#     #return (name[0].split())
#
#
# # Driver code
# name = ["karthik babu hari babu"]
# print(convert(name))
#
# name = 'karthik babu hari babu'
# # n = name.split()
# # print(n)
# # nam = []
# # for na in n:
# #     print(na)
# #     nam.append(na)
# # print(nam[2])
#
# n = name [::-1]
# print(n)


#include <stdio.h>

# no = [2,38,4857,1299,1,2,4,7]
# no.sort()
# print(no)
# n = sorted(no)
# print(n)

# # Defining lists
# L1 = [1, 2, 3]
# L2 = [2, 3, 4]
#
# # L3 = []
# # for i in range(len(L1)):
# #     L3.append(L1[i]*L2[i])
# # print(L3)
#
# import operator
#
# a,b,c = map(operator.mul, L1, L2)
# print(a,b,c)


# def pal(s):
# #     rev = ''
# #
# #     for c in reversed(s):
# #         rev += c
# #
# #     if rev == s:
# #         return True
# #     else:
# #         return False
# # print(pal('madam'))

# import itertools
# #
# # c = itertools.count(5,10)
# # print(next(c))
# # print(next(c))

# no = int(input("enter teh ni"))
# s = 0
# temp = no
# while temp > 0:
#     c = temp %10
#     print(c)
#     s += c**3
#     print(s)
#     temp = temp//10
#     print(temp)
#
# if no == s:
#     print("armstrong")
# else:
#     print("not armstrong")

#pyramid

# no = 5
# m = (2 * no) - 2
#
# for i in range(0, no):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print(" ")

#prime:

# def pri(n):
# #     if n > 1:
# #         for i in range(2, n):
# #             if n % i == 0:
# #                 print("not prime")
# #                 break
# #             else:
# #                 print(" prime")
# #                 break
# #     else:
# #         print("not prime")
# #
# # pri(3)

# ph = "1905"
# #
# # for p in ph:
# #     print(p)

#!env python

from lmconsole.client import *

client = LMclient('kharicha').wait()
print("client is", client)

service = client.service("6hu-91t-yd7-qik")

service.update_inventory().wait()

print(service.inventory)

shver = service.inventory['cat9k-24'].exec('show version').wait()

print(shver.result.data)

ship = service.inventory['cat9k-24'].exec('show ip int br').wait()

print(shver.result.data)

ddr = service.inventory['cat9k-24']
ses = ddr.ssh().wait()
print(ses)

cmd = "guestshell run python3 /home/guestshell/emre/runemre py --facts=/bootflash/guest-share/emre/tcam/emre-facts --rules=/bootflash/guest-share/emre/tcam/emre-rules"

ses.write(cmd.encode())
out = ses.read(None, blocking=False).decode()

print(out)




client.terminate()

while True:
    try:
        emre.wait(timeout=120)
        break
    except TimeoutError:
        print('not yet ready')
print('done')

emre = service.inventory['cat9k-24'].exec('guestshell run python3 /home/guestshell/emre/runemre.py --facts=/bootflash/guest-share/emre/tcam/emre-facts --rules=/bootflash/guest-share/emre/tcam/emre-rules').wait(timeout=120)


emre = service.inventory['cat9k-24']
ses = emre.ssh().wait()
cmd = "guestshell run python3 /home/guestshell/emre/runemre.py --facts=/bootflash/guest-share/emre/tcam/emre-facts --rules=/bootflash/guest-share/emre/tcam/emre-rules\n”
ses.write(cmd.encode())
out = ses.read(None, blocking=False).decode()
out | print

emre = service.inventory['cat9k-24’]
emre.interactive()