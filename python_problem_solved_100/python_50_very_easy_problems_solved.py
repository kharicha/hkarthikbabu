#100+ Python challenging programming exercises

# 1, Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# l = []
# for i in range(2000, 3200+1):
#     if i % 7 == 0 and i % 5 != 0:
#         l.append(str(i))
# print(l)
# print (','.join(l))

#2, Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
#40320

# def fact(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(8))

#3 Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# n = int(input().strip())
# d = dict()
# for i in range(1, n+1):
#     d[i] = i * i
#
# print (d)
# for k, v in d.items():
#     print ("{} > {}".format(k, v))

#4 Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# n = input().strip()
# values = n.split(',')
# t = tuple(values)
# print(values)
# print(t)

#5 Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters

# class kar():
#     def __init__(self):
#         self.string = ''
#     def getString(self):
#         self.string = input().strip()
#     def printString(self):
#         print (self.string.upper())
#
# k = kar()
# k.getString()
# k.printString()

#6 Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
#
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value
# (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.

# import math
# c = 50
# h = 30
# val = []
#
# items = [x for x in input().strip().split(',')]
# print(items)
# for i in items:
#     val.append(str(int(round((math.sqrt(2*c*float(i)/h))))))
# print(val)
# print(','.join(val))

#7 Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

# dimensions=[int(x) for x in input().split(',')]
# print(dimensions)
# rowNum=dimensions[0]
# colNum=dimensions[1]
# print(rowNum)
# print(colNum)
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# print(multilist)
#
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
#
# print (multilist)

# dim = [int(x) for x in input().split(',')]
# row = dim[0]
# col = dim[1]
# ml = [[0 for c in range(col)] for r in  range(row)]
# print (ml)
#
# for r in range(row):
#     for c in range(col):
#         ml[r][c] = r * c
# print(ml)

#8 Question:
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# strings = input().split(',')
# print(strings)
# s = sorted(strings)
# print(','.join(s))
# s = sorted(strings, reverse = True)
# print(','.join(s))

# items=[x for x in input().split(',')]
# items.sort()
# print (','.join(items))

#9 Question
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s)
#     else:
#         break
# for l in lines:
#     print(l.upper())

#10 Question:
# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# item = [x for x in input().split(' ')]
# print (item)
# l = []
# for i in item:
#     l.append(i)
# print(' '.join(sorted(list(set(l)))))

# s = raw_input()
# words = [word for word in s.split(" ")]
# print " ".join(sorted(list(set(words))))

#11 Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#

# val = []
# items = [x for x in input().split(',')]
# print(items)
# for i in items:
#     intp = int(i, 2)
#     print(intp)
#     if intp%5 == 0:
#         val.append(i)
# print(','.join(val))

#12 Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# val = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0]) % 2 == 0 ) and (int(s[1]) % 2 == 0 ) and (int(s[2]) % 2 ==0 ) and (int(s[3]) % 2 == 0):
#         val.append(s)
# print(','.join(val))

#13 Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# sen = input()
# print(sen)
# digits = 0
# letters = 0
# sc = 0
# for s in sen:
#     if s.isdigit():
#         digits += 1
#     elif s.isalpha():
#         letters += 1
#     else:
#         sc += 1
#
# print("LETTERS", letters)
# print("DIGITS", digits)
# print("SPECIAL CHAR", sc)

# same using dic
# sen = input()
# d = {'DIGITS' : 0 , 'LETTERS' : 0}
# for s in sen:
#     if s.isdigit():
#         d['DIGITS'] +=1
#     elif s.isalpha():
#         d['LETTERS'] +=1
#
# print("LETTERS", d['DIGITS'])
# print("DIGITS", d['LETTERS'])

#14 Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# sen = input()
# d = {"UPPER":0, "LOWER":0}
# for s in sen:
#     if s.isupper():
#         d['UPPER'] += 1
#     elif s.islower():
#         d['LOWER'] += 1
#     else:
#         pass
# print("UPPER CASE", d['UPPER'])
# print("LOWER CASE", d['LOWER'])

#15 Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print(n1+n2+n3+n4)

#16 Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# out = [x for x in input().split(',') if int(x)%2!=0]
# print (','.join(out))

#17 Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
#
# net = 0
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(' ')
#     ac = values[0]
#     rs = int(values[1])
#     if ac == 'D':
#         net += rs
#     elif ac == 'W':
#         net -= rs
#     else:
#         pass
# print(net)

#18 Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# import re
# pw = [x for x in input().split(',')]
# print(pw)
# val =[]
#
# for p in pw:
#     if len(p) < 6 or len(p) > 12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]", p):
#         continue
#     elif not re.search("[0-9]", p):
#         continue
#     elif not re.search("[A-Z]", p):
#         continue
#     elif not re.search("[$#@]", p):
#         continue
#     elif re.search("\s", p):
#         continue
#     else:
#         val.append(p)
# print(val)
# print(",".join(val))

# reverse a string

#s = input()
# rev = ''
# index = len(s)
# while index >0:
#     rev += s[index -1]
#     index -= 1
# print(rev)

#print(s[::-1])

#19 Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
# age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
#
# from operator import itemgetter, attrgetter
# val = []
# while True:
#     t = input()
#     if not t:
#         break
#     val.append(tuple(t.split(',')))
# print(sorted(val, key=itemgetter(0,1,2)))

#20 Question:
# Write a method which can calculate square value of number

# def cal_sqr(n):
#     return n**2
#
# print(cal_sqr(10))

#21 Question:
#    Define a function which can print a dictionary
#    where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

