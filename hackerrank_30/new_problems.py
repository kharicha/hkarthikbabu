'''
Solve Me First & Simple Array Sum
'''

# def solve(a,b):
#     return a+b
#
# num1 = int(input())
# num2 = int(input())
# print(solve(num1, num2))

'''
Given an array of integers, find the sum of its elements
'''
# a = [ int(x) for x in input().split(' ')]
# #inbuilt sum function
# print(sum(a))
#
# #using iterative
# s = 0
# for i in range(len(a)):
#     print(i)
#     s += a[i]
# print(s)

'''
Compare the Triplets
'''
# a = [int(x) for x in input().split(' ')]
# b = [int(x) for x in input().split(' ')]
# al = bl = 0
# for i in range(len(a)):
#         if a[i] > b[i]:
#             al += 1
#         elif a[i] < b[i]:
#             bl += 1
#         else:
#             pass
# print(al, bl)

'''
add a very big sum
'''

# s = int(input())
# l = []
# for i in range(s):
#     l.append(int(input()))
# print(l)
# print(sum(l))

# import re
# output = '''
# Local MEPs:
# --------------------------------------------------------------------------------
# MPID Domain Name                                 Lvl   MacAddress     Type  CC
# Ofld Domain Id                                   Dir   Port           Id
#      MA Name                                           SrvcInst       Source
#      EVC name
#      CCM Mode
# --------------------------------------------------------------------------------
# 8000 kar                                         0     aabb.cc00.8310 BD-V  Y
# No   kar                                         Down  Et0/1          101
#      red                                               500            Staticgreen
#      Multicast
#
# Total Local MEPs: 1
#
# Local MIPs: None
# '''
# print(output)
#
# mpid = dname = evcname = ccmmode = di = sinst = cc = 0
# dire = 'down'
# sins = '500'
#
# for line in output.split('\n'):
#     line = line.strip()
#     print(line)
#     if not di:
#         if re.search('%s' %(dire),line, re.IGNORECASE):
#             di = 1
#             continue
#     if not sinst:
#         if re.search('%s' %(sins),line, re.IGNORECASE):
#             sinst = 1
#             continue
#
# if (sinst & di):
#     print('karthik')
# else:
#     print('babu')
#
# # intf = "e0/1"
# # print(intf)
# # cli = "show run interface %s"
# # cli %= intf
# # print(cli)
#


# def mergesort(dataset):
#
#     if len(dataset) > 1:
#         mid = len(dataset) // 2
#         left = dataset[:mid]
#         right = dataset[mid:]
#
#         mergesort(left)
#         mergesort(right)
#
#         i = j = k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 dataset[k] = left[i]
#                 i += 1
#             else:
#                 dataset[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             dataset[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             dataset[k] = right[j]
#             j += 1
#             k += 1
#
# items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
# print(items)
# mergesort(items)
# print(items)

# def bbsort(dataset):
#
#     for i in range(len(dataset) -1, 0, -1):
#         for j in range(i):
#             if dataset[j] > dataset[j+1]:
#                 temp = dataset[j]
#                 dataset[j] = dataset[j+1]
#                 dataset[j+1] = temp
#
# items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
# print(items)
# bbsort(items)
# print(items)


def findel(item, itemlist):
    for i in range(len(itemlist)):
        if item == itemlist[i]:
            return(i)

    print("item " +str(item)+ " not found")


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(findel(87, items))
print(findel(879, items))