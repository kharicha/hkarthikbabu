# def nat(n):
#     sum = 0
#     for i in range(1, n):
#         if i%3 == 0 or i%5 == 0:
#             sum += i
#             print(i)
#     return sum
#
# print(nat(1000))

dictionary = { "some_key": "some_value" }

for key in dictionary:
    print("%s --> %s" %(key, dictionary[key]))

for key, value in dictionary.items():
    print("%s --> %s" %(key, value))