# def pr_d():
#     d = dict()
#     for i in range(1, 3+1):
#         d[i] = i**2
#     print(d.values())
#     for k, v in d.items():
#         print(v)
#         print(k)
#         print("{} , {}".format(k,v))
#
# pr_d()

# 22 Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# def sq_list():
#     l = []
#     for i in range(1, 20+1):
#         l.append(i**2)
#     print(l)
# sq_list()

#23 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.
#
# def sq_list():
#     l = []
#     for i in range(1, 20+1):
#         l.append(i**2)
#     for i in range(5):
#         print(l[i])
#     print(l[:5])
# sq_list()

#24 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.

# def sq_list():
#     l = []
#     for i in range(1, 20+1):
#         l.append(i**2)
#     for i in range(5):
#         print(l[i])
#     print(l[-5:])
# sq_list()

#25 Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the except the first 5 elements in the list.
#
# def sq_list():
#     l = []
#     for i in range(1, 20+1):
#         l.append(i**2)
#     print(l[5:])
# sq_list()

#26 Define a function which can generate and print a tuple where the value
# are square of numbers between 1 and 20 (both included).

# def sq_tu():
#     l = []
#     for i in range(1, 21):
#         l.append(i**2)
#     print (tuple(l))
# sq_tu()

#27 With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values in one line and the last half values in one line.

# tu = (1,2,3,4,5,6,7,8,9,10)
# print(tu[:5])
# print(tu[5:])

#28 Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# tu = (1,2,3,4,5,6,7,8,9,10)
# n_tu = []
# for i in range(len(tu)):
#     if tu[i] % 2 == 0:
#         n_tu.append(tu[i])
# print(tuple(n_tu))

#29 Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# l = [1,2,3,4,5,6,7,8,9,10]
# s = list(map(lambda x: x**2, filter(lambda x: x%2 ==0, l)))
# print(s)

#30 Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# li =[]
# for i in range(1, 21):
#     li.append(i)
# s = list(filter(lambda x: x%2==0, li))
# print(s)

# evenNumbers = filter(lambda x: x%2==0, range(1,21))
# print (list(evenNumbers))

#31 Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# s = list(map(lambda x: x**2, range(1,21)))
# print(s)

#32 Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

# s = input()
# st = s.split('@')
# print(st[0])
# print(st[1])

#same using reg exp
# s= input()
# import re
# pat = "(\w+)\@(\w+)\.(\w+)"
# r2 = re.match(pat, s)
# print(r2.group(1))

# s = input()
# import re
# pat = "(\w+)@(\w+)\.(\w+)"
# r2 = re.match(pat, s)
# print(r2.group(1))
# print(r2.group(2))

#33 convert a ASCII string to unicode one with encode utf-8

# s = input()
# u = unicode( s ,"utf-8")
# print(u)

#34 prime number

# n = int(input())
#
# if n > 1:
#     for i in range (2, n):
#         if n%i == 0:
#             print("Not a prime")
#             break
#     else:
#         print("{} a prime".format(n))
# else:
#     print("Not a Prime")

# 35 fibonacci

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
#
# print(f(10))

# 36 factorial

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(10))

#37 Question:

# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 10
#
# Then, the output of the program should be:
#
# 0,2,4,6,8,10
#
# Hints:
# Use yield to produce the next value in generator.

# The yield statement suspends function’s execution and sends a value back to the caller,
# but retains enough state to enable function to resume where it is left off.
# When resumed, the function continues execution immediately after the last yield run.

# def even(n):
#     i = 0
#     while i <= n:
#         if i%2 == 0:
#             yield i
#         i += 1
#
# n=int(input())
# values = []
# for i in even(n):
#     values.append(str(i))
# print (",".join(values))

#38 Question:
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma
# separated form while n is input by console.

# Example:
# If the following n is given as input to the program:
#
# 100
#
# Then, the output of the program should be:
#
# 0,35,70
#
# Hints:
# Use yield to produce the next value in generator.
#
# def gen(n):
#     i = 0
#     while i<=n:
#         if i%5 ==0 and i%7 ==0:
#             yield i
#         i +=1
#
# n = int(input())
# l = []
# for i in gen(n):
#     l.append(str(i))
# print(",".join(l))

# 39
# Random Generator

# import random
# print (random.random()*100)
# print (random.random()*100-5)

#40 Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%2!=0]
# print(li)

#41 By using list comprehension, please write a program to
# print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# li = [12,24,35,70,88,120,155]
# li = [x for x in li if x%5 == 0 and x%7 ==0]
# print(li)

#42 By using list comprehension, please write a program to print the list after
# removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i%2 !=0 ]
# print(li)

#43 By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
# array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
# print (array)
#
# li = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(li)

#44 By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
# print(li)

#45 By using list comprehension,
# please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# li = [12,24,35,24,88,120,155]
# li = [x for x in li if x!=24]
# print(li)

#46 With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.

# li = set([12,24,35,24,88,120,155,88,120,155])
# print(li)

#47 Please write a program which count and print the numbers of each character in a string input by console.

# Example:
# If the following string is given as input to the program:
#
# abcdefgabc
#
# Then, the output of the program should be:
#
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

#s = input()
# d = dict()
# for c in s:
#     if c in d:
#         d[c] += 1
#     else:
#         d[c] = 1
# print(d)
# for k,v in d.items():
#     print("{},{}".format(k,v))

#48 Please write a program which accepts a string from console and print the characters that have even indexes.

# Example:
# If the following string is given as input to the program:
#
# H1e2l3l4o5w6o7r8l9d
#
# Then, the output of the program should be:
#
# Helloworld

# s = input()
# print(s[::2])