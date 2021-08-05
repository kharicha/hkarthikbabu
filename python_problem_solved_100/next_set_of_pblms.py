# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# # # # # # # # # # # # # between 2000 and 3200 (both included).
# # # # # # # # # # # # # The numbers obtained should be printed in a comma-separated sequence on a single line.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # li =[]
# # # # # # # # # # # # # # for i in range(2000, 3201):
# # # # # # # # # # # # # #     if i%7 == 0 and i%5 !=0:
# # # # # # # # # # # # # #         li.append(str(i))
# # # # # # # # # # # # # # print(",".join(li))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #using list comprension
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program which can compute the factorial of a given numbers.The results should be printed in a
# # # # # # # # # # # # # comma-separated sequence on a single line.
# # # # # # # # # # # # # Suppose the following input is supplied to the program: 8 Then, the output should be:40320
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def fac(n):
# # # # # # # # # # # # # #     if n < 1:
# # # # # # # # # # # # # #         return 1
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         return n * fac(n-1)
# # # # # # # # # # # # # # print(fac(8))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # iterative
# # # # # # # # # # # # # # def fac(n):
# # # # # # # # # # # # # #     i = 1
# # # # # # # # # # # # # #     fact = 1
# # # # # # # # # # # # # #     while i <=n:
# # # # # # # # # # # # # #         fact = fact * i
# # # # # # # # # # # # # #         i += 1
# # # # # # # # # # # # # #     return fact
# # # # # # # # # # # # # # print(fac(8))
# # # # # # # # # # # # #
# # # # # # # # # # # # # #using for loop
# # # # # # # # # # # # # # def fac(n):
# # # # # # # # # # # # # #     f = 1
# # # # # # # # # # # # # #     for i in range(1,n+1):
# # # # # # # # # # # # # #         f = f * i
# # # # # # # # # # # # # #     return f
# # # # # # # # # # # # # # print(fac(8))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# # # # # # # # # # # # # such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# # # # # # # # # # # # # Suppose the following input is supplied to the program: 8
# # # # # # # # # # # # #
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # #using dict
# # # # # # # # # # # # # # def di(n):
# # # # # # # # # # # # # #     d = dict()
# # # # # # # # # # # # # #     for i in range(1, n+1):
# # # # # # # # # # # # # #         d[i] = i * i
# # # # # # # # # # # # # #     return (d)
# # # # # # # # # # # # # # print(di(8))
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Using dictionary comprehension
# # # # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # # # ans = { i : i*i for i in range(1, n+1)}
# # # # # # # # # # # # # # print(ans)
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program which accepts a sequence of comma-separated numbers from console and generate
# # # # # # # # # # # # # a list and a tuple which contains every number.Suppose the following input is supplied to the program:
# # # # # # # # # # # # # 34,67,55,33,12,98
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # ['34', '67', '55', '33', '12', '98']
# # # # # # # # # # # # # ('34', '67', '55', '33', '12', '98')
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # n = input().strip()
# # # # # # # # # # # # # # values = n.split(',')
# # # # # # # # # # # # # # print(values)
# # # # # # # # # # # # # # print(tuple(values))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Define a class which has at least two methods:
# # # # # # # # # # # # #
# # # # # # # # # # # # # getString: to get a string from console input
# # # # # # # # # # # # # printString: to print the string in upper case.
# # # # # # # # # # # # # Also please include simple test function to test the class methods.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # class Solution():
# # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # #         self.s = ''
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     def getString(self):
# # # # # # # # # # # # # #         s = input()
# # # # # # # # # # # # # #         self.s = s
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     def printString(self):
# # # # # # # # # # # # # #         return self.s.upper()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # s = Solution()
# # # # # # # # # # # # # # s.getString()
# # # # # # # # # # # # # # print(s.printString())
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program that calculates and prints the value according to the given formula:
# # # # # # # # # # # # #
# # # # # # # # # # # # # Q = Square root of [(2 _ C _ D)/H]
# # # # # # # # # # # # #
# # # # # # # # # # # # # Following are the fixed values of C and H:
# # # # # # # # # # # # #
# # # # # # # # # # # # # C is 50. H is 30.
# # # # # # # # # # # # #
# # # # # # # # # # # # # D is the variable whose values should be input to your program in a comma-separated sequence.
# # # # # # # # # # # # #
# # # # # # # # # # # # # For example Let us assume the following comma separated input sequence is given to the program:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 100,150,180
# # # # # # # # # # # # # The output of the program should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 18,22,24
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # c = 50
# # # # # # # # # # # # # # h = 30
# # # # # # # # # # # # # # l = []
# # # # # # # # # # # # # # # lis = [x for x in input().split(',')]
# # # # # # # # # # # # # # n = input()
# # # # # # # # # # # # # # lis = n.split(',')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for li in lis:
# # # # # # # # # # # # # #     l.append(str(int(round(math.sqrt(2*c*float(li)/h)))))
# # # # # # # # # # # # # # print(','.join(l))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# # # # # # # # # # # # # The element value in the i-th row and j-th column of the array should be i _ j.*
# # # # # # # # # # # # #
# # # # # # # # # # # # # Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# # # # # # # # # # # # #
# # # # # # # # # # # # # Then, the output of the program should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # num = input().split(',')
# # # # # # # # # # # # # # row = int(num[0])
# # # # # # # # # # # # # # col = int(num[1])
# # # # # # # # # # # # # # x = [[0 for c in range(col)] for r in range(row)]
# # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for r in range(row):
# # # # # # # # # # # # # #     for c in range(col):
# # # # # # # # # # # # # #         x[r][c] = r*c
# # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program that accepts a comma separated sequence of words as input and prints the words in
# # # # # # # # # # # # # a comma-separated sequence after sorting them alphabetically.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Suppose the following input is supplied to the program:
# # # # # # # # # # # # #
# # # # # # # # # # # # # without,hello,bag,world
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # bag,hello,without,world
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # items = [ x for x in input().split(',')]
# # # # # # # # # # # # # # items.sort()
# # # # # # # # # # # # # # print(','.join(items))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Suppose the following input is supplied to the program:
# # # # # # # # # # # # #
# # # # # # # # # # # # # Hello world
# # # # # # # # # # # # # Practice makes perfect
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # HELLO WORLD
# # # # # # # # # # # # # PRACTICE MAKES PERFECT
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # li = []
# # # # # # # # # # # # # # while True:
# # # # # # # # # # # # # #     s = input()
# # # # # # # # # # # # # #     if not s:
# # # # # # # # # # # # # #         break
# # # # # # # # # # # # # #     li.append(s.upper())
# # # # # # # # # # # # # # for s in li:
# # # # # # # # # # # # # #     print(s)
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program that accepts a sequence of whitespace separated words as input and
# # # # # # # # # # # # # prints the words after removing all duplicate words and sorting them alphanumerically.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Suppose the following input is supplied to the program:
# # # # # # # # # # # # #
# # # # # # # # # # # # # hello world and practice makes perfect and hello world again
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # again and hello makes perfect practice world
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # st = [x for x in input().split(' ')]
# # # # # # # # # # # # # # print (" ".join(sorted(list(set(st)))))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program which accepts a sequence of comma separated 4 digit binary numbers
# # # # # # # # # # # # # as its input and then check whether they are divisible by 5 or not. The numbers
# # # # # # # # # # # # # that are divisible by 5 are to be printed in a comma separated sequence.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Example:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 0100,0011,1010,1001
# # # # # # # # # # # # # Then the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 1010
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # l = []
# # # # # # # # # # # # # # nu = [x for x in input().split(',')]
# # # # # # # # # # # # # # for n in nu:
# # # # # # # # # # # # # #     i = int(n,2)
# # # # # # # # # # # # # #     if i % 5 == 0:
# # # # # # # # # # # # # #         l.append(n)
# # # # # # # # # # # # # # print(''.join(l))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program, which will find all such numbers between 1000 and 3000
# # # # # # # # # # # # # (both included) such that each digit of the number is an even number.
# # # # # # # # # # # # # The numbers obtained should be printed in a comma-separated sequence on a single line.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # l = []
# # # # # # # # # # # # # # for n in range(1000, 3001):
# # # # # # # # # # # # # #     s = str(n)
# # # # # # # # # # # # # #     if (int(s[0])%2 ==0) and (int(s[1])%2 ==0) and (int(s[2])%2 ==0) and (int(s[3])%2==0):
# # # # # # # # # # # # # #         l.append(s)
# # # # # # # # # # # # # # print(','.join(l))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program that accepts a sentence and calculate the number of letters and digits.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Suppose the following input is supplied to the program:
# # # # # # # # # # # # # hello world! 123
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # LETTERS 10
# # # # # # # # # # # # # DIGITS 3
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # digit = letter = sc = 0
# # # # # # # # # # # # # # s = input()
# # # # # # # # # # # # # # for c in s:
# # # # # # # # # # # # # #     if c.isdigit():
# # # # # # # # # # # # # #         digit +=1
# # # # # # # # # # # # # #     elif c.isalpha():
# # # # # # # # # # # # # #         letter +=1
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         sc +=1
# # # # # # # # # # # # # # print('LETTER {}\nDIGITS {}'.format(letter,digit))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # s = input()
# # # # # # # # # # # # # # d = {'LETTERS': 0, 'DIGITS': 0}
# # # # # # # # # # # # # # for c in s:
# # # # # # # # # # # # # #     if c.isdigit():
# # # # # # # # # # # # # #         d['DIGITS'] += 1
# # # # # # # # # # # # # #     elif c.isalpha():
# # # # # # # # # # # # # #         d['LETTERS'] += 1
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         pass
# # # # # # # # # # # # # # print(d)
# # # # # # # # # # # # # # print ('LETTERS', d['LETTERS'])
# # # # # # # # # # # # # # print ('DIGITS', d['DIGITS'])
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Suppose the following input is supplied to the program:
# # # # # # # # # # # # #
# # # # # # # # # # # # # Hello world!
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # UPPER CASE 1
# # # # # # # # # # # # # LOWER CASE 9
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # s = input()
# # # # # # # # # # # # # # lc = 0
# # # # # # # # # # # # # # uc = 0
# # # # # # # # # # # # # # for c in s:
# # # # # # # # # # # # # #     if c.isupper():
# # # # # # # # # # # # # #         uc +=1
# # # # # # # # # # # # # #     elif c.islower():
# # # # # # # # # # # # # #         lc +=1
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         pass
# # # # # # # # # # # # # # print("UPPER CASE {} \nLOWER CASE {}".format(uc, lc))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Suppose the following input is supplied to the program:
# # # # # # # # # # # # # 9
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 11106
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = input()
# # # # # # # # # # # # # # a = int( "%s" % n)
# # # # # # # # # # # # # # b = int( "%s%s" % (n,n))
# # # # # # # # # # # # # # c = int( "%s%s%s" % (n,n,n))
# # # # # # # # # # # # # # d = int( "%s%s%s%s" % (n,n,n,n))
# # # # # # # # # # # # # # print(a+b+c+d)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = input()
# # # # # # # # # # # # # # print(int(n) + int(2*n) + int(3*n) + int(4*n))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Use a list comprehension to square each odd number in a list.
# # # # # # # # # # # # # The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 1,2,3,4,5,6,7,8,9
# # # # # # # # # # # # # Then, the output should be:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 1,9,25,49,81
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # l = [ str(int(i)**2)  for i in input().split(',') if int(i)%2!=0]
# # # # # # # # # # # # # # print(','.join(l))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Take two inputs from the user. One will be an integer. The other will be a float number. Then multiply them to display the output.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # # # i = float(input())
# # # # # # # # # # # # # # print(n*i)
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Take two numbers from the users. Calculate the result of second number power of the first number.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # n = input().split(',')
# # # # # # # # # # # # # # b = int(n[0])
# # # # # # # # # # # # # # p = int(n[1])
# # # # # # # # # # # # # # print(b ** p)
# # # # # # # # # # # # # # print(pow(b,p))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # random num
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # To create a random number, you have to import a built-in library named random. And then you can call the randint method on it
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # import random
# # # # # # # # # # # # # # print(random.randint(0,10))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Find the floor division of two numbers.
# # # # # # # # # # # # #
# # # # # # # # # # # # # # print(round(17/5))
# # # # # # # # # # # # # # print(17//5)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Swap two variables
# # # # # # # # # # # # # # To swap two variables: the value of the first variable will become the value of the second variable.
# # # # # # # # # # # # # # On the other hand, the value of the second variable will become the value of the first variable.
# # # # # # # # # # # # #
# # # # # # # # # # # # # # a = 2
# # # # # # # # # # # # # # b = 3
# # # # # # # # # # # # # # temp = a
# # # # # # # # # # # # # # a = b
# # # # # # # # # # # # # # b = temp
# # # # # # # # # # # # # # print('a,b', a,b)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # a = 2
# # # # # # # # # # # # # # b = 3
# # # # # # # # # # # # # # a, b = b, a
# # # # # # # # # # # # # # print('a,b', a,b)
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # max of two
# # # # # # # # # # # # # The problem
# # # # # # # # # # # # # Find the max number of two numbers.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # print(max(5,10))
# # # # # # # # # # # # #
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # max of three
# # # # # # # # # # # # # The problem
# # # # # # # # # # # # # Find the largest of the three numbers.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # n = input().split(',')
# # # # # # # # # # # # # # # max = n[0]
# # # # # # # # # # # # # # # if n[1]  >= n[0] and n[1] >= n[2]:
# # # # # # # # # # # # # # #     max = n[1]
# # # # # # # # # # # # # # # elif n[2] >= n[0] and n[2] >= n[1]:
# # # # # # # # # # # # # # #     max = n[1]
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     max = n[1]
# # # # # # # # # # # # # # print(max)
# # # # # # # # # # # # # # #shortcut
# # # # # # # # # # # # # # print(max(int(n[0]),int(n[1]),int(n[2])))
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Average of numbers
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Take numbers from a user and show the average of the numbers the user entered.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # n = int(input("how many numbers you want to enter: "))
# # # # # # # # # # # # # # l = []
# # # # # # # # # # # # # # for i in range(n):
# # # # # # # # # # # # # #     s = int(input())
# # # # # # # # # # # # # #     l.append(s)
# # # # # # # # # # # # # # su = sum(l)
# # # # # # # # # # # # # # print(su//n)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Divisible by 3 and 5
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # # # l = [ str(x) for x in range(n) if x%3==0 and x%5 ==0]
# # # # # # # # # # # # # # print(','.join(l))
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Sum of Elements
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # For a given list, get the sum of each number in the list
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # nums = [13,89,65,42,12,11,56]
# # # # # # # # # # # # # # print(sum(nums))
# # # # # # # # # # # # # # s = 0
# # # # # # # # # # # # # # for i in nums:
# # # # # # # # # # # # # #     s += i
# # # # # # # # # # # # # # print(s)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Largest element of a list
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Find the largest element of a list.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # nums = [13,89,65,42,12,11,56]
# # # # # # # # # # # # # # print(max(nums))
# # # # # # # # # # # # # # max = nums[0]
# # # # # # # # # # # # # # for i in nums:
# # # # # # # # # # # # # #     if i > max:
# # # # # # # # # # # # # #         max = i
# # # # # # # # # # # # # # print(max)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Sum of squares
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Take a number as input. Then get the sum of the numbers. If the number is n. Then get
# # # # # # # # # # # # #
# # # # # # # # # # # # # 0^2+1^2+2^2+3^2+4^2+.............+n^2
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # # # s = 0
# # # # # # # # # # # # # # for i in range(n+1):
# # # # # # # # # # # # # #     s += i**2
# # # # # # # # # # # # # #     #s += pow(i,2)
# # # # # # # # # # # # # # print(s)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def square_sum(num):
# # # # # # # # # # # # # #     sum = 0
# # # # # # # # # # # # # #     for i in range(num + 1):
# # # # # # # # # # # # # #         square = (i ** 2)
# # # # # # # # # # # # # #         sum = sum + square
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     return sum
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # num = int(input('Enter a number: '))
# # # # # # # # # # # # # # sum = square_sum(num)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print('sum of square numbers is ', sum)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Second Largest
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # For a list, find the second largest number in the list.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # #nums = [13,89,65,42,12,11,56]
# # # # # # # # # # # # # # m1 = nums[0]
# # # # # # # # # # # # # # m2 = nums[0]
# # # # # # # # # # # # # # for i in range(1, len(nums)):
# # # # # # # # # # # # # #     if nums[i] > m1:
# # # # # # # # # # # # # #         m2 = m1
# # # # # # # # # # # # # #         m1 = nums[i]
# # # # # # # # # # # # # #     elif nums[i] > m2:
# # # # # # # # # # # # # #         m2 = nums[i]
# # # # # # # # # # # # # # print(m2)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # nums.remove(max(nums))
# # # # # # # # # # # # # # m = max(nums)
# # # # # # # # # # # # # # print(m)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Second smallest element
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # For a list, find the second smallest element in the list
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # nums = [13,89,65,42,12,11,56]
# # # # # # # # # # # # # # m1 = nums[0]
# # # # # # # # # # # # # # m2 = nums[0]
# # # # # # # # # # # # # # for i in range(1, len(nums)):
# # # # # # # # # # # # # #     if nums[i] < m1:
# # # # # # # # # # # # # #         m2 = m1
# # # # # # # # # # # # # #         m1 = nums[i]
# # # # # # # # # # # # # #     elif nums[i] < m2:
# # # # # # # # # # # # # #         m2 = nums[i]
# # # # # # # # # # # # # # print(m2)
# # # # # # # # # # # # # # nums.remove(min(nums))
# # # # # # # # # # # # # # print(min(nums))
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Remove duplicate characters
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # For a given string, remove all duplicate characters from that string.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # s = 'ejhduwekcurbwejck'
# # # # # # # # # # # # # # si = ''
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for c in s:
# # # # # # # # # # # # # #     if c not in si:
# # # # # # # # # # # # # #         si += c
# # # # # # # # # # # # # # print(si)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Miles to Kilometers
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Convert miles to kilometers.
# # # # # # # # # # # # # I am telling you just one thing:
# # # # # # # # # # # # #
# # # # # # # # # # # # # 1 mile = 1.609344 kilometers
# # # # # # # # # # # # #
# # # # # # # # # # # # # Now, think what you can do with this information.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = float(input("enter the miles to get convert to miles:"))
# # # # # # # # # # # # # # k = n * 1.609344
# # # # # # # # # # # # # # print(k)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Celsius to Fahrenheit
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Take the temperature in degrees Celsius and convert it to Fahrenheit.
# # # # # # # # # # # # # To convert degrees Celsius temperature to Fahrenheit, you have to multiply by 9 and divide by 5.
# # # # # # # # # # # # #
# # # # # # # # # # # # # And then, add 32.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = float(input("enter the celsius to f: "))
# # # # # # # # # # # # # # f = (n * 1.8) + 32
# # # # # # # # # # # # # # print(f)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Decimal to Binary and vice versa
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # Convert a decimal number to binary number.
# # # # # # # # # # # # #
# # # # # # # # # # # # # To convert a decimal number to a binary number, you have to keep dividing the number by 2.
# # # # # # # # # # # # #
# # # # # # # # # # # # # While dividing, you will keep the remainder. These remainders will be used to build a binary number.
# # # # # # # # # # # # #
# # # # # # # # # # # # # Then, reverse the order of the reminder, to get the binary number.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = int(input("enter the number to convert to binary"))
# # # # # # # # # # # # # # bits = []
# # # # # # # # # # # # # # while n >0:
# # # # # # # # # # # # # #     bits.append(n%2)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(bits)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #recursive:
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def dec_to_binary(n):
# # # # # # # # # # # # # #    if n > 1:
# # # # # # # # # # # # # #        dec_to_binary(n//2)
# # # # # # # # # # # # # #    print(n % 2,end = '')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # num = int(input("Your decimal number: "))
# # # # # # # # # # # # # # dec_to_binary(num)
# # # # # # # # # # # # # # print(" ")
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # #<TBD>
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = input("enter the BINARY number to convert to DECIMAL")
# # # # # # # # # # # # # # s = int(n,2)
# # # # # # # # # # # # # # print(s)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #reverse a number
# # # # # # # # # # # # #
# # # # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # rev = 0
# # # # # # # # # # # # # # while n >0:
# # # # # # # # # # # # # #     ld = n%10
# # # # # # # # # # # # # #     rev = rev*10 + ld
# # # # # # # # # # # # # #     n = n//10
# # # # # # # # # # # # # # print(rev)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Reverse a string
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def reverse_string(s):
# # # # # # # # # # # # # #     rev = ''
# # # # # # # # # # # # # #     for c in s:
# # # # # # # # # # # # # #         rev = c + rev
# # # # # # # # # # # # # #     return (rev)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # str = input("Enter your string: ")
# # # # # # # # # # # # # # result = reverse_string(str)
# # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # reverse a string (stack)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def reverse_string(s):
# # # # # # # # # # # # # #     st = []
# # # # # # # # # # # # # #     for c in s:
# # # # # # # # # # # # # #         st.append(c)
# # # # # # # # # # # # # #     print(st)
# # # # # # # # # # # # # #     rev = ''
# # # # # # # # # # # # # #     while len(st) > 0:
# # # # # # # # # # # # # #         last = st.pop()
# # # # # # # # # # # # # #         rev = rev + last
# # # # # # # # # # # # # #     return (rev)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # str = input("Enter your string: ")
# # # # # # # # # # # # # # result = reverse_string(str)
# # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # #reverse a string using recursive
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def revr(s):
# # # # # # # # # # # # # #     if len(s) == 0:
# # # # # # # # # # # # # #         return s
# # # # # # # # # # # # # #     return revr(s[1:]) + s[0]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(revr("karthik"))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def reverse_words(sentence):
# # # # # # # # # # # # # #     words = sentence.split()
# # # # # # # # # # # # # #     words.reverse()
# # # # # # # # # # # # # #     return " ".join(words)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # usr_input = input("Enter a sentence: ")
# # # # # # # # # # # # # # reverse = reverse_words(usr_input)
# # # # # # # # # # # # # # print('Reversed words are: ', reverse)
# # # # # # # # # # # # #
# # # # # # # # # # # # # ####
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def h(a):
# # # # # # # # # # # # # #     import itertools
# # # # # # # # # # # # # #     kar = sorted(list(itertools.permutations(a)), reverse=True)
# # # # # # # # # # # # # #     for k in kar:
# # # # # # # # # # # # # #         h,i,j,p = k
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         hour = (h*10+i)
# # # # # # # # # # # # # #         min = (j*10+p)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         if hour < 24 and min <60:
# # # # # # # # # # # # # #             return f"{h}{i}:{j}{p}"
# # # # # # # # # # # # # #     return " "
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # a = [1,2,3,4]
# # # # # # # # # # # # # # print(h(a))
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def three(no):
# # # # # # # # # # # # # #     no.sort()
# # # # # # # # # # # # # #     triplets = []
# # # # # # # # # # # # # #     for i in range(len(no)-2):
# # # # # # # # # # # # # #         left = i+1
# # # # # # # # # # # # # #         right = len(no) - 1
# # # # # # # # # # # # # #         while left < right:
# # # # # # # # # # # # # #             cs = no[i] + no[left] + no[right]
# # # # # # # # # # # # # #             if no[i] + no[left] + no[right] == 0:
# # # # # # # # # # # # # #                 triplets.append([no[i],  no[left], no[right]])
# # # # # # # # # # # # # #                 left += 1
# # # # # # # # # # # # # #                 right -= 1
# # # # # # # # # # # # # #             elif cs < 0:
# # # # # # # # # # # # # #                 left += 1
# # # # # # # # # # # # # #             elif cs > 0:
# # # # # # # # # # # # # #                 right -= 1
# # # # # # # # # # # # # #     return triplets
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # no = [-1, 0, 1, 2, -1, -4]
# # # # # # # # # # # # # # print(three(no))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def two(no, ts):
# # # # # # # # # # # # # #     no.sort()
# # # # # # # # # # # # # #     doubles = []
# # # # # # # # # # # # # #     left = 0
# # # # # # # # # # # # # #     right = len(no) -1
# # # # # # # # # # # # # #     while left < right:
# # # # # # # # # # # # # #         cs = no[left] + no[right]
# # # # # # # # # # # # # #         if ts == cs:
# # # # # # # # # # # # # #             doubles.append([no[left], no[right]])
# # # # # # # # # # # # # #             left += 1
# # # # # # # # # # # # # #             right -= 1
# # # # # # # # # # # # # #         elif cs < ts:
# # # # # # # # # # # # # #             left += 1
# # # # # # # # # # # # # #         elif cs > ts:
# # # # # # # # # # # # # #             right -= 1
# # # # # # # # # # # # # #     return doubles
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # no = [-3,5,-4,8,11,1,-1,6]
# # # # # # # # # # # # # # ts = 10
# # # # # # # # # # # # # # print(two(no, ts))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def uni(s):
# # # # # # # # # # # # # #     d = {}
# # # # # # # # # # # # # #     for c in s:
# # # # # # # # # # # # # #         if c not in d:
# # # # # # # # # # # # # #             d[c] = 1
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             d[c] += 1
# # # # # # # # # # # # # #     print(d)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for i in range(len(s)):
# # # # # # # # # # # # # #         if d[s[i]] == 1:
# # # # # # # # # # # # # #             return i
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # s = "loveleetcode"
# # # # # # # # # # # # # # print(uni(s))
# # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def maxsa(array):
# # # # # # # # # # # # # #     maxending = array[0]
# # # # # # # # # # # # # #     maxsofar = array[0]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for i in range(1, len(array)):
# # # # # # # # # # # # # #         num = array[i]
# # # # # # # # # # # # # #         maxending = max(num, maxending + num)
# # # # # # # # # # # # # #         maxsofar = max(maxending, maxsofar)
# # # # # # # # # # # # # #     return maxsofar
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # array = [-2,1,-3,4,-1,2,1,-5,4]
# # # # # # # # # # # # # # print(maxsa(array))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def over(li):
# # # # # # # # # # # # # #     li.sort(key=lambda li:li[0])
# # # # # # # # # # # # # #     print(li)
# # # # # # # # # # # # # #     i = 1
# # # # # # # # # # # # # #     while i < len(li):
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         if li[i][0] <= li[i-1][1]:
# # # # # # # # # # # # # #             li[i-1][0] = min(li[i-1][0], li[i][0])
# # # # # # # # # # # # # #             li[i-1][1] = max(li[i-1][1], li[i][1])
# # # # # # # # # # # # # #             li.pop(i)
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             i += 1
# # # # # # # # # # # # # #     return li
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # li = [[1,3], [8,10], [2,6],  [15,18]]
# # # # # # # # # # # # # # print(over(li))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # lm = lambda y:y*y*y
# # # # # # # # # # # # # # print(lm(5))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # li = [1,2,3,4,5,6,7,8,9]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # final = list(map(lambda x: (x%2 != 0), li))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(final)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # def over(li, newli):
# # # # # # # # # # # # # #     i = 0
# # # # # # # # # # # # # #     res = []
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     while i < len(li) and newli[0] > li[i][0]:
# # # # # # # # # # # # # #         res.append(li[i])
# # # # # # # # # # # # # #         i += 1
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # li = [[1,3], [6,9]]
# # # # # # # # # # # # # # newli = [2,5]
# # # # # # # # # # # # # # print(over(li, newli))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def most(st):
# # # # # # # # # # # # # #     word = {}
# # # # # # # # # # # # # #     words = st.split()
# # # # # # # # # # # # # #     print(words)
# # # # # # # # # # # # # #     most_frequent_words = []
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for w in words:
# # # # # # # # # # # # # #         if w in word:
# # # # # # # # # # # # # #             word[w] += 1
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             word[w] = 1
# # # # # # # # # # # # # #     print(word)
# # # # # # # # # # # # # #     maxvalue = min(word.values())
# # # # # # # # # # # # # #     print(maxvalue)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for wor, val in word.items():
# # # # # # # # # # # # # #         if val == maxvalue:
# # # # # # # # # # # # # #             most_frequent_words.append(wor)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for wo in sorted(most_frequent_words):
# # # # # # # # # # # # # #         print(wo)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     return most_frequent_words
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # st = "hello my name is hello joanne is"
# # # # # # # # # # # # # # print(most(st))
# # # # # # # # # # # # # # import math
# # # # # # # # # # # # # # def dist(points,k):
# # # # # # # # # # # # # #     d = [ (math.sqrt(point[0]**2 + point[1]**2),point) for point in points]
# # # # # # # # # # # # # #     print(d)
# # # # # # # # # # # # # #     return [po for di, po in sorted(d)[:k]]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # points = [[1,3], [-2,2]]
# # # # # # # # # # # # # # k = 1
# # # # # # # # # # # # # # print(dist(points,k))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def wa(arr):
# # # # # # # # # # # # # #     arr.sort()
# # # # # # # # # # # # # #     print(arr)
# # # # # # # # # # # # # #     wt = 0
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for idx, value in enumerate(arr):
# # # # # # # # # # # # # #         al = len(arr) - (idx + 1)
# # # # # # # # # # # # # #         print(al)
# # # # # # # # # # # # # #         wt += al * value
# # # # # # # # # # # # # #     return wt
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # arr = [3,2,1,2,6]
# # # # # # # # # # # # # # print(wa(arr))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # 0 + 1 + (2+1) +(2+2+1) + (1+2+2+3)
# # # # # # # # # # # # # # 1+3+5+8
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def sortedSquaredArray(array):
# # # # # # # # # # # # # #     # Write your code here.
# # # # # # # # # # # # # #     out = [0 for _ in array]
# # # # # # # # # # # # # #     si = 0
# # # # # # # # # # # # # #     ei = len(array) - 1
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for idx in reversed(range(len(array))):
# # # # # # # # # # # # # #         sv = array[si]
# # # # # # # # # # # # # #         bv = array[ei]
# # # # # # # # # # # # # #         print(sv, bv)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         if abs(sv) > abs(bv):
# # # # # # # # # # # # # #             out[idx] = sv * sv
# # # # # # # # # # # # # #             si += 1
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             out[idx] = bv * bv
# # # # # # # # # # # # # #             ei -= 1
# # # # # # # # # # # # # #     return out
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # array = [-9,-8, -7, 1,2,3,5,6,8,9]
# # # # # # # # # # # # # # print(sortedSquaredArray(array))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def findKthLargestValueInBst(tree, k):
# # # # # # # # # # # # # #     # Write your code here.
# # # # # # # # # # # # # #     array = []
# # # # # # # # # # # # # #     reverseiot(tree, node)
# # # # # # # # # # # # # #     return array[]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # def reverseiot(node, array):
# # # # # # # # # # # # # #     if node is None:
# # # # # # # # # # # # # #         return
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     reverseiot(node.right, array)
# # # # # # # # # # # # # #     array.append(node.value)
# # # # # # # # # # # # # #     reverseiot(node.left, array)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # tree = [22, 20, ]
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def isp(s):
# # # # # # # # # # # # # #     s.replace(" ", "")
# # # # # # # # # # # # # #     s1 = ""
# # # # # # # # # # # # # #     for i in s:
# # # # # # # # # # # # # #         j = i.lower()
# # # # # # # # # # # # # #         if j.isalnum():
# # # # # # # # # # # # # #             s1 += j
# # # # # # # # # # # # # #     print(s1)
# # # # # # # # # # # # # #     print(s1[::-1])
# # # # # # # # # # # # # #     return s1 == s1[::-1]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # s = "race a car"
# # # # # # # # # # # # # # print(isp(s))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def rep(s):
# # # # # # # # # # # # # #     s = s.replace('-', '')
# # # # # # # # # # # # # #     s = s.title()
# # # # # # # # # # # # # #     s = s.replace(' ','')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     print(s)
# # # # # # # # # # # # # #     genie_parser = "ShowPlatformHardwareFedSwActiveFwdasicResourceTcamUtilization"
# # # # # # # # # # # # # #     if s == genie_parser:
# # # # # # # # # # # # # #         return True
# # # # # # # # # # # # # #     return False
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # s = "show platform hardware fed sw active fwd-asic resource tcam utilization"
# # # # # # # # # # # # # # print(rep(s))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # d = '(devices (device CAT9K-24))', '(thresholds (max-threshold 0) (used-threshold 1) (percent-used-threshold 1))', '(reporting (healthy 0) (degraded 1))'
# # # # # # # # # # # # # # dic = {}
# # # # # # # # # # # # # # print(d)
# # # # # # # # # # # # # # for di in d:
# # # # # # # # # # # # # #     print(di)
# # # # # # # # # # # # # #     l = list(di)
# # # # # # # # # # # # # #     print(l)
# # # # # # # # # # # # # #     print(dict(l))
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # a,b,c = d
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # import ast
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # a = '''
# # # # # # # # # # # # # # '(devices (device CAT9K-24))', '(thresholds (max-threshold 0) (used-threshold 1) (percent-used-threshold 1))', '(reporting (healthy 0) (degraded 1))
# # # # # # # # # # # # # # '''
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # a = a.replace('(','{').replace(')','}').replace(' ',':').replace(',:',',')
# # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # d = {'devices': {'device': 'CAT9K-24'}, 'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}, 'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for key in d.keys():
# # # # # # # # # # # # # #     print(key)
# # # # # # # # # # # # # #     print(d[key])
# # # # # # # # # # # # # #     for k in d[key]:
# # # # # # # # # # # # # #         print(k)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # a = '''
# # # # # # # # # # # # # # d = '(devices (device CAT9K-24))', '(thresholds (max-threshold 0) (used-threshold 1) (percent-used-threshold 1))', '(reporting (healthy 0) (degraded 1))"
# # # # # # # # # # # # # # '''
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # a = a.strip('\n')
# # # # # # # # # # # # # # a = a.split('=')[1]
# # # # # # # # # # # # # # for l in a.split(','):
# # # # # # # # # # # # # #     l = l.replace('(','').replace(')','').replace("'",'').replace('"','')
# # # # # # # # # # # # # #     l = l.strip("'")
# # # # # # # # # # # # # #     l = l.split()
# # # # # # # # # # # # # #     key = l[0].strip('\n')
# # # # # # # # # # # # # #     print('{}:'.format(key))
# # # # # # # # # # # # # #     for i in range(1, len(l), 2):
# # # # # # # # # # # # # #         key1 = l[i].strip('\n')
# # # # # # # # # # # # # #         val1 = l[i+1].strip('\n')
# # # # # # # # # # # # # #         print('\t{}: {}'.format(str(key1),str(val1)))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = [
# # # # # # # # # # # # # # {'devices': {'device': 'CAT9K-24'},
# # # # # # # # # # # # # # {'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'},
# # # # # # # # # # # # # # {'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # # # ]
# # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = [
# # # # # # # # # # # # # # {'devices': {'device': 'CAT9K-24'}},
# # # # # # # # # # # # # # {'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}},
# # # # # # # # # # # # # # {'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # # # ]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(initial_facts)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # for key in initial_facts:
# # # # # # # # # # # # # #     print(key)
# # # # # # # # # # # # # #     for k,v in key.items():
# # # # # # # # # # # # # #         print(k)
# # # # # # # # # # # # # #         print(v)
# # # # # # # # # # # # # #         for vi in v:
# # # # # # # # # # # # # #             print(vi)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # # initial_facts = "{'devices': {'device': 'CAT9K-24'}}, {'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}}, {'reporting': {'healthy': '0', 'degraded': '1'}}"
# # # # # # # # # # # # # # print(initial_facts)
# # # # # # # # # # # # # # i_f = json.loads(initial_facts)
# # # # # # # # # # # # # # print(i_f)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #initial_facts = "{'devices': {'device': 'CAT9K-24'}}, {'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}}, {'reporting': {'healthy': '0', 'degraded': '1'}}"
# # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = '{ "devices":{"device":"CAT9K-24"}, "thresholds":{"max-threshold":"0", "used-threshold":"1","percent-used-threshold":"1"},"reporting":{"healthy":"0","degraded":"1"}}'
# # # # # # # # # # # # #
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # # result = json.loads(initial_facts)
# # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # # # print(type(result))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for key in result.items():
# # # # # # # # # # # # # #     print(key)
# # # # # # # # # # # # # #     di = dict(key)
# # # # # # # # # # # # # #     print(di)
# # # # # # # # # # # # # #     # key = dict(key)
# # # # # # # # # # # # # #     # for key1 in key.items():
# # # # # # # # # # # # # #     #     print(key1)
# # # # # # # # # # # # # #     #
# # # # # # # # # # # # # #     #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # initial_facts = ["{'devices': {'device': 'CAT9K-24'}}, {'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}}, {'reporting': {'healthy': '0', 'degraded': '1'}}"]
# # # # # # # # # # # # # # # for key in initial_facts:
# # # # # # # # # # # # # # #     for k1,v1 in key.items(): # the basic way
# # # # # # # # # # # # # # #         temp = ""
# # # # # # # # # # # # # # #         temp+=k1
# # # # # # # # # # # # # # #         print(temp)
# # # # # # # # # # # # # # #         for k2,v2 in v1.items():
# # # # # # # # # # # # # # #             print(k2)
# # # # # # # # # # # # # # #             #print(v2)
# # # # # # # # # # # # # # #             #temp = temp+" "+str(k2)+" "+str(v2)
# # # # # # # # # # # # # # #         #print(temp)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #{'devices': {'device': 'CAT9K-24'}}, {'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}}, {'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = "{'devices': {'device': 'CAT9K-24'}}, {'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}}, {'reporting': {'healthy': '0', 'degraded': '1'}}"
# # # # # # # # # # # # # # # # import ast
# # # # # # # # # # # # # # # # result = ast.literal_eval(initial_facts)
# # # # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # # # # initial_facts = eval(initial_facts)
# # # # # # # # # # # # # # # print(initial_facts)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = '{ "devices":{"device":"CAT9K-24"} "thresholds":{"max-threshold":"0", "used-threshold":"1","percent-used-threshold":"1"} "reporting":{"healthy":"0","degraded":"1"}}'
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # # result = json.loads(initial_facts)
# # # # # # # # # # # # # # d = dict()
# # # # # # # # # # # # # # for key in result.items():
# # # # # # # # # # # # # #   print("key is {}".format(key))
# # # # # # # # # # # # # #   d[key[0]] = key[1]
# # # # # # # # # # # # # #   print(str(d))
# # # # # # # # # # # # # # print(type(d))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for di in d.items():
# # # # # # # # # # # # # #     print(di)
# # # # # # # # # # # # # #     for die in di.items():
# # # # # # # # # # # # # #         print(die)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = '{ "devices":{"device":"CAT9K-24"}, "thresholds":{"max-threshold":"0","used-threshold":"1","percent-used-threshold":"1"}, "reporting":{"healthy":"0","degraded":"1"}}'
# # # # # # # # # # # # # # print(initial_facts)
# # # # # # # # # # # # # # print(type(initial_facts))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import ast
# # # # # # # # # # # # # # facts_dict = ast.literal_eval(initial_facts)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(facts_dict)
# # # # # # # # # # # # # # print(type(facts_dict))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for fd, value in facts_dict.items():
# # # # # # # # # # # # # #     print(fd)
# # # # # # # # # # # # # #     print(value)
# # # # # # # # # # # # # #     for v in value:
# # # # # # # # # # # # # #         print(v)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = '{ "devices" : {"device":"CAT9K-24"} , "thresholds":{"max-threshold":"0","used-threshold":"1","percent-used-threshold":"1"} , "reporting":{"healthy":"0","degraded":"1"}}'
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # # result = json.loads(initial_facts)
# # # # # # # # # # # # # # d = dict()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for key in result.items():
# # # # # # # # # # # # # #   print("key is {}".format(key))
# # # # # # # # # # # # # #   d[key[0]] = key[1]
# # # # # # # # # # # # # # for i in d.keys():
# # # # # # # # # # # # # #     print(type(i), type(d[i]))
# # # # # # # # # # # # # #     print('{} : {}'.format(i,d[i]))
# # # # # # # # # # # # # #     for j in d[i].keys():
# # # # # # # # # # # # # #         print(type(j), type(d[i][j]))
# # # # # # # # # # # # # #         print('{} : {}'.format(j, d[i][j]))
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # #working
# # # # # # # # # # # # # #{'devices': {'device': 'CAT9K-24'}, 'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}, 'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # result = json.loads(initial_facts)
# # # # # # # # # # # # # # d = dict()
# # # # # # # # # # # # # # d2 = dict()
# # # # # # # # # # # # # # d3 = dict()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for key in result.items():
# # # # # # # # # # # # # #   print("key is {}".format(key))
# # # # # # # # # # # # # #   d[key[0]] = key[1]
# # # # # # # # # # # # # #   print(str(d))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for i in d.items():
# # # # # # # # # # # # # #     print(type(i))
# # # # # # # # # # # # # #     d2[list(i)[0]] = list(i)[1]
# # # # # # # # # # # # # #     print(str(d2))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for i in d2.items():
# # # # # # # # # # # # # #     print(type(i))
# # # # # # # # # # # # # #     d3[list(i)[0]] = list(i)[1]
# # # # # # # # # # # # # #     print(str(d3))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for die in d3.items():
# # # # # # # # # # # # # #     print(die)
# # # # # # # # # # # # # #     for i in die.items():
# # # # # # # # # # # # # #         print(i)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # initial_facts = {'devices': {'device': 'CAT9K-24'}, 'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'}, 'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for di, value in initial_facts.items():
# # # # # # # # # # # # # #     print(di)
# # # # # # # # # # # # # #     print(value)
# # # # # # # # # # # # # #     for v,vi in value.items():
# # # # # # # # # # # # # #         print(v)
# # # # # # # # # # # # # #         print(vi)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import pprint
# # # # # # # # # # # # # # f_l = {'fact_type': 'show_and_assert', 'device-index': 0, 'device': 'cat9k-24', 'access-method': 'cli', 'command': 'show platform hardware fed sw active fwd-asic resource tcam utilization', 'genie_parser': 'ShowPlatformHardwareFedSwActiveFwdasicResourceTcamUtilization', 'assert_fact_for_each_item_in': 'tcam-table', 'protofact': {'template': 'tcam-util', 'slots': {'dir': '$+dir', 'max': '$+max', 'used': '$+used', 'percent-used': '$+percent-used', 'v4': '$+v4', 'v6': '$+v6', 'mpls': '$+mpls', 'other': '$+other'}}}
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #pprint.pformat(f_l)
# # # # # # # # # # # # # # kar = pprint.pformat(f_l)
# # # # # # # # # # # # # # print([kar])
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # {"fact_type": "show_and_assert",
# # # # # # # # # # # # # # "device-index": 0,
# # # # # # # # # # # # # # "device": 'CAT9K-24',
# # # # # # # # # # # # # # "access-method": 'cli',
# # # # # # # # # # # # # # "command": 'show platform hardware fed sw active fwd-asic resource tcam utilization',
# # # # # # # # # # # # # # "genie_parser": "ShowPlatformHardwareFedSwActiveFwdasicResourceTcamUtilization",
# # # # # # # # # # # # # # "assert_fact_for_each_item_in": "tcam_table+application",
# # # # # # # # # # # # # # "protofact": {"template": "tcam-stats",
# # # # # # # # # # # # # #               "slots": {"table": "$",
# # # # # # # # # # # # # #                         "dir": "$+dir",
# # # # # # # # # # # # # #                         "max": "$+max",
# # # # # # # # # # # # # #                         "used": "$+used",
# # # # # # # # # # # # # #                         "percent-used": "$+percent-used",
# # # # # # # # # # # # # #                         "v4": "$+v4",
# # # # # # # # # # # # # #                         "v6": "$+v6",
# # # # # # # # # # # # # #                         "mpls": "$+mpls",
# # # # # # # # # # # # # #                         "other": "$+other"
# # # # # # # # # # # # # #                        }
# # # # # # # # # # # # # #               }
# # # # # # # # # # # # # # # }
# # # # # # # # # # # # #
# # # # # # # # # # # # # # service_impact = '''
# # # # # # # # # # # # # # <send-notification xmlns="http://cisco.com/ns/yang/cisco-ios-xe-ddr-control">
# # # # # # # # # # # # # #     <description>{0}</description>
# # # # # # # # # # # # # #     <messages>
# # # # # # # # # # # # # # {1}    </messages>
# # # # # # # # # # # # # #     <clips-facts>
# # # # # # # # # # # # # # {2}    </clips-facts>
# # # # # # # # # # # # # #     <dict-facts>
# # # # # # # # # # # # # # {3}    </dict-facts>
# # # # # # # # # # # # # #   </send-notification>
# # # # # # # # # # # # # # '''
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print("si: {}".format(service_impact))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # {'devices': {'device': 'CAT9K-24'},
# # # # # # # # # # # # # #  'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'},
# # # # # # # # # # # # # #  'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #  <send-notification xmlns="http://cisco.com/ns/yang/cisco-ios-xe-ddr-control">
# # # # # # # # # # # # # #     <description>{0}</description>
# # # # # # # # # # # # # #     <messages>
# # # # # # # # # # # # # # {1}    </messages>
# # # # # # # # # # # # # #     <clips-facts>
# # # # # # # # # # # # # # {2}    </clips-facts>
# # # # # # # # # # # # # #     <dict-facts>
# # # # # # # # # # # # # # {3}    </dict-facts>
# # # # # # # # # # # # # #   </send-notification>
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # UPLOAD_FOLDER = '/Users/kharicha/Desktop/eMRE/DDR/web/my_dir/forms/upload_files/'
# # # # # # # # # # # # # # # filename = "kar.txt"
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # fn = UPLOAD_FOLDER + filename
# # # # # # # # # # # # # # # print(fn)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # import os
# # # # # # # # # # # # # # filenames = "ddr-devices.txt"
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(filenames)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for filename in filenames:
# # # # # # # # # # # # # #     os.rename(filename, filename.replace(" ", "-"))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(filename)
# # # # # # # # # # # # #
# # # # # # # # # # # # # import re
# # # # # # # # # # # # #
# # # # # # # # # # # # # # filename = "ddr-devices (1).txt"
# # # # # # # # # # # # # # # fn = re.sub(r'\([^)]*\)', '', filename)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # fn = re.sub(r" ?\([^)]+\)", "", filename)
# # # # # # # # # # # # # # fn = fn.replace(".txt", "")
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(fn)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # fn = "ddr-devices_1.txt"
# # # # # # # # # # # # # # fn = fn.split('_')
# # # # # # # # # # # # # # print(fn)
# # # # # # # # # # # # # # fn = fn[0].replace('.txt','')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #fn = re.sub('_.{*}', '', fn).replace('.txt', '')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(fn)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # mgmt_ip = "172.27.255.24"
# # # # # # # # # # # # # # start= ['telnet' + ' '+ mgmt_ip]
# # # # # # # # # # # # # # print(start)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def oi(intervals):
# # # # # # # # # # # # # #     print(intervals)
# # # # # # # # # # # # # #     si = sorted(intervals, key=lambda x:x[0])
# # # # # # # # # # # # # #     print(si)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     mi = []
# # # # # # # # # # # # # #     ci = si[0]
# # # # # # # # # # # # # #     mi.append(ci)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     for ni in si:
# # # # # # # # # # # # # #         cis, cie = ci
# # # # # # # # # # # # # #         nis, nie = ni
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         if cie >= nis:
# # # # # # # # # # # # # #             ci[1] = max(cie,nie)
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             ci = ni
# # # # # # # # # # # # # #             mi.append(ci)
# # # # # # # # # # # # # #     return mi
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # intervals = [[1,2], [3,5], [6,8], [4,7], [9,10]]
# # # # # # # # # # # # # # print(oi(intervals))
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # Statement(pattern=r'.*Do you wish to proceed anyway\? \(y/n\)\s*\[n\]',
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # pattern=r'configuration. Enter Y if you are sure you want to proceed. ? [no]:'
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # Delete filename \[/guest-share/ddr/ddr-devices\]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # pattern=r'.*Enter Y if you are sure you want to proceed. \? \[no\].*'
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # dialog = Dialog([
# # # # # # # # # # # # # # Statement(pattern=r'Partition command reloads the switch, Continue?[confirm]',
# # # # # # # # # # # # # # action='sendline()',
# # # # # # # # # # # # # # loopcontinue=True,
# # # # # # # # # # # # # # continuetimer=False)
# # # # # # # # # # # # # # (pattern=r'Partition operation will destroy all data in \"sdflash:\". Continue?[confirm]',
# # # # # # # # # # # # # # action='sendline()',
# # # # # # # # # # # # # # loopcontinue=True,
# # # # # # # # # # # # # # continuetimer=False)
# # # # # # # # # # # # # # (pattern=r'Partition command will not work on flash',
# # # # # # # # # # # # # # action='sendline()',
# # # # # # # # # # # # # # loopcontinue=True,
# # # # # # # # # # # # # # continuetimer=False)
# # # # # # # # # # # # # # ])
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # **** DDR Debug: Main fact loop: {'fact_type': 'show_and_assert',
# # # # # # # # # # # # # #                                  'device-index': 0, 'device': 'CAT9K-24', 'access-method': 'cli',
# # # # # # # # # # # # # #                                  'command': 'show platform hardware fed sw active fwd-asic resource tcam utilization',
# # # # # # # # # # # # # #                                  'genie_parser': 'ShowPlatformHardwareFedSwActiveFwdasicResourceTcamUtilization',
# # # # # # # # # # # # # #                                  'assert_fact_for_each_item_in': 'tcam_table+application',
# # # # # # # # # # # # # #                                  'protofact': {'template': 'tcam-stats', 'slots':
# # # # # # # # # # # # # #                                      {'table': '$', 'dir': '$+dir', 'max': '$+max', 'used': '$+used', 'percent-used': '$+percent-used',
# # # # # # # # # # # # # #                                       'v4': '$+v4', 'v6': '$+v6', 'mpls': '$+mpls', 'other': '$+other'}}}
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # **** DDR Debug: Main fact loop: {'fact_type': 'show_and_assert',
# # # # # # # # # # # # # #                                  'device-index': 0, 'device': 'CAT9k-24', 'access-method': 'cli',
# # # # # # # # # # # # # #                                  'command': 'show platform hardware fed sw active fwd-asic resource tcam utilization',
# # # # # # # # # # # # # #                                  'genie_parser': 'ShowPlatformHardwareFedSwActiveFwdasicResourceTcamUtilization',
# # # # # # # # # # # # # #                                  'assert_fact_for_each_item_in': 'tcam_table+application',
# # # # # # # # # # # # # #                                  'protofact': {'template': 'tcam-stats', 'slots':
# # # # # # # # # # # # # #                                      {'table': '$', 'dir': '$+dir', 'max': '$+max', 'used': '$+used', 'percent-used': '$+percent-used',
# # # # # # # # # # # # # #                                       'v4': '$+v4', 'v6': '$+v6', 'mpls': '$+mpls', 'other': '$+other'}}}
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # fact_type = "show_and_assert"
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # fact = {"fact_type": fact_type}
# # # # # # # # # # # # # # print(fact)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # fkey = "karthik"
# # # # # # # # # # # # # # fkey += "+"
# # # # # # # # # # # # # # skey = "babu"
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # kar = fkey+skey
# # # # # # # # # # # # # # print(kar)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # import re
# # # # # # # # # # # # # # import os
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # a = "<interfaces xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper'> <interface> <name/> <statistics> <in-errors/> <in-crc-errors/> <in-errors-64/> </statistics> </interface> </interfaces>"
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # c = a.split()
# # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # # print(type(c))
# # # # # # # # # # # # # # finalrpc = ""
# # # # # # # # # # # # # # for b in c:
# # # # # # # # # # # # # #     finalrpc += b + os.linesep
# # # # # # # # # # # # # # print(finalrpc[:-1].replace('\n', ''))
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # c = a.split(" ")
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # a = " <interfaces xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper'>
# # # # # # # # # # # # # # <interface>
# # # # # # # # # # # # # # <name/>
# # # # # # # # # # # # # # <statistics>
# # # # # # # # # # # # # # <in-errors/>
# # # # # # # # # # # # # # <in-crc-errors/>
# # # # # # # # # # # # # # <in-errors-64/>
# # # # # # # # # # # # # # </statistics>
# # # # # # # # # # # # # # </interface>
# # # # # # # # # # # # # # </interfaces>
# # # # # # # # # # # # # #     "
# # # # # # # # # # # # # # e = []
# # # # # # # # # # # # # # c = a.split(" ")
# # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # # for b in c:
# # # # # # # # # # # # # #     print(b)
# # # # # # # # # # # # # #     out = re.search('<(.*)/>', b)
# # # # # # # # # # # # # #     if out:
# # # # # # # # # # # # # #         e.append(out.group(1))
# # # # # # # # # # # # # # print(e)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # c = re.split(')
# # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # c = a.split('\n')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for b in c:
# # # # # # # # # # # # # #     print(b)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # print(a.splitlines())
# # # # # # # # # # # # # # a = a.splitlines()
# # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # c = []
# # # # # # # # # # # # # # for b  in a:
# # # # # # # # # # # # # #     print(b)
# # # # # # # # # # # # # #     out = re.search('<(.*)/>',b)
# # # # # # # # # # # # # #     c.append(out.group(1))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # import re
# # # # # # # # # # # # # # # s = ['This sentence is correct.','This sentence is not correct', 'Something is !wrong! here.','"This is an example of *correct* sentence."']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # What I tried so for is:
# # # # # # # # # # # # # # # for i in s:
# # # # # # # # # # # # # # #     print(re.match('^[A-Z][^?!.]*[?.!]$', i) is not None)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # filename = "ddr-devices (1).txt"
# # # # # # # # # # # # # # # fn = re.sub(r'\([^)]*\)', '', filename)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # with open('/Users/kharicha/Desktop/eMRE/DDR/web/my_dir/forms/countries.txt','r') as file:
# # # # # # # # # # # # # #     countriesStr = file.read()
# # # # # # # # # # # # # # print(countriesStr)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # with open('/Users/kharicha/Desktop/eMRE/DDR/web/my_dir/forms/ddr-mt.txt','r') as file:
# # # # # # # # # # # # # #     mtfact = file.read()
# # # # # # # # # # # # # # print(mtfact)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # from pathlib import Path
# # # # # # # # # # # # # # countriesStr=Path('/Users/kharicha/Desktop/eMRE/DDR/web/my_dir/forms/ddr-mt.txt').read_text()
# # # # # # # # # # # # # # print(countriesStr)
# # # # # # # # # # # # #
# # # # # # # # # # # # # f = open("/Users/kharicha/Desktop/eMRE/DDR/web/my_dir/forms/ddr-mt.txt", mode='r', encoding='utf-8')
# # # # # # # # # # # # # kar = f.readlines()
# # # # # # # # # # # # # print(kar)
# # # # # # # # # # # # # for k in kar:
# # # # # # # # # # # # #     print(k)
# # # # # # # # # # # # #
# # # # # # # # # # # # # {'devices': {'device': 'CAT9K-24'},
# # # # # # # # # # # # # 'thresholds': {'max-threshold': '0', 'used-threshold': '1', 'percent-used-threshold': '1'},
# # # # # # # # # # # # # 'reporting': {'healthy': '0', 'degraded': '1'}}
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # {'devices': {'device': 'CAT9K-24'},
# # # # # # # # # # # # 'int-thresholds': {'in-errors': '1000', 'in-crc-errors': '1000', 'in-errors-64': '1000', 'in-oversize-frames': '1000'},
# # # # # # # # # # # # 'reporting': {'healthy': '0', 'degraded': '1'},
# # # # # # # # # # # # 'interface-error-state': {'device': 'CAT9K-24', 'name': 'GigabitEthernet0/0'},
# # # # # # # # # # # # 'interface-error-state': {'device': 'CAT9K-24', 'name': 'GigabitEthernet1/0/1'}}
# # # # # # # # # # # # #
# # # # # # # # # # # # # keyfil = []
# # # # # # # # # # # # #
# # # # # # # # # # # # # if keyfil:
# # # # # # # # # # # # #     print("karthik")
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # aaa_configs = service.inventory['cat9k-24'].exec(["config terminal", "aaa new-model", "aaa authentication login default local", "aaa authentication login CONSOLE none", " aaa authentication enable default none", "aaa authorization exec default local", "aaa session-id common", "\x1a"]).wait()
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # c = ['ddmi-cat9300-2#show running-config', 'Building configuration...', '', 'Current configuration : 32429 bytes', '!', '! Last configuration change at 06:01:53 UTC Thu Apr 15 2021 by admin', '!', 'version 17.6', 'service timestamps debug datetime msec', 'service timestamps log datetime msec', 'service internal', 'service call-home', 'no platform punt-keepalive disable-kernel-core', '!', 'hostname ddmi-cat9300-2', '!', '!', 'vrf definition Mgmt-vrf', ' !', ' address-family ipv4', ' exit-address-family', ' !', ' address-family ipv6', ' exit-address-family', '!', 'logging discriminator nosel facility drops SELINUX', 'no logging console', 'logging monitor discriminator nosel', '!', 'aaa new-model', '!', '!', 'aaa authentication login default local', 'aaa authentication login CONSOLE none', 'aaa authentication login VTY_authen group dnac-network-radius-group local', 'aaa authentication login dnac-cts-list group dnac-client-radius-group local', 'aaa authentication enable default none', 'aaa authentication dot1x default group dnac-client-radius-group', 'aaa authorization exec default local', 'aaa authorization exec VTY_author group dnac-network-radius-group local if-authenticated', 'aaa authorization network default group dnac-client-radius-group', 'aaa authorization network dnac-cts-list group dnac-client-radius-group', 'aaa accounting update newinfo periodic 2880', 'aaa accounting identity default start-stop group dnac-client-radius-group', 'aaa accounting exec default start-stop group dnac-network-radius-group', '!', '!', '!', '!', '!', '!', 'aaa session-id common', 'ethernet cfm ieee', 'ethernet cfm domain genericstring level 3', '!', 'boot system switch all flash:cat9k_iosxe.2020-08-19_18.15_maniver2.SSA.bin', 'switch 1 provision c9300-24t', '!', '!', '!', '!', 'ip routing', '!', '!', '!', '!', '!', '!', '!', 'ip multicast-routing', 'ip bootp server', 'no ip domain lookup', '!', '!', '!', 'login on-success log', 'ipv6 unicast-routing', '!', '!', '!', '!', '!', '!', '!', 'mpls label mode all-vrfs protocol all-afs per-vrf', '!', 'parameter-map type subscriber attribute-to-service BUILTIN_DEVICE_TO_TEMPLATE', ' 10 map device-type regex "Cisco-IP-Phone"', '  20 interface-template IP_PHONE_INTERFACE_TEMPLATE', ' 20 map device-type regex "Cisco-IP-Camera"', '  20 interface-template IP_CAMERA_INTERFACE_TEMPLATE', ' 30 map device-type regex "Cisco-DMP"', '  20 interface-template DMP_INTERFACE_TEMPLATE', ' 40 map oui eq "00.0f.44"', '  20 interface-template DMP_INTERFACE_TEMPLATE', ' 50 map oui eq "00.23.ac"', '  20 interface-template DMP_INTERFACE_TEMPLATE', ' 60 map device-type regex "Cisco-AIR-AP"', '  20 interface-template AP_INTERFACE_TEMPLATE', ' 70 map device-type regex "Cisco-AIR-LAP"', '  20 interface-template LAP_INTERFACE_TEMPLATE', ' 80 map device-type regex "Cisco-TelePresence"', '  20 interface-template TP_INTERFACE_TEMPLATE', ' 90 map device-type regex "Surveillance-Camera"', '  10 interface-template MSP_CAMERA_INTERFACE_TEMPLATE', ' 100 map device-type regex "Video-Conference"', '  10 interface-template MSP_VC_INTERFACE_TEMPLATE', ' 110 map device-type regex "Cisco-CAT-LAP"', '  10 interface-template LAP_INTERFACE_TEMPLATE', '!', 'access-session mac-move deny', 'device-tracking policy IPDT_MAX_10', ' limit address-count 10', ' no protocol udp', '!', '!', '!', 'group-policy traffic-steering transport TLS', '!', 'crypto pki trustpoint SLA-TrustPoint', ' enrollment pkcs12', ' revocation-check crl', '!', 'crypto pki trustpoint TP-self-signed-71867858', ' enrollment selfsigned', ' subject-name cn=IOS-Self-Signed-Certificate-71867858', ' revocation-check none', ' rsakeypair TP-self-signed-71867858', '!', '!', 'crypto pki certificate chain SLA-TrustPoint', ' certificate ca 01', '  30820321 30820209 A0030201 02020101 300D0609 2A864886 F70D0101 0B050030', '  32310E30 0C060355 040A1305 43697363 6F312030 1E060355 04031317 43697363', '  6F204C69 63656E73 696E6720 526F6F74 20434130 1E170D31 33303533 30313934', '  3834375A 170D3338 30353330 31393438 34375A30 32310E30 0C060355 040A1305', '  43697363 6F312030 1E060355 04031317 43697363 6F204C69 63656E73 696E6720', '  526F6F74 20434130 82012230 0D06092A 864886F7 0D010101 05000382 010F0030', '  82010A02 82010100 A6BCBD96 131E05F7 145EA72C 2CD686E6 17222EA1 F1EFF64D', '  CBB4C798 212AA147 C655D8D7 9471380D 8711441E 1AAF071A 9CAE6388 8A38E520', '  1C394D78 462EF239 C659F715 B98C0A59 5BBB5CBD 0CFEBEA3 700A8BF7 D8F256EE', '  4AA4E80D DB6FD1C9 60B1FD18 FFC69C96 6FA68957 A2617DE7 104FDC5F EA2956AC', '  7390A3EB 2B5436AD C847A2C5 DAB553EB 69A9A535 58E9F3E3 C0BD23CF 58BD7188', '  68E69491 20F320E7 948E71D7 AE3BCC84 F10684C7 4BC8E00F 539BA42B 42C68BB7', '  C7479096 B4CB2D62 EA2F505D C7B062A4 6811D95B E8250FC4 5D5D5FB8 8F27D191', '  C55F0D76 61F9A4CD 3D992327 A8BB03BD 4E6D7069 7CBADF8B DF5F4368 95135E44', '  DFC7C6CF 04DD7FD1 02030100 01A34230 40300E06 03551D0F 0101FF04 04030201', '  06300F06 03551D13 0101FF04 05300301 01FF301D 0603551D 0E041604 1449DC85', '  4B3D31E5 1B3E6A17 606AF333 3D3B4C73 E8300D06 092A8648 86F70D01 010B0500', '  03820101 00507F24 D3932A66 86025D9F E838AE5C 6D4DF6B0 49631C78 240DA905', '  604EDCDE FF4FED2B 77FC460E CD636FDB DD44681E 3A5673AB 9093D3B1 6C9E3D8B', '  D98987BF E40CBD9E 1AECA0C2 2189BB5C 8FA85686 CD98B646 5575B146 8DFC66A8', '  467A3DF4 4D565700 6ADF0F0D CF835015 3C04FF7C 21E878AC 11BA9CD2 55A9232C', '  7CA7B7E6 C1AF74F6 152E99B7 B1FCF9BB E973DE7F 5BDDEB86 C71E3B49 1765308B', '  5FB0DA06 B92AFE7F 494E8A9E 07B85737 F3A58BE1 1A48A229 C37C1E69 39F08678', '  80DDCD16 D6BACECA EEBC7CF9 8428787B 35202CDC 60E4616A B623CDBD 230E3AFB', '  418616A9 4093E049 4D10AB75 27E86F73 932E35B5 8862FDAE 0275156F 719BB2F0', '  D697DF7F 28', '  quit', 'crypto pki certificate chain TP-self-signed-71867858', ' certificate self-signed 01', '  3082032C 30820214 A0030201 02020101 300D0609 2A864886 F70D0101 05050030', '  2F312D30 2B060355 04031324 494F532D 53656C66 2D536967 6E65642D 43657274', '  69666963 6174652D 37313836 37383538 301E170D 31393132 32343130 30333034', '  5A170D33 30303130 31303030 3030305A 302F312D 302B0603 55040313 24494F53', '  2D53656C 662D5369 676E6564 2D436572 74696669 63617465 2D373138 36373835', '  38308201 22300D06 092A8648 86F70D01 01010500 0382010F 00308201 0A028201', '  0100AF03 AF67DF21 FD73D15E B2360A66 594485F4 2043784C 3A369829 A984929D', '  CB30F424 9C2B2ED5 CE0D56A4 55C8E27D 68F489F4 6B4E17F6 817D9C88 EC49A048', '  3865CDA1 6803FFA4 AB178EED C0C3344C CA45D02C EAB3F185 DB2258B3 49B66E61', '  71928BE7 ED766D85 BA49CBBB 9FF75BAE E2630CB1 EA501D9F 8AD4A5DE 88B9C393', '  E8CA06FC 11357DEA 7243FE41 67DE63EF F8739B74 8F20CE19 A2C96EB8 669AE37B', '  AFFF202A 0FB8F5E1 B84BC829 83D425C4 E3EC24A4 02F6C02B BD17BCA5 DEA0AADC', '  D5E06830 5D7A72EF FF3A1798 D56C7C9E 18D9BB3C C34404E2 91876E24 D10F4237', '  95633FB3 DC1C61CC 920A951B 6C2754E9 AD7771F0 1AB8BAB2 F3AFDFE6 350BD1BE', '  F3450203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 301F0603', '  551D2304 18301680 1476FC52 CEB9F1AE 2BF67EBA 7CE44FD7 BA744A5A 2E301D06', '  03551D0E 04160414 76FC52CE B9F1AE2B F67EBA7C E44FD7BA 744A5A2E 300D0609', '  2A864886 F70D0101 05050003 82010100 91BD47F3 AEF56E58 6D73F163 2BCDA206', '  0185B102 9C20F581 D35B6920 AF53C7CE EF4A4CEC 66853F17 827F5D17 44021150', '  AD656ABC 2CD2A5B6 18655287 9AAE6E53 4F66CBE3 4A779429 A8C8FABD 49CE8633', '  8AA6FA8A 8CE58340 270DE337 8D115FF5 9F0F438A 63CC1288 ECC9E5E0 52DFF76D', '  9DA86FCA 2D576014 02B5EE83 26657880 B4D7F841 17C72957 8F7F6C34 5091C2D0', '  67DF85C7 E50ED637 71DC9971 D086BEA6 A22DBCB4 1EDE0D99 EE93D9C3 54DFE924', '  777BA1FC 9770F700 14C4A2D8 A7C6F3B6 501E0380 9CB03647 9FE67F04 C0D508E3', '  C74BC302 9602261E 7940F032 7AF2F0E8 ABC4D8EA 3F10E6D8 197130EF DCFC3C21', '  A739509E 6DD52326 B30E5F8B 436A0517', '  quit', '!', 'cts authorization list dnac-cts-list', '!', 'service-template DEFAULT_CRITICAL_DATA_TEMPLATE', 'service-template DEFAULT_CRITICAL_VOICE_TEMPLATE', ' voice vlan', 'service-template DEFAULT_LINKSEC_POLICY_MUST_SECURE', ' linksec policy must-secure', 'service-template DEFAULT_LINKSEC_POLICY_SHOULD_SECURE', ' linksec policy should-secure', 'service-template DefaultCriticalAccess_SRV_TEMPLATE', ' access-group IPV4-CRITICAL_AUTH_ACL', ' access-group IPV6-CRITICAL_AUTH_ACL', 'service-template DefaultCriticalAuthVlan_SRV_TEMPLATE', 'service-template DefaultCriticalVoice_SRV_TEMPLATE', ' voice vlan', 'service-template webauth-global-inactive', ' inactivity-timer 3600', 'system mtu 9100', 'license boot level network-advantage addon dna-advantage', 'license smart transport off', 'device classifier', '!', '!', 'no diagnostic bootup level', '!', 'spanning-tree mode rapid-pvst', 'spanning-tree extend system-id', 'no spanning-tree vlan 1-4094', 'memory free low-watermark processor 141155', '!', 'username admin privilege 15 password 0 DMIdmi1!', '!', 'redundancy', ' mode sso', '!', '!', '!', '!', '!', '!', 'transceiver type all', ' monitoring', 'lldp run', '!', 'class-map type control subscriber match-all AAA_SVR_DOWN_AUTHD_HOST', ' match authorization-status authorized', ' match result-type aaa-timeout', '!', 'class-map type control subscriber match-all AAA_SVR_DOWN_UNAUTHD_HOST', ' match authorization-status unauthorized', ' match result-type aaa-timeout', '!', 'class-map type control subscriber match-all AUTHC_SUCCESS_AUTHZ_FAIL', ' match authorization-status unauthorized', ' match result-type success', '!', 'class-map type control subscriber match-all DOT1X', ' match method dot1x', '!', 'class-map type control subscriber match-all DOT1X_FAILED', ' match method dot1x', ' match result-type method dot1x authoritative', '!', 'class-map type control subscriber match-all DOT1X_MEDIUM_PRIO', ' match authorizing-method-priority gt 20', '!', 'class-map type control subscriber match-all DOT1X_NO_RESP', ' match method dot1x', ' match result-type method dot1x agent-not-found', '!', 'class-map type control subscriber match-all DOT1X_TIMEOUT', ' match method dot1x', ' match result-type method dot1x method-timeout', '!', 'class-map type control subscriber match-any IN_CRITICAL_AUTH', ' match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE', '!', 'class-map type control subscriber match-any IN_CRITICAL_AUTH_CLOSED_MODE', ' match activated-service-template DefaultCriticalAuthVlan_SRV_TEMPLATE', ' match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE', '!', 'class-map type control subscriber match-all MAB', ' match method mab', '!', 'class-map type control subscriber match-all MAB_FAILED', ' match method mab', ' match result-type method mab authoritative', '!', 'class-map type control subscriber match-none NOT_IN_CRITICAL_AUTH', ' match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE', '!', 'class-map type control subscriber match-none NOT_IN_CRITICAL_AUTH_CLOSED_MODE', ' match activated-service-template DefaultCriticalAuthVlan_SRV_TEMPLATE', ' match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE', '!', '!', 'class-map match-any system-cpp-police-ewlc-control', '  description EWLC Control', 'class-map match-any system-cpp-police-topology-control', '  description Topology control', 'class-map match-any system-cpp-police-sw-forward', '  description Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic', 'class-map match-any system-cpp-default', '  description EWLC Data, Inter FED Traffic', 'class-map match-any data', ' match dscp af21', 'class-map match-any system-cpp-police-sys-data', '  description Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed', 'class-map match-all CL2Miss', ' match l2 dst-mac miss', 'class-map match-any system-cpp-police-punt-webauth', '  description Punt Webauth', 'class-map match-any system-cpp-police-l2lvx-control', '  description L2 LVX control packets', 'class-map match-any system-cpp-police-forus', '  description Forus Address resolution and Forus traffic', 'class-map match-any system-cpp-police-multicast-end-station', '  description MCAST END STATION', 'class-map match-any system-cpp-police-high-rate-app', '  description High Rate Applications', 'class-map match-any system-cpp-police-multicast', '  description MCAST Data', 'class-map match-any system-cpp-police-l2-control', '  description L2 control', 'class-map match-any system-cpp-police-dot1x-auth', '  description DOT1X Auth', 'class-map match-any system-cpp-police-data', '  description ICMP redirect, ICMP_GEN and BROADCAST', 'class-map match-any system-cpp-police-stackwise-virt-control', '  description Stackwise Virtual OOB', 'class-map match-any non-client-nrt-class', 'class-map match-any system-cpp-police-routing-control', '  description Routing control and Low Latency', 'class-map match-any system-cpp-police-protocol-snooping', '  description Protocol snooping', 'class-map match-any system-cpp-police-dhcp-snooping', '  description DHCP snooping', 'class-map match-any video', ' match dscp af41', 'class-map match-any system-cpp-police-ios-routing', '  description L2 control, Topology control, Routing control, Low Latency', 'class-map match-any system-cpp-police-system-critical', '  description System Critical and Gold Pkt', 'class-map match-any voice', ' match dscp ef', 'class-map match-any system-cpp-police-ios-feature', '  description ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed', '!', '!', 'policy-map type control subscriber PMAP_DefaultWiredDot1xClosedAuth_1X_MAB', ' event session-started match-all', '  10 class always do-until-failure', '   10 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event authentication-failure match-first', '  5 class DOT1X_FAILED do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure', '   30 authorize', '   40 pause reauthentication', '  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure', '   10 pause reauthentication', '   20 authorize', '  30 class DOT1X_NO_RESP do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  40 class MAB_FAILED do-until-failure', '   10 terminate mab', '   20 authentication-restart 60', '  50 class DOT1X_TIMEOUT do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  60 class always do-until-failure', '   10 terminate dot1x', '   20 terminate mab', '   30 authentication-restart 60', ' event aaa-available match-all', '  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 clear-session', '  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 resume reauthentication', ' event agent-found match-all', '  10 class always do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event inactivity-timeout match-all', '  10 class always do-until-failure', '   10 clear-session', ' event authentication-success match-all', ' event violation match-all', '  10 class always do-until-failure', '   10 restrict', ' event authorization-failure match-all', '  10 class AUTHC_SUCCESS_AUTHZ_FAIL do-until-failure', '   10 authentication-restart 60', '!', 'policy-map type control subscriber PMAP_DefaultWiredDot1xClosedAuth_MAB_1X', ' event session-started match-all', '  10 class always do-until-failure', '   10 authenticate using mab priority 20', ' event authentication-failure match-first', '  5 class DOT1X_FAILED do-until-failure', '   10 terminate dot1x', '   20 authentication-restart 60', '  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure', '   30 authorize', '   40 pause reauthentication', '  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure', '   10 pause reauthentication', '   20 authorize', '  30 class MAB_FAILED do-until-failure', '   10 terminate mab', '   20 authenticate using mab retries 2 retry-time 0 priority 10', '  40 class DOT1X_NO_RESP do-until-failure', '   10 terminate dot1x', '   20 authentication-restart 60', '  50 class DOT1X_TIMEOUT do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  60 class always do-until-failure', '   10 terminate mab', '   20 terminate dot1x', '   30 authentication-restart 60', ' event aaa-available match-all', '  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 clear-session', '  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 resume reauthentication', ' event agent-found match-all', '  10 class always do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event inactivity-timeout match-all', '  10 class always do-until-failure', '   10 clear-session', ' event authentication-success match-all', ' event violation match-all', '  10 class always do-until-failure', '   10 restrict', ' event authorization-failure match-all', '  10 class AUTHC_SUCCESS_AUTHZ_FAIL do-until-failure', '   10 authentication-restart 60', '!', 'policy-map type control subscriber PMAP_DefaultWiredDot1xLowImpactAuth_1X_MAB', ' event session-started match-all', '  10 class always do-until-failure', '   10 authenticate using dot1x', ' event authentication-failure match-first', '  5 class DOT1X_FAILED do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure', '   25 activate service-template DefaultCriticalAccess_SRV_TEMPLATE', '   30 authorize', '   40 pause reauthentication', '  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure', '   10 pause reauthentication', '   20 authorize', '  30 class DOT1X_NO_RESP do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  40 class MAB_FAILED do-until-failure', '   10 terminate mab', '   20 authentication-restart 60', '  50 class DOT1X_TIMEOUT do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  60 class always do-until-failure', '   10 terminate dot1x', '   20 terminate mab', '   30 authentication-restart 60', ' event aaa-available match-all', '  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 clear-session', '  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 resume reauthentication', ' event agent-found match-all', '  10 class always do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event inactivity-timeout match-all', '  10 class always do-until-failure', '   10 clear-session', ' event authentication-success match-all', ' event violation match-all', '  10 class always do-until-failure', '   10 restrict', ' event authorization-failure match-all', '  10 class AUTHC_SUCCESS_AUTHZ_FAIL do-until-failure', '   10 authentication-restart 60', '!', 'policy-map type control subscriber PMAP_DefaultWiredDot1xLowImpactAuth_MAB_1X', ' event session-started match-all', '  10 class always do-until-failure', '   10 authenticate using mab priority 20', ' event authentication-failure match-first', '  5 class DOT1X_FAILED do-until-failure', '   10 terminate dot1x', '   20 authentication-restart 60', '  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure', '   25 activate service-template DefaultCriticalAccess_SRV_TEMPLATE', '   30 authorize', '   40 pause reauthentication', '  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure', '   10 pause reauthentication', '   20 authorize', '  30 class MAB_FAILED do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', '  40 class DOT1X_NO_RESP do-until-failure', '   10 terminate dot1x', '   20 authenticate using dot1x', '  50 class DOT1X_TIMEOUT do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  60 class always do-until-failure', '   10 terminate mab', '   20 terminate dot1x', '   30 authentication-restart 60', ' event aaa-available match-all', '  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 clear-session', '  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 resume reauthentication', ' event agent-found match-all', '  10 class always do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event inactivity-timeout match-all', '  10 class always do-until-failure', '   10 clear-session', ' event authentication-success match-all', ' event violation match-all', '  10 class always do-until-failure', '   10 restrict', ' event authorization-failure match-all', '  10 class AUTHC_SUCCESS_AUTHZ_FAIL do-until-failure', '   10 authentication-restart 60', '!', 'policy-map type control subscriber PMAP_DefaultWiredDot1xOpenAuth_1X_MAB', ' event session-started match-all', '  10 class always do-until-failure', '   10 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event authentication-failure match-first', '  5 class DOT1X_FAILED do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure', '   30 authorize', '   40 pause reauthentication', '  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure', '   10 pause reauthentication', '   20 authorize', '  30 class DOT1X_NO_RESP do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  40 class MAB_FAILED do-until-failure', '   10 terminate mab', '   20 authentication-restart 60', '  50 class DOT1X_TIMEOUT do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  60 class always do-until-failure', '   10 terminate dot1x', '   20 terminate mab', '   30 authentication-restart 60', ' event aaa-available match-all', '  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 clear-session', '  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 resume reauthentication', ' event agent-found match-all', '  10 class always do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event inactivity-timeout match-all', '  10 class always do-until-failure', '   10 clear-session', ' event authentication-success match-all', ' event violation match-all', '  10 class always do-until-failure', '   10 restrict', ' event authorization-failure match-all', '  10 class AUTHC_SUCCESS_AUTHZ_FAIL do-until-failure', '   10 authentication-restart 60', '!', 'policy-map type control subscriber PMAP_DefaultWiredDot1xOpenAuth_MAB_1X', ' event session-started match-all', '  10 class always do-until-failure', '   10 authenticate using mab priority 20', ' event authentication-failure match-first', '  5 class DOT1X_FAILED do-until-failure', '   10 terminate dot1x', '   20 authentication-restart 60', '  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure', '   30 authorize', '   40 pause reauthentication', '  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure', '   10 pause reauthentication', '   20 authorize', '  30 class MAB_FAILED do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', '  40 class DOT1X_NO_RESP do-until-failure', '   10 terminate dot1x', '   20 authentication-restart 60', '  50 class DOT1X_TIMEOUT do-until-failure', '   10 terminate dot1x', '   20 authenticate using mab priority 20', '  60 class always do-until-failure', '   10 terminate mab', '   20 terminate dot1x', '   30 authentication-restart 60', ' event aaa-available match-all', '  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 clear-session', '  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure', '   10 resume reauthentication', ' event agent-found match-all', '  10 class always do-until-failure', '   10 terminate mab', '   20 authenticate using dot1x retries 2 retry-time 0 priority 10', ' event inactivity-timeout match-all', '  10 class always do-until-failure', '   10 clear-session', ' event authentication-success match-all', ' event violation match-all', '  10 class always do-until-failure', '   10 restrict', ' event authorization-failure match-all', '  10 class AUTHC_SUCCESS_AUTHZ_FAIL do-until-failure', '   10 authentication-restart 60', '!', 'policy-map egress', ' class voice', '  priority level 1', '  police rate 20000000', ' class video', '  police rate 100000000', ' class data', '  police rate 40000000', ' class class-default', 'policy-map ingress', ' class voice', '  police rate 20000000  peak-rate 40000000', ' class video', '  police rate 200000000  peak-rate 400000000', ' class data', '  police rate 40000000  peak-rate 80000000', ' class class-default', 'policy-map PL2Miss', ' class CL2Miss', '  police 100000', 'policy-map system-cpp-policy', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', 'autoconf enable', '!', 'template LAP_INTERFACE_TEMPLATE', ' storm-control broadcast level pps 1k', ' storm-control multicast level pps 2k', ' storm-control action trap', ' spanning-tree portfast', ' spanning-tree bpduguard enable', ' switchport access vlan 2045', ' switchport mode access', ' switchport block unicast', ' switchport port-security violation protect', ' switchport port-security aging time 2', ' switchport port-security aging type inactivity', ' switchport port-security', ' load-interval 30', ' ip dhcp snooping limit rate 15', '!', '!', 'interface Loopback0', ' no ip address', '!', 'interface GigabitEthernet0/0', ' vrf forwarding Mgmt-vrf', ' ip address 172.27.255.24 255.255.255.0', ' negotiation auto', '!', 'interface GigabitEthernet1/0/1', ' no switchport', ' no ip address', ' shutdown', '!', 'interface GigabitEthernet1/0/2', ' shutdown', '!', 'interface GigabitEthernet1/0/3', ' shutdown', '!', 'interface GigabitEthernet1/0/4', ' shutdown', '!', 'interface GigabitEthernet1/0/5', '!', 'interface GigabitEthernet1/0/6', '!', 'interface GigabitEthernet1/0/7', '!', 'interface GigabitEthernet1/0/8', '!', 'interface GigabitEthernet1/0/9', '!', 'interface GigabitEthernet1/0/10', ' service-policy input ingress', '!', 'interface GigabitEthernet1/0/11', '!', 'interface GigabitEthernet1/0/12', '!', 'interface GigabitEthernet1/0/13', '!', 'interface GigabitEthernet1/0/14', '!', 'interface GigabitEthernet1/0/15', '!', 'interface GigabitEthernet1/0/16', '!', 'interface GigabitEthernet1/0/17', '!', 'interface GigabitEthernet1/0/18', '!', 'interface GigabitEthernet1/0/19', '!', 'interface GigabitEthernet1/0/20', '!', 'interface GigabitEthernet1/0/21', '!', 'interface GigabitEthernet1/0/22', '!', 'interface GigabitEthernet1/0/23', '!', 'interface GigabitEthernet1/0/24', '!', 'interface GigabitEthernet1/1/1', '!', 'interface GigabitEthernet1/1/2', '!', 'interface GigabitEthernet1/1/3', '!', 'interface GigabitEthernet1/1/4', '!', 'interface TenGigabitEthernet1/1/1', ' description user', ' no switchport', ' no ip address', '!', 'interface TenGigabitEthernet1/1/2', '!', 'interface TenGigabitEthernet1/1/3', '!', 'interface TenGigabitEthernet1/1/4', '!', 'interface TenGigabitEthernet1/1/5', '!', 'interface TenGigabitEthernet1/1/6', '!', 'interface TenGigabitEthernet1/1/7', '!', 'interface TenGigabitEthernet1/1/8', '!', 'interface FortyGigabitEthernet1/1/1', '!', 'interface FortyGigabitEthernet1/1/2', '!', 'interface TwentyFiveGigE1/1/1', '!', 'interface TwentyFiveGigE1/1/2', '!', 'interface AppGigabitEthernet1/0/1', '!', 'interface Vlan1', ' no ip address', '!', 'router bgp 3', ' bgp router-id 1.1.1.1', ' bgp log-neighbor-changes', ' bgp graceful-restart', ' no bgp default ipv4-unicast', ' neighbor 255.255.255.255 remote-as 3', ' neighbor 255.255.255.255 description EVPN-BGP Enabled', ' neighbor 255.255.255.255 shutdown', ' !', ' address-family ipv4', ' exit-address-family', ' !', ' address-family l2vpn evpn', '  neighbor 255.255.255.255 activate', '  neighbor 255.255.255.255 send-community extended', ' exit-address-family', '!', 'iox', 'ip forward-protocol nd', 'ip http server', 'ip http authentication local', 'ip http secure-server', 'ip route vrf Mgmt-vrf 0.0.0.0 0.0.0.0 172.27.255.1', 'ip tacacs source-interface Loopback0', 'ip ssh version 2', 'ip ssh pubkey-chain', '  username admin', 'ip scp server enable', '!', '!', 'ip access-list extended bogus', ' 10 permit ip any any', '!', '!', 'ip prefix-list PFX_SUBNET_ROUTES seq 10 deny 0.0.0.0/0 ge 32', 'ip radius source-interface Loopback0', 'logging history debugging', 'logging snmp-trap emergencies', 'logging snmp-trap alerts', 'logging snmp-trap critical', 'logging snmp-trap errors', 'logging snmp-trap warnings', 'logging snmp-trap notifications', 'logging snmp-trap informational', 'logging snmp-trap debugging', 'logging host 10.24.72.167', 'logging host 10.24.72.167 vrf Mgmt-vrf', 'logging host 10.24.95.55 vrf Mgmt-vrf', 'logging host 172.20.86.186', 'logging host 17.1.102.186', '!', '!', 'ipv6 prefix-list PFX_V6_SUBNET_ROUTES seq 10 deny ::/0 ge 32 le 32', 'route-map SUBNET_ROUTES permit 10', ' match ip address prefix-list PFX_SUBNET_ROUTES', '!', 'route-map SUBNET_ROUTES permit 20', '!', 'route-map SUBNET_V6_ROUTES permit 10', ' match ip address prefix-list PFX_SUBNET_ROUTES', '!', 'route-map SUBNET_V6_ROUTES permit 20', '!', '!', 'snmp-server community public RO', 'snmp-server trap link ietf', 'snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart', 'snmp-server enable traps flowmon', 'snmp-server enable traps entity-perf throughput-notif', 'snmp-server enable traps call-home message-send-fail server-fail', 'snmp-server enable traps tty', 'snmp-server enable traps ospf state-change', 'snmp-server enable traps ospf errors', 'snmp-server enable traps ospf retransmit', 'snmp-server enable traps ospf lsa', 'snmp-server enable traps ospf cisco-specific state-change nssa-trans-change', 'snmp-server enable traps ospf cisco-specific state-change shamlink interface', 'snmp-server enable traps ospf cisco-specific state-change shamlink neighbor', 'snmp-server enable traps ospf cisco-specific errors', 'snmp-server enable traps ospf cisco-specific retransmit', 'snmp-server enable traps ospf cisco-specific lsa', 'snmp-server enable traps eigrp', 'snmp-server enable traps auth-framework sec-violation', 'snmp-server enable traps rep', 'snmp-server enable traps vtp', 'snmp-server enable traps vlancreate', 'snmp-server enable traps vlandelete', 'snmp-server enable traps port-security', 'snmp-server enable traps license', 'snmp-server enable traps smart-license', 'snmp-server enable traps cpu threshold', 'snmp-server enable traps memory bufferpeak', 'snmp-server enable traps stackwise', 'snmp-server enable traps udld link-fail-rpt', 'snmp-server enable traps udld status-change', 'snmp-server enable traps fru-ctrl', 'snmp-server enable traps flash insertion removal lowspace', 'snmp-server enable traps energywise', 'snmp-server enable traps power-ethernet police', 'snmp-server enable traps entity', 'snmp-server enable traps pw vc', 'snmp-server enable traps mvpn', 'snmp-server enable traps envmon', 'snmp-server enable traps cef resource-failure peer-state-change peer-fib-state-change inconsistency', 'snmp-server enable traps lisp', 'snmp-server enable traps isis', 'snmp-server enable traps ipsla', 'snmp-server enable traps entity-diag boot-up-fail hm-test-recover hm-thresh-reached scheduled-test-fail', 'snmp-server enable traps bfd', 'snmp-server enable traps ike policy add', 'snmp-server enable traps ike policy delete', 'snmp-server enable traps ike tunnel start', 'snmp-server enable traps ike tunnel stop', 'snmp-server enable traps ipsec cryptomap add', 'snmp-server enable traps ipsec cryptomap delete', 'snmp-server enable traps ipsec cryptomap attach', 'snmp-server enable traps ipsec cryptomap detach', 'snmp-server enable traps ipsec tunnel start', 'snmp-server enable traps ipsec tunnel stop', 'snmp-server enable traps ipsec too-many-sas', 'snmp-server enable traps config-copy', 'snmp-server enable traps config', 'snmp-server enable traps config-ctid', 'snmp-server enable traps dhcp', 'snmp-server enable traps event-manager', 'snmp-server enable traps hsrp', 'snmp-server enable traps ipmulticast', 'snmp-server enable traps msdp', 'snmp-server enable traps ospfv3 state-change', 'snmp-server enable traps ospfv3 errors', 'snmp-server enable traps pim neighbor-change rp-mapping-change invalid-pim-message', 'snmp-server enable traps bridge newroot topologychange', 'snmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency', 'snmp-server enable traps syslog', 'snmp-server enable traps bgp cbgp2', 'snmp-server enable traps nhrp nhs', 'snmp-server enable traps nhrp nhc', 'snmp-server enable traps nhrp nhp', 'snmp-server enable traps nhrp quota-exceeded', 'snmp-server enable traps mpls rfc ldp', 'snmp-server enable traps mpls ldp', 'snmp-server enable traps mpls rfc traffic-eng', 'snmp-server enable traps mpls traffic-eng', 'snmp-server enable traps mpls fast-reroute protected', 'snmp-server enable traps local-auth', 'snmp-server enable traps vlan-membership', 'snmp-server enable traps errdisable', 'snmp-server enable traps rf', 'snmp-server enable traps transceiver all', 'snmp-server enable traps bulkstat collection transfer', 'snmp-server enable traps mac-notification change move threshold', 'snmp-server enable traps vrfmib vrf-up vrf-down vnet-trunk-up vnet-trunk-down', 'snmp-server enable traps mpls vpn', 'snmp-server enable traps mpls rfc vpn', 'snmp-server host 10.24.56.22 vrf Mgmt-vrf public', 'snmp-server host 17.1.102.186 version 2c tesseract-traps', 'snmp-server host 172.20.86.186 version 2c tesseract-traps', 'snmp-server manager', '!', 'radius-server attribute 6 on-for-login-auth', 'radius-server attribute 6 support-multiple', 'radius-server attribute 8 include-in-access-req', 'radius-server attribute 25 access-request include', 'radius-server attribute 31 mac format ietf upper-case', 'radius-server attribute 31 send nas-port-detail mac-only', 'radius-server dead-criteria time 5 tries 3', 'radius-server deadtime 3', '!', '!', 'control-plane', ' service-policy input system-cpp-policy', '!', '!', 'line con 0', ' exec-timeout 0 0', ' login authentication CONSOLE', ' no domain-lookup', ' escape-character BREAK', ' stopbits 1', 'line vty 0 4', ' session-timeout 200', ' exec-timeout 0 0', ' no domain-lookup', ' transport input all', ' transport output all', ' escape-character BREAK', 'line vty 5 15', ' session-timeout 200', ' no domain-lookup', ' transport input all', ' transport output all', ' escape-character BREAK', 'line vty 16 31', ' transport input all', '!', 'call-home', ' ! If contact email address in call-home is configured as sch-smart-licensing@cisco.com', ' ! the email address configured in Cisco Smart License Portal will be used as contact email address to send SCH notifications.', ' contact-email-addr sch-smart-licensing@cisco.com', ' profile "CiscoTAC-1"', '  active', '!', '!', '!', '!', '!', '!', 'telemetry ietf subscription 204', ' filter xpath /interfaces', ' source-vrf Mgmt-vrf', ' stream yang-push', ' update-policy on-change', 'telemetry ietf subscription 205', ' filter xpath /cdp-ios-xe-oper:cdp-neighbor-details/cdp-neighbor-detail', ' source-vrf Mgmt-vrf', ' stream yang-push', ' update-policy on-change', 'app-hosting appid guestshell', ' app-vnic management guest-interface 0', ' name-server0 171.70.168.183', 'netconf-yang', 'netconf-yang cisco-ia snmp-trap-control trap-list 1.3.6.1.4.1.9.9.41.2.0.1', 'no netconf-yang cisco-ia intelligent-sync', 'end']
# # # # # # # # # # # # #
# # # # # # # # # # # # # if "aaa new-model" and "logging history debugging" and "snmp-server enable traps syslog" and "netconf-yang" in c:
# # # # # # # # # # # # #     print("true")
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print("false")
# # # # # # # # # # # # #
# # # # # # # # # # # # # kar = [
# # # # # # # # # # # # # "ddmi-cat9300-2#dir bootflash:/guest-share/",
# # # # # # # # # # # # # "Directory of flash:/guest-share/",
# # # # # # # # # # # # # "",
# # # # # # # # # # # # # "622785 -rw- 1334 Apr 16 2021 00:10:18 +00:00 TEST-action-functions_04-16-2021_00:10:14.320043.1",
# # # # # # # # # # # # # "622784 -rw- 1334 Apr 16 2021 00:05:02 +00:00 TEST-action-functions_04-16-2021_00:04:58.550621.1",
# # # # # # # # # # # # # "622780 -rw- 1334 Apr 16 2021 00:04:45 +00:00 TEST-action-functions_04-16-2021_00:04:40.826208.1",
# # # # # # # # # # # # # "622781 -rw- 1334 Apr 15 2021 23:43:08 +00:00 TEST-action-functions_04-15-2021_23:43:03.872912.1",
# # # # # # # # # # # # # ]
# # # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # #kar = ['ddmi-cat9300-2#dir bootflash:/guest-share/', 'Directory of flash:/guest-share/', '', '622792  -rw-             1334  Apr 16 2021 02:55:06 +00:00  TEST-action-functions_04-16-2021_02:55:02.227953.1', '622908  drwx             4096  Apr 16 2021 02:54:06 +00:00  ddr', '622783  -rw-             1334  Apr 16 2021 02:43:39 +00:00  TEST-action-functions_04-16-2021_02:43:34.771766.1', '622788  -rw-             1334  Apr 16 2021 02:18:00 +00:00  TEST-action-functions_04-16-2021_02:17:56.039734.1', '622787  -rw-             1334  Apr 16 2021 00:27:53 +00:00  TEST-action-functions_04-16-2021_00:27:48.714877.1', '622785  -rw-             1334  Apr 16 2021 00:10:18 +00:00  TEST-action-functions_04-16-2021_00:10:14.320043.1', '622784  -rw-             1334  Apr 16 2021 00:05:02 +00:00  TEST-action-functions_04-16-2021_00:04:58.550621.1', '622780  -rw-             1334  Apr 16 2021 00:04:45 +00:00  TEST-action-functions_04-16-2021_00:04:40.826208.1', '622781  -rw-             1334  Apr 15 2021 23:43:08 +00:00  TEST-action-functions_04-15-2021_23:43:03.872912.1', '622782  -rw-             1334  Apr 15 2021 23:33:27 +00:00  TEST-action-functions_04-15-2021_23:33:23.664273.1', '622763  -rw-              690  Apr 15 2021 23:32:16 +00:00  TEST-action-functions_04-15-2021_23:32:11.912909.1', '622776  -rw-             1166  Apr 15 2021 05:02:16 +00:00  Interface_health_04-15-2021_05:02:12.361487.1', '622779  -rw-              991  Apr 15 2021 05:00:27 +00:00  Interface_health_04-15-2021_05:00:18.317197.1', '622774  -rw-             1326  Apr 15 2021 04:48:01 +00:00  Interface_health_04-15-2021_04:47:57.599256.1', '622775  -rw-             1001  Apr 15 2021 04:47:45 +00:00  Interface_health_04-15-2021_04:47:41.536503.1', '622773  -rw-             1326  Apr 15 2021 04:46:18 +00:00  Interface_health_04-15-2021_04:46:14.062674.1', '622772  -rw-             8341  Apr 15 2021 04:44:47 +00:00  Interface_health_04-15-2021_04:44:43.381991.1', '622771  -rw-             1094  Apr 15 2021 04:40:12 +00:00  Interface_health_04-15-2021_04:40:08.758177.1', '622770  -rw-             1094  Apr 15 2021 04:37:04 +00:00  Interface_health_04-15-2021_04:37:00.727795.1', '622769  -rw-             1094  Apr 15 2021 04:34:20 +00:00  Interface_health_04-15-2021_04:34:16.005013.1', '622768  -rw-             1094  Apr 15 2021 04:33:41 +00:00  Interface_health_04-15-2021_04:33:37.819038.1', '622766  -rw-             1094  Apr 15 2021 04:29:20 +00:00  Interface_health_04-15-2021_04:29:16.058209.1', '622767  -rw-             1094  Apr 15 2021 04:26:47 +00:00  Interface_health_04-15-2021_04:26:43.699735.1', '622762  -rw-            14616  Apr 15 2021 04:18:10 +00:00  Interface_health_04-15-2021_04:17:58.781558.1', '622761  -rw-             1096  Apr 15 2021 04:16:42 +00:00  Interface_health_04-15-2021_04:16:29.430431.1', '622685  -rw-             6457  Apr 15 2021 04:12:49 +00:00  Interface_health_04-15-2021_04:12:38.423409.1', '622760  -rw-         27295247  Apr 15 2021 04:06:19 +00:00  copy_emre_show-tech-acl_04-15-2021_04:06:19.877663', '622730  -rw-         27295247  Apr 15 2021 04:06:18 +00:00  emre_show-tech-acl', '622666  drwx             4096  Mar 11 2021 17:09:56 +00:00  emre', '622690  drwx             4096  Oct 21 2020 18:25:38 +00:00  __pycache__', '', '11353194496 bytes total (2475573248 bytes free)']
# # # # # # # # # # # #
# # # # # # # # # # # # # kar = ['ddmi-9500-2#dir bootflash:/guest-share/', 'Directory of flash:/guest-share/', '', '303250  -rw-              560   May 5 2021 02:23:19 +05:30  tac-cpu', '303249  -rw-           327233   May 5 2021 02:23:09 +05:30  tac-cpu_TS_05-04-2021_20:53:06.167474', '303115  -rw-              239   May 5 2021 02:23:06 +05:30  Btrace_dmiauthd_log_05-04-2021_20:53:04.905027', '303255  drwx             4096   May 4 2021 21:53:52 +05:30  ddr', '303227  drwx             4096   Mar 4 2021 19:58:03 +05:30  emre', '', '11353194496 bytes total (416956416 bytes free)']
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # print(kar)
# # # # # # # # # # # # # print(kar[0])
# # # # # # # # # # # # # print(kar[1])
# # # # # # # # # # # # # print(kar[2])
# # # # # # # # # # # # # print(kar[3])
# # # # # # # # # # # # # print(kar[4])
# # # # # # # # # # # # # kb = kar[4]
# # # # # # # # # # # # # print(kb)
# # # # # # # # # # # # # print(type(kb))
# # # # # # # # # # # # # s = kb.split(" ")
# # # # # # # # # # # # # print(s)
# # # # # # # # # # # # # print(s[-1:])
# # # # # # # # # # # #
# # # # # # # # # # # # # fn = ['TEST-action-functions_04-16-2021_00:27:48.714877.1']
# # # # # # # # # # # # # for f in fn:
# # # # # # # # # # # # #     print(f)
# # # # # # # # # # # # # log_path = "dir bootflash:/guest-share/{}".format(f)
# # # # # # # # # # # # # print(log_path)
# # # # # # # # # # # # # import re
# # # # # # # # # # # # # ff = kar[4]
# # # # # # # # # # # # # print(ff)
# # # # # # # # # # # # # pat = ".*_TS_.*"
# # # # # # # # # # # # # result = re.match(pat, ff)
# # # # # # # # # # # # #
# # # # # # # # # # # # # if result:
# # # # # # # # # # # # #   print("Search successful.")
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #   print("Search unsuccessful.")
# # # # # # # # # # # #
# # # # # # # # # # # # # ff = kar[4]
# # # # # # # # # # # # #
# # # # # # # # # # # # # ff = ff.split(" ")
# # # # # # # # # # # # # fn = ff[-1:]
# # # # # # # # # # # # # print(fn)
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # service_impact = '''
# # # # # # # # # # # # #   <send-notification xmlns="http://cisco.com/ns/yang/cisco-ios-xe-ddr-control">
# # # # # # # # # # # # #     <description>{0}</description>
# # # # # # # # # # # # #     <messages>
# # # # # # # # # # # # # {1}    </messages>
# # # # # # # # # # # # #     <clips-facts>
# # # # # # # # # # # # # {2}    </clips-facts>
# # # # # # # # # # # # #     <dict-facts>
# # # # # # # # # # # # # {3}    </dict-facts>
# # # # # # # # # # # # #   </send-notification>'''
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # print(service_impact)
# # # # # # # # # # # #
# # # # # # # # # # # # # def ins(array):
# # # # # # # # # # # # #     for i in range(1, len(array)):
# # # # # # # # # # # # #         print("i {}".format(i))
# # # # # # # # # # # # #         j = i
# # # # # # # # # # # # #         while j > 0 and array[j] < array[j-1]:
# # # # # # # # # # # # #             swap(j, j-1, array)
# # # # # # # # # # # # #             print("j {}".format(j))
# # # # # # # # # # # # #             j -=1
# # # # # # # # # # # # #             print("j {}".format(j))
# # # # # # # # # # # # #     return array
# # # # # # # # # # # #
# # # # # # # # # # # # # def bs(array):
# # # # # # # # # # # # #     issorted = False
# # # # # # # # # # # # #     c = 0
# # # # # # # # # # # # #     while not issorted:
# # # # # # # # # # # # #         issorted = True
# # # # # # # # # # # # #         for i in range(len(array)-1-c):
# # # # # # # # # # # # #             if array[i] > array[i+1]:
# # # # # # # # # # # # #                 swap(i, i+1, array)
# # # # # # # # # # # # #                 issorted = False
# # # # # # # # # # # # #         c += 1
# # # # # # # # # # # # #     return array
# # # # # # # # # # # #
# # # # # # # # # # # # # def ss(array):
# # # # # # # # # # # # #     ci = 0
# # # # # # # # # # # # #     while ci < len(array) - 1:
# # # # # # # # # # # # #         si = ci
# # # # # # # # # # # # #         for i in range(ci+1, len(array)):
# # # # # # # # # # # # #             if array[si] > array[i]:
# # # # # # # # # # # # #                 si = i
# # # # # # # # # # # # #         swap(ci, si, array)
# # # # # # # # # # # # #         ci += 1
# # # # # # # # # # # # #
# # # # # # # # # # # # #     return array
# # # # # # # # # # # # #
# # # # # # # # # # # # # def swap(i,j, array):
# # # # # # # # # # # # #     array[i],array[j] = array[j],array[i]
# # # # # # # # # # # #
# # # # # # # # # # # # # def m(a1,a2):
# # # # # # # # # # # # #     print(a1,a2)
# # # # # # # # # # # # #     m = len(a1)
# # # # # # # # # # # # #     n = len(a2)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     for i in range(m):
# # # # # # # # # # # # #         if a1[i] > a2[0]:
# # # # # # # # # # # # #             temp = a1[i]
# # # # # # # # # # # # #             a1[i] = a2[0]
# # # # # # # # # # # # #             a2[0] = temp
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #     # print(a1, a2)
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # print(m([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # def me(a1, a2):
# # # # # # # # # # # # #     i = j = 0
# # # # # # # # # # # # #     l1 = len(a1)
# # # # # # # # # # # # #     l2 = len(a2)
# # # # # # # # # # # # #     arr = []
# # # # # # # # # # # # #     while i < l1 and j < l2:
# # # # # # # # # # # # #         if a1[i] < a2[j]:
# # # # # # # # # # # # #             arr.append(a1[i])
# # # # # # # # # # # # #             i += 1
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             arr.append(a2[j])
# # # # # # # # # # # # #             j += 1
# # # # # # # # # # # # #
# # # # # # # # # # # # #     while i < l1:
# # # # # # # # # # # # #         arr.append(a1[i])
# # # # # # # # # # # # #         i += 1
# # # # # # # # # # # # #
# # # # # # # # # # # # #     while j < l2:
# # # # # # # # # # # # #         arr.append(a2[j])
# # # # # # # # # # # # #         j += 1
# # # # # # # # # # # # #
# # # # # # # # # # # # #     return arr
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # a1 = [1,4,9,10]
# # # # # # # # # # # # # a2 = [2,3,6,7,8]
# # # # # # # # # # # # # print(me(a1,a2))
# # # # # # # # # # # #
# # # # # # # # # # # # # sl = "'Syslog logging: enabled (0 messages dropped, 2 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)\nNo Active Message Discriminator.\nInactive Message Discriminator:\nnosel     facility       drops    SELINUX\n    Console logging: disabled\n    Monitor logging: level debugging, 4277 messages logged, xml disabled,\n                     filtering disabled\n    Buffer logging:  disabled, xml disabled,\n                    filtering disabled\n    Exception Logging: size (4096 bytes)\n    Count and timestamp logging messages: disabled\n    File logging: disabled\n    Persistent logging: disabled\nNo active filter modules.\n    Trap logging: level informational, 4353 message lines logged\n        Logging Source-Interface:       VRF Name:\n    TLS Profiles: \n*May  2 06:05:58.182 PST: %LINK-3-UPDOWN: Interface Loopback3, changed state to down\n*May  2 06:06:00.677 PST: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/23, changed state to up'"
# # # # # # # # # # # # # print(sl)
# # # # # # # # # # # # # import re
# # # # # # # # # # # # # #m = re.search("(?P<interface>GigabitEthernet\d.\d.\d+).*changed state to down", sl, re.DOTALL)
# # # # # # # # # # # # # #m = re.search("(?P<interface>[A-Z][a-z]\d.\d.\d+).*changed state to down", sl, re.DOTALL)
# # # # # # # # # # # # # m = re.search("(?P<interface>Loopback\d+).*changed state to down", sl, re.DOTALL)
# # # # # # # # # # # # # r = re.search("(?P<interface>GigabitEthernet\d+).*changed state to up", sl, re.DOTALL)
# # # # # # # # # # # # # if m:
# # # # # # # # # # # # #     print(m.group("interface"))
# # # # # # # # # # # # #     intf = m.group("interface")
# # # # # # # # # # # # #
# # # # # # # # # # # # # if r:
# # # # # # # # # # # # #     print(r.group("interface"))
# # # # # # # # # # # # #     intfr = r.group("interface")
# # # # # # # # # # # # #
# # # # # # # # # # # # # print(intf)
# # # # # # # # # # # # # print(intfr)
# # # # # # # # # # # #
# # # # # # # # # # # # # import re
# # # # # # # # # # # # #
# # # # # # # # # # # # # def errorhdl(pattern, output,result):
# # # # # # # # # # # # #
# # # # # # # # # # # # #     if len(pattern) > 1:
# # # # # # # # # # # # #         for p in pattern:
# # # # # # # # # # # # #             matches = p.findall(output)
# # # # # # # # # # # # #
# # # # # # # # # # # # #             for match in matches:
# # # # # # # # # # # # #                 if match:
# # # # # # # # # # # # #                     print(match)
# # # # # # # # # # # # #                     if "FACTS" in match:
# # # # # # # # # # # # #                         print(result[0])
# # # # # # # # # # # # #                     elif "RULES" in match:
# # # # # # # # # # # # #                         print(result[1])
# # # # # # # # # # # # #                     else:
# # # # # # # # # # # # #                         print(result[2])
# # # # # # # # # # # # #     else:
# # # # # # # # # # # # #
# # # # # # # # # # # # #         for p in pattern:
# # # # # # # # # # # # #             matches = p.findall(output)
# # # # # # # # # # # # #
# # # # # # # # # # # # #             for match in matches:
# # # # # # # # # # # # #                 if match:
# # # # # # # # # # # # #                     print(result)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Deploy USE Case Error Handling Scenarios - deploy_use_case
# # # # # # # # # # # # #
# # # # # # # # # # # # # # DDR INITIAL BASIC CONFIGS - Configuration failure
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # ddmi-9500-2(config)#karthik
# # # # # # # # # # # # #                      ^
# # # # # # # # # # # # # % Invalid input detected at '^' marker.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # output = "ddmi-9500-2(config)#karthik^Z\nkarthik\n ^\n% Invalid input detected at '^' marker.\n\nddmi-9500-2#\nddmi-9500-2#"
# # # # # # # # # # # # # # pattern = [re.compile(r'.*Invalid input detected.*')]
# # # # # # # # # # # # # # result = "DDR Basic configs failed to configure in the device"
# # # # # # # # # # # # #
# # # # # # # # # # # # # #REMOVE THE DDR FILES FROM THE FLASH - rmdir failure
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # [guestshell@guestshell ~]$ rmdir karthik
# # # # # # # # # # # # # rmdir: failed to remove 'karthik': No such file or directory
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # output = "rmdir: failed to remove 'karthik': No such file or directory"
# # # # # # # # # # # # # # pattern = [re.compile(r'.*No such file or directory.*')]
# # # # # # # # # # # # # # result = "Removing the DDR Existing Directory Fails"
# # # # # # # # # # # # #
# # # # # # # # # # # # # #mkdir failure if usecase.name is empty
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # [guestshell@guestshell karthik]$ mkdir
# # # # # # # # # # # # # mkdir: missing operand
# # # # # # # # # # # # # Try 'mkdir --help' for more information.
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # # output = "mkdir: missing operand"
# # # # # # # # # # # # # # pattern = [re.compile(r'.*missing operand.*')]
# # # # # # # # # # # # # # result = "Creating the DDR new Directory to copy DDR specific files Fails"
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Execute USE Case Error Handling Scenarios - execute_use_case
# # # # # # # # # # # # #
# # # # # # # # # # # # # #DDR Use Case Execute: Executing DDR Python - no ddr py files to execute
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # ddmi-9500-2#guestshell run python3 /bootflash/guest-share/ddr/babu/babu.py
# # # # # # # # # # # # # python3: can't open file '/bootflash/guest-share/ddr/babu/babu.py': [Errno 2] No such file or directory
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # # output = "python3: can't open file \'/bootflash/guest-share/ddr/babu/babu.py\': [Errno 2] No such file or directory"
# # # # # # # # # # # # # # pattern = [re.compile(r'.*can\'t open file.*')]
# # # # # # # # # # # # # # result = "No DDR Python files to Execute"
# # # # # # # # # # # # #
# # # # # # # # # # # # # #DDR Use Case Execute: Executing DDR CLIPS - no ddr clips files to execute
# # # # # # # # # # # # # '''
# # # # # # # # # # # # # ddmi-9500-2#$/babu/ddr-flags --facts=/bootflash/guest-share/ddr/babu/ddr-facts --rules=/bootflash/guest-share/ddr/babu/ddr-rules --devices=/bootflash/guest-share/ddr/babu/ddr-devices
# # # # # # # # # # # # # %%%%% DDR Error: FACTS file not found
# # # # # # # # # # # # # %%%%% DDR Error: RULES file not found
# # # # # # # # # # # # # %%%%% DDR Error: ddr-flags file read error: [Errno 2] No such file or directory: '/bootflash/guest-share/ddr/babu/ddr-flags'
# # # # # # # # # # # # # '''
# # # # # # # # # # # # #
# # # # # # # # # # # # # output = '''
# # # # # # # # # # # # # %%%%% DDR Error: FACTS file not found
# # # # # # # # # # # # # %%%%% DDR Error: RULES file not found
# # # # # # # # # # # # # %%%%% DDR Error: ddr-flags file read error: [Errno 2] No such file or directory: \'/bootflash/guest-share/ddr/babu/ddr-flags\''''
# # # # # # # # # # # # #
# # # # # # # # # # # # # pattern = [re.compile(r'.*FACTS file not found.*'),re.compile(r'.*RULES file not found.*'), re.compile(r'.*No such file or directory.*')]
# # # # # # # # # # # # # result = ["No DDR CLIPS Fact files to Execute", "No DDR CLIPS Rules files to Execute", "No DDR CLIPS files to Execute"]
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # errorhdl(pattern,output,result)
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # class color:
# # # # # # # # # # # # #    PURPLE = '\033[95m'
# # # # # # # # # # # # #    CYAN = '\033[96m'
# # # # # # # # # # # # #    DARKCYAN = '\033[36m'
# # # # # # # # # # # # #    BLUE = '\033[94m'
# # # # # # # # # # # # #    GREEN = '\033[92m'
# # # # # # # # # # # # #    YELLOW = '\033[93m'
# # # # # # # # # # # # #    RED = '\033[91m'
# # # # # # # # # # # # #    BOLD = '\033[1m'
# # # # # # # # # # # # #    UNDERLINE = '\033[4m'
# # # # # # # # # # # # #    END = '\033[0m'
# # # # # # # # # # # # #
# # # # # # # # # # # # # print("The output is:" + color.BOLD + 'Python Programming !' + color.BLUE)
# # # # # # # # # # # # #
# # # # # # # # # # # # # import enum
# # # # # # # # # # # # # # Using enum class create enumerations
# # # # # # # # # # # # # class Days(enum.Enum):
# # # # # # # # # # # # #     Sun = 1
# # # # # # # # # # # # #     Mon = 2
# # # # # # # # # # # # #     Tue = 3
# # # # # # # # # # # # # # print the enum member as a string
# # # # # # # # # # # # # print ("The enum member as a string is : ",end="")
# # # # # # # # # # # # # print (Days.Mon)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # print the enum member as a repr
# # # # # # # # # # # # # print ("he enum member as a repr is : ",end="")
# # # # # # # # # # # # # print (repr(Days.Sun))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Check type of enum member
# # # # # # # # # # # # # print ("The type of enum member is : ",end ="")
# # # # # # # # # # # # # print (type(Days.Mon))
# # # # # # # # # # # # #
# # # # # # # # # # # # # # print name of enum member
# # # # # # # # # # # # # print ("The name of enum member is : ",end ="")
# # # # # # # # # # # # # print (Days.Tue.name)
# # # # # # # # # # # #
# # # # # # # # # # # # import re
# # # # # # # # # # # # res = "ddmi-9500-2#dir bootflash:guest-share/ddr/chaos/\nDirectory of flash:guest-share/ddr/chaos/\n\n303320  -rw-            91303  May 24 2021 20:04:02 +05:30  ?\n303319  -rw-         43276386  May 24 2021 20:02:47 +05:30  ddmi-9500-2_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_17162_20210524-191633-IST.core.gz\n303318  -rw-         43279742  May 24 2021 20:02:47 +05:30  ddmi-9500-2_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_15403_20210524-191603-IST.core.gz\n303317  -rw-         43276593  May 24 2021 20:02:47 +05:30  ddmi-9500-2_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_14665_20210524-191534-IST.core.gz\n303313  -rw-            91303  May 24 2021 19:14:47 +05:30  rp_base.cdb\n303314  drwx             4096  May 24 2021 15:20:36 +05:30  __pycache__\n303312  -rw-             1743  May 24 2021 15:16:11 +05:30  chaos.py\n303310  -rw-            58128  May 24 2021 15:15:55 +05:30  genie_parsers.py\n303311  -rw-            23817  May 24 2021 15:15:53 +05:30  ddrlib.py\n\n11353194496 bytes total (243400704 bytes free)"
# # # # # # # # # # # #
# # # # # # # # # # # # #print(res)
# # # # # # # # # # # # #
# # # # # # # # # # # # # pattern = re.compile(r'.*ddmi.*gz')
# # # # # # # # # # # # # matches = pattern.findall(res)
# # # # # # # # # # # # # new = []
# # # # # # # # # # # # # for match in matches:
# # # # # # # # # # # # #     x = match.split()
# # # # # # # # # # # # #     new.append(x[8])
# # # # # # # # # # # # #
# # # # # # # # # # # # # print(new)
# # # # # # # # # # # #
# # # # # # # # # # # # # import re
# # # # # # # # # # # # # res = "https://www.valid.in"
# # # # # # # # # # # # #
# # # # # # # # # # # # # pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
# # # # # # # # # # # # #
# # # # # # # # # # # # # matches = pattern.findall(res)
# # # # # # # # # # # # # for match in matches:
# # # # # # # # # # # # #     if match:
# # # # # # # # # # # # #         print(match)
# # # # # # # # # # # # #         proto, dom, tld, v= match
# # # # # # # # # # # # #         print(dom)
# # # # # # # # # # # # #         print(tld)
# # # # # # # # # # # # #         dom = dom.strip(r'www.')
# # # # # # # # # # # # #         print(dom)
# # # # # # # # # # # # #         full_dom = f"{dom}.{tld}"
# # # # # # # # # # # # #         print(full_dom)
# # # # # # # # # # # # #         print(type(full_dom))
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # import re
# # # # # # # # # # # # # import datetime
# # # # # # # # # # # # # from datetime import datetime
# # # # # # # # # # # # # import time
# # # # # # # # # # # # # from ddrlib import *
# # # # # # # # # # # # # import os
# # # # # # # # # # # # # import json
# # # # # # # # # # # # #
# # # # # # # # # # # # # USECASE_NAME = "<<USECASENAME>>"
# # # # # # # # # # # # # #TARGET_DIR = f"/bootflash/guest-share/ddr/{USECASE_NAME}/"
# # # # # # # # # # # # # TARGET_DIR = "/bootflash/guest-share/ddr/tac_cpu/"
# # # # # # # # # # # # #
# # # # # # # # # # # # # DEVICE_IP = "<<DEVICEIP>>"
# # # # # # # # # # # # # USERNAME = "<<USERNAME>>"
# # # # # # # # # # # # # PASSWORD = "<<PASSSWORD>>"
# # # # # # # # # # # # #
# # # # # # # # # # # # # timestamp =  "TS_" + datetime.now().strftime("%m-%d-%Y_%H:%M:%S.%f")
# # # # # # # # # # # # # device=['127.0.0.1', 830, 'guestshell', 'none']
# # # # # # # # # # # # #
# # # # # # # # # # # # # def write_to_file(data: str, filename: str, mode: str = "w"):
# # # # # # # # # # # # #     with open(TARGET_DIR+filename, mode) as f:
# # # # # # # # # # # # #         f.write(data)
# # # # # # # # # # # # #
# # # # # # # # # # # # # def append_to_file(data: str, filename: str):
# # # # # # # # # # # # #     write_to_file(data, filename, "a")
# # # # # # # # # # # # #
# # # # # # # # # # # # # def log_data(data: str):
# # # # # # # # # # # # #     append_to_file("output.json")
# # # # # # # # # # # # #
# # # # # # # # # # # # # def save_output(data: str) -> None:
# # # # # # # # # # # # #     write_to_file(data, "output.json", "w")
# # # # # # # # # # # # #
# # # # # # # # # # # # # # NETCONF connection to device uses localhost IP, port 830, username "guestshell" with no password
# # # # # # # # # # # # #
# # # # # # # # # # # # # device = ["127.0.0.1", 830, "guestshell", "none"]
# # # # # # # # # # # # #
# # # # # # # # # # # # # try:
# # # # # # # # # # # # # # wait for notification generated with Syslog for configuration mode exit is generated on device
# # # # # # # # # # # # #     ddr_nc_notify(device, False, ["CONFIG_I", "Configured from"])
# # # # # # # # # # # # #
# # # # # # # # # # # # #     commands = [
# # # # # # # # # # # # #         f"show proc cpu sort",
# # # # # # # # # # # # #         f"show proc cpu hist",
# # # # # # # # # # # # #         f"show proc cpu platform sorted",
# # # # # # # # # # # # #         f"show interface",
# # # # # # # # # # # # #         f"show interface stats",
# # # # # # # # # # # # #         f"show log ",
# # # # # # # # # # # # #         f"show ip traffic",
# # # # # # # # # # # # #         f"show users",
# # # # # # # # # # # # #         f"show platform software fed switch active punt cause summary",
# # # # # # # # # # # # #         f"show platform software fed switch active cpu-interface",
# # # # # # # # # # # # #         f"show platform software fed switch active punt cpuq all",
# # # # # # # # # # # # #         f"no monitor capture tac_cpu",
# # # # # # # # # # # # #         f"monitor capture tac_cpu control-plane in match any file location flash:/guest-share/tac-cpu",
# # # # # # # # # # # # #         f"monitor capture tac_cpu start",
# # # # # # # # # # # # #         f"monitor capture tac_cpu stop"
# # # # # # # # # # # # #     ]
# # # # # # # # # # # # #
# # # # # # # # # # # # #     output = {}
# # # # # # # # # # # # #     for command in commands:
# # # # # # # # # # # # #         output[command] = ddr_cli_command(device, False, 'cli', command, True, timestamp)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     # One way or another, the output goes into output.json
# # # # # # # # # # # # #     save_output(json.dumps(output))
# # # # # # # # # # # # #
# # # # # # # # # # # # #     ddr_write_to_syslog("DDR-Python static use case: uc-tac-cpu complete")
# # # # # # # # # # # # # except Exception as e:
# # # # # # # # # # # # #     raise Exception("DDR-Python tac_cpu usecase failed")
# # # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # def cuboid_volume(l):
# # # # # # # # # # # # #     print(l)
# # # # # # # # # # # # #     return (l*l*l)
# # # # # # # # # # # # #
# # # # # # # # # # # # # length = [2,1.1, -2.5, 2j, 'two']
# # # # # # # # # # # # #
# # # # # # # # # # # # # for i in range(len(length)):
# # # # # # # # # # # # #     print(length[i])
# # # # # # # # # # # # #     print ("The volume of cuboid:",cuboid_volume(length[i]))
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # import re
# # # # # # # # # # # # import datetime
# # # # # # # # # # # # from datetime import datetime
# # # # # # # # # # # # import time
# # # # # # # # # # # # from ddrlib import *
# # # # # # # # # # # # import os
# # # # # # # # # # # # import json
# # # # # # # # # # # # from ncclient import manager
# # # # # # # # # # # #
# # # # # # # # # # # # USECASE_NAME = "<<USECASENAME>>"
# # # # # # # # # # # # #TARGET_DIR = f"/bootflash/guest-share/ddr/{USECASE_NAME}/"
# # # # # # # # # # # # DEVICE_IP = "<<DEVICEIP>>"
# # # # # # # # # # # # USERNAME = "<<USERNAME>>"
# # # # # # # # # # # # PASSWORD = "<<PASSSWORD>>"
# # # # # # # # # # # # def write_to_file(data: str, filename: str, mode: str = "w"):
# # # # # # # # # # # #     with open(TARGET_DIR+filename, mode) as f:
# # # # # # # # # # # #         f.write(data)
# # # # # # # # # # # #
# # # # # # # # # # # # def append_to_file(data: str, filename: str):
# # # # # # # # # # # #     write_to_file(data, filename, "a")
# # # # # # # # # # # #
# # # # # # # # # # # # def log_data(data: str):
# # # # # # # # # # # #     append_to_file("output.json")
# # # # # # # # # # # #
# # # # # # # # # # # # def save_output(data: str) -> None:
# # # # # # # # # # # #     write_to_file(data, "output.json", "w")
# # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # Use local NETCONF connection in guestshell without password
# # # # # # # # # # # # #
# # # # # # # # # # # # device = ["127.0.0.1", 830, "guestshell", "none"]
# # # # # # # # # # # # access_type = 'cli'
# # # # # # # # # # # # TARGET_DIR = "/bootflash/guest-share/ddr/interface_dynamic/"
# # # # # # # # # # # # #
# # # # # # # # # # # # # Use SSH offbox NETCONF connection with device credentials
# # # # # # # # # # # # #
# # # # # # # # # # # # #device = ["172.27.255.24", 830, "admin", "DMIdmi1!"]
# # # # # # # # # # # # #access_type = 'ssh'
# # # # # # # # # # # # #TARGET_DIR = "./examples/logs/"
# # # # # # # # # # # #
# # # # # # # # # # # # timestamp =  "TS_" + datetime.now().strftime("%m-%d-%Y_%H:%M:%S.%f")
# # # # # # # # # # # # debug = False
# # # # # # # # # # # # #
# # # # # # # # # # # # # interface_dynamic use case - When an interface is unshut, get the name of the interface and use the value
# # # # # # # # # # # # # to perform actions
# # # # # # # # # # # # #
# # # # # # # # # # # # # ddmi-cat9300-2(config-if)#no shut
# # # # # # # # # # # # # ddmi-cat9300-2(config-if)#
# # # # # # # # # # # # # *May 27 11:08:37.778: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback1, changed state to up
# # # # # # # # # # # # # *May 27 11:08:37.779: %LINK-3-UPDOWN: Interface Loopback1, changed state to up
# # # # # # # # # # # #
# # # # # # # # # # # # try:
# # # # # # # # # # # #
# # # # # # # # # # # #     # Show commands to collect interface information using the interface name extracted from the Syslog message
# # # # # # # # # # # #     output = {}
# # # # # # # # # # # #     commands = [
# # # # # # # # # # # #         f"show version",
# # # # # # # # # # # #         f"show ip int bri"
# # # # # # # # # # # #     ]
# # # # # # # # # # # #
# # # # # # # # # # # #     for command in commands:
# # # # # # # # # # # #         output[command] = ddr_cli_command(device, access_type, command, True, timestamp, debug_flag=debug).decode('utf-8')
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #     #
# # # # # # # # # # # #     # Generate Syslog notification if running on the device
# # # # # # # # # # # #     #
# # # # # # # # # # # #     output['use-case-notification'] = 'DDR-Python use case: interface_dynamic complete'
# # # # # # # # # # # #
# # # # # # # # # # # #     ## Write to results of the use case execution to the "output.json" file
# # # # # # # # # # # #     save_output(json.dumps(output))
# # # # # # # # # # # #     #save_output(json.dumps(output.decode("utf-8")))
# # # # # # # # # # # #     #save_output(json.dumps(list(output)))
# # # # # # # # # # # #     #print(output)
# # # # # # # # # # # #
# # # # # # # # # # # # except Exception as e:
# # # # # # # # # # # #     raise Exception("DDR-Python interface_dynamic usecase failed")
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # g_enable_list = "'nx-dmi-36# guestshell enable', 'ERROR: Guest shell is already enabled'"
# # # # # # # # # # # # #
# # # # # # # # # # # # # if "Guestshell enabled successfully" in g_enable_list:
# # # # # # # # # # # # #     print("DDR Infra Deploy: Guestshell Enabled Successfully !!!\n")
# # # # # # # # # # # # # elif "Guest shell is already enabled" in g_enable_list:
# # # # # # # # # # # # #     print("DDR Infra Deploy: Guestshell Enabled Successfully !!!\n")
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print("karthik")
# # # # # # # # # # # # #
# # # # # # # # # # # # ver_check_list = "'nx-dmi-36# show version', 'Cisco Nexus Operating System (NX-OS) Software', 'TAC support: http://www.cisco.com/tac', 'Copyright (C) 2002-2021, Cisco and/or its affiliates.', 'All rights reserved.', 'The copyrights to certain works contained in this software are', 'owned by other third parties and used and distributed under their own', 'licenses, such as open source.  This software is provided "as is," and unless', 'otherwise stated, there is no warranty, express or implied, including but not', 'limited to warranties of merchantability and fitness for a particular purpose.', 'Certain components of this software are licensed under', 'the GNU General Public License (GPL) version 2.0 or', 'GNU General Public License (GPL) version 3.0  or the GNU', 'Lesser General Public License (LGPL) Version 2.1 or', 'Lesser General Public License (LGPL) Version 2.0.', 'A copy of each such license is available at', 'http://www.opensource.org/licenses/gpl-2.0.php and', 'http://opensource.org/licenses/gpl-3.0.html and', 'http://www.opensource.org/licenses/lgpl-2.1.php and', 'http://www.gnu.org/licenses/old-licenses/library.txt.', '', 'Software', '  BIOS: version 07.66', '  NXOS: version 10.1(2)', '  BIOS compile time:  06/11/2019--More--', '  NXOS image file is: bootflash:///nxos.10.1.2.bin', '  NXOS compile time:  5/13/2021 17:00:00 [05/14/2021 02:21:06]', '', 'Hardware', '  cisco Nexus9000 C93108TC-EX chassis', '  Intel(R) Xeon(R) CPU  @ 1.80GHz with 24627792 kB of memory.', '  Processor Board ID FDO23440TQY', '  Device name: nx-dmi-36', '  bootflash:   53298520 kB', '', 'Kernel uptime is 1 day(s), 19 hour(s), 30 minute(s), 39 second(s)', '', 'Last reset at 44486 usecs after Fri Jun  4 12:30:36 2021', '  Reason: Reset Requested by CLI command reload', '  System version: 9.4(1)', '  Service:', '', 'plugin', '  Core Plugin, Ethernet Plugin', '', 'Active Package(s):'"
# # # # # # # # # # # # print(ver_check_list)
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # 1->2>-3>4>NULL
# # # # # # # # # # # # #
# # # # # # # # # # # # # 4>3>2>1>NULL
# # # # # # # # # # # #
# # # # # # # # # # # # class Node:
# # # # # # # # # # # #     def _init__(self, data):
# # # # # # # # # # # #         self.data = data
# # # # # # # # # # # #         self.next = None
# # # # # # # # # # # #
# # # # # # # # # # # # class LL:
# # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # #         self.head = None
# # # # # # # # # # # #
# # # # # # # # # # # #     def rev(self):
# # # # # # # # # # # #         prev = None
# # # # # # # # # # # #         current = self.head
# # # # # # # # # # # #
# # # # # # # # # # # #         while current is not None:
# # # # # # # # # # # #             next = current.next
# # # # # # # # # # # #             current.next = prev
# # # # # # # # # # # #             prev = current
# # # # # # # # # # # #
# # # # # # # # # # # #             current = next
# # # # # # # # # # # #         self.head = prev
# # # # # # # # # # # #
# # # # # # # # # # # #     def push:
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # void show_mem_rep(char *start,int n)
# # # # # # # # # # # # {
# # # # # # # # # # # #     int i;
# # # # # # # # # # # #     for (i ==0; i < n; i++)
# # # # # # # # # # # #         printf("%.2x", start[i]);
# # # # # # # # # # # # }
# # # # # # # # # # # #
# # # # # # # # # # # # int main()
# # # # # # # # # # # # {
# # # # # # # # # # # #     int i = 0x1234567;
# # # # # # # # # # # #     show_mem_rep((char *)&i, sizeof(i));
# # # # # # # # # # # #     getchar();
# # # # # # # # # # # #     return 0;
# # # # # # # # # # # # }
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # run('example_script.py', uids = Or('common_setup',
# # # # # # # # # # #                                    And('^bgp.+', '.*traffic.*', Not('sanity')),
# # # # # # # # # # #                                    And('^ospf.+', '.*traffic.*', Not('sanity')),
# # # # # # # # # # #                                    'common_cleanup'))
# # # # # # # # # # #
# # # # # # # # # # # --uids "Or('common_setup', And('DeployInfra'), And('DeployUseCase'), And('ExecuteUseCase'), And('CollectData'), And('CleanInfra'), 'Common_cleanup')"
# # # # # # # # # # #
# # # # # # # # # # # --uids "Or('common_setup', And('DeployUseCase'), And('ExecuteUseCase'), And('CollectData'), 'Common_cleanup')"
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # output = "ddmi-cat9300-2#show app-hosting list | in guestshell guestshell                               RUNNING"
# # # # # # # # # # #
# # # # # # # # # # # check_string = ['RUNNING', 'DEPLOYED']
# # # # # # # # # # # for i in check_string:
# # # # # # # # # # #     if i in output:
# # # # # # # # # # #         print("karthik")
# # # # # # # # # # #         break
# # # # # # # # # # #     else:
# # # # # # # # # # #         print("babu")
# # # # # # # # # # #
# # # # # # # # # # # out = re.search('<(.*)/>',b)
# # # # # # # # # #
# # # # # # # # # # # import re
# # # # # # # # # # # # output = "<state>Activated</state>"
# # # # # # # # # # # #
# # # # # # # # # # # # match = re.search(r".*<state>(.*)</state>.*", output)
# # # # # # # # # # # #
# # # # # # # # # # # # if match:
# # # # # # # # # # # #     print("karthik")
# # # # # # # # # # # #     value = match.group(1)
# # # # # # # # # # # #     print(value)
# # # # # # # # # # #
# # # # # # # # # # # def ce(usecase):
# # # # # # # # # # #
# # # # # # # # # # #     valid_uc = ["link", "linkcef"]
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #     for v in valid_uc:
# # # # # # # # # # #         print(v)
# # # # # # # # # # #         print(usecase)
# # # # # # # # # # #         if v == usecase:
# # # # # # # # # # #             break
# # # # # # # # # # #     else:
# # # # # # # # # # #         print("not a vliad usevase")
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # ce("linkcefwhcg")
# # # # # # # # # #
# # # # # # # # # # import re
# # # # # # # # # # out = "Interface              IP-Address      OK? Method Status                Protocol Vlan101                19.0.0.1        YES NVRAM  up                    up      "
# # # # # # # # # #
# # # # # # # # # # # def find_ip(s) :
# # # # # # # # # # #     ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s).group()
# # # # # # # # # # #
# # # # # # # # # # #     if ip:
# # # # # # # # # # #         return ip
# # # # # # # # # # #
# # # # # # # # # # # print(find_ip(out))
# # # # # # # # # # #p1 = re.compile(r'.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*')
# # # # # # # # # #
# # # # # # # # # # parsed_dict = {}
# # # # # # # # # # dict = parsed_dict.setdefault('interface_ip_address', {})
# # # # # # # # # # print(parsed_dict)
# # # # # # # # # #
# # # # # # # # # # p1 = re.compile(r'^.*Interface +IP-Address.*')
# # # # # # # # # #
# # # # # # # # # # p2 = re.compile(r'^(?P<interface>[^pP][\S]+) +(?P<ip_address>(\S+))'
# # # # # # # # # #
# # # # # # # # # #                 )
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # p2 = re.compile(r'^(?P<port>[a-zA-Z0-9]+) +(?P<vrf>[a-zA-Z0-9\-]+)'
# # # # # # # # # # #                         r' +(?P<status>[a-zA-Z]+) +(?P<ip_address>(\S+))'
# # # # # # # # # # #                         r' +(?P<speed>\S+) +(?P<mtu>[0-9]+)$')
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # for line in out.splitlines():
# # # # # # # # # #     line = line.strip()
# # # # # # # # # #     print(line)
# # # # # # # # # #
# # # # # # # # # #     m = p1.match(line)
# # # # # # # # # #     m = p2.match(line)
# # # # # # # # # #     if m:
# # # # # # # # # #         print("babu")
# # # # # # # # # #         group = m.groupdict()
# # # # # # # # # #         print(group)
# # # # # # # # # # print(parsed_dict)
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # import re
# # # # # # # # # # # output = "# VLAN Name Status Ports # ---- -------------------------------- --------- -------------------------------# 2 VLAN0002 active Gi1/0/1, Gi1/0/2"
# # # # # # # # # # #
# # # # # # # # # # # def parse(output):
# # # # # # # # # # #
# # # # # # # # # # #     # Init vars
# # # # # # # # # # #         parsed_dict = {}
# # # # # # # # # # #         dict = parsed_dict.setdefault('connected_vlan_ports', {})
# # # # # # # # # # #
# # # # # # # # # # #     # VLAN Name Status Ports
# # # # # # # # # # #     # ---- -------------------------------- --------- -------------------------------
# # # # # # # # # # #     # 2 VLAN0002 active Gi1/0/1, Gi1/0/2
# # # # # # # # # # #
# # # # # # # # # # #         p1 = re.compile(r'.*active(\s+)(?P<port>(\S+)).*')
# # # # # # # # # # #
# # # # # # # # # # #         for line in output.splitlines():
# # # # # # # # # # #             line = line.strip()
# # # # # # # # # # #
# # # # # # # # # # #             m = p1.match(line)
# # # # # # # # # # #             if m:
# # # # # # # # # # #                 group = m.groupdict()
# # # # # # # # # # #                 port = str(group["port"]).rstrip(",")
# # # # # # # # # # #                 port_dict = dict.setdefault(port, {})
# # # # # # # # # # #                 break
# # # # # # # # # # #         return parsed_dict
# # # # # # # # # # #
# # # # # # # # # # # print(parse(output))
# # # # # # # #
# # # # # # # # import re
# # # # # # # # output = """
# # # # # # # # ddmi-cat9300-2#
# # # # # # # # Interface              IP-Address      OK? Method Status                Protocol
# # # # # # # # Vlan1                  19.1.1.1        YES manual up                    up
# # # # # # # #
# # # # # # # # """
# # # # # # # #
# # # # # # # # ############# WORKINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG ###############
# # # # # # # # parsed_dict = {}
# # # # # # # # intf_dict = parsed_dict.setdefault('interface_ip_address', {})
# # # # # # # #
# # # # # # # # p1 = re.compile(r'^(?P<interface>\w+)\s+(?P<ip>\d+\.\d+\.\d+\.\d+)\s+(?P<ok>(YES|NO))\s+(?P<method>\w+)\s+(?P<status>\w+)\s+(?P<protocol>\w+)')
# # # # # # # #
# # # # # # # # for line in output.splitlines():
# # # # # # # #     line = line.strip()
# # # # # # # #
# # # # # # # #     m = p1.match(line)
# # # # # # # #     if m:
# # # # # # # #         group = m.groupdict()
# # # # # # # #         interface = str(group["interface"].lstrip('"').rstrip('"'))
# # # # # # # #         interface_dict = intf_dict.setdefault(interface, {})
# # # # # # # #         interface_dict['ip'] = str(group['ip'])
# # # # # # # #         interface_dict['ok'] = str(group['ok'])
# # # # # # # #         interface_dict['method'] = str(group['method'])
# # # # # # # #         interface_dict['status'] = str(group['status'])
# # # # # # # #         interface_dict['protocol'] = str(group['protocol'])
# # # # # # # #         continue
# # # # # # # # print(parsed_dict)
# # # # # # # #
# # # # # # # #
# # # # # # # # import re
# # # # # # # # output = """
# # # # # # # # ddmi-cat9300-2#
# # # # # # # # Vlan1 is up, line protocol is up
# # # # # # # #   Internet address is 19.1.1.1/24
# # # # # # # #   Broadcast address is 255.255.255.255
# # # # # # # #   Address determined by setup command
# # # # # # # #   MTU is 1500 bytes
# # # # # # # #   Helper address is not set
# # # # # # # #   Directed broadcast forwarding is disabled
# # # # # # # #   Outgoing Common access list is not set
# # # # # # # #   Outgoing access list is not set
# # # # # # # #   Inbound Common access list is not set
# # # # # # # #   Inbound  access list is not set
# # # # # # # #   Proxy ARP is enabled
# # # # # # # #   Local Proxy ARP is disabled
# # # # # # # #   Security level is default
# # # # # # # #   Split horizon is enabled
# # # # # # # #   ICMP redirects are always sent
# # # # # # # #   ICMP unreachables are always sent
# # # # # # # #   ICMP mask replies are never sent
# # # # # # # #   IP fast switching is enabled
# # # # # # # #   IP Flow switching is disabled
# # # # # # # #   IP CEF switching is enabled
# # # # # # # #   IP CEF switching turbo vector
# # # # # # # #   IP Null turbo vector
# # # # # # # #   Associated unicast routing topologies:
# # # # # # # #         Topology "base", operation state is UP
# # # # # # # #   IP multicast fast switching is enabled
# # # # # # # #   IP multicast distributed fast switching is disabled
# # # # # # # #   IP route-cache flags are Fast, CEF
# # # # # # # #   Router Discovery is disabled
# # # # # # # #   IP output packet accounting is disabled
# # # # # # # #   IP access violation accounting is disabled
# # # # # # # #   TCP/IP header compression is disabled
# # # # # # # #   RTP/IP header compression is disabled
# # # # # # # #   Probe proxy name replies are disabled
# # # # # # # #   Policy routing is disabled
# # # # # # # #   Network address translation is disabled
# # # # # # # #   BGP Policy Mapping is disabled
# # # # # # # #   Input features: MCI Check
# # # # # # # #   IPv4 WCCP Redirect outbound is disabled
# # # # # # # #   IPv4 WCCP Redirect inbound is disabled
# # # # # # # #   IPv4 WCCP Redirect exclude is disabled
# # # # # # # #   IP Clear Dont Fragment is disabled
# # # # # # # #
# # # # # # # # """
# # # # # # # #
# # # # # # # # parsed_dict = {}
# # # # # # # # intf_dict = parsed_dict.setdefault('interface_ip_address', {})
# # # # # # # #
# # # # # # # # p1 = re.compile(r'^(?P<interface>[\w\/\.\-\:]+)\s+is\s+(?P<enabled>\w+)\,\s+line\s+protocol\sis\s(?P<status>\w+)')
# # # # # # # # p2 = re.compile(r'^.*Internet\s+[A|a]ddress\s+is\s+(?P<ipv4>.*)\/(?P<prefix>[0-9]+)')
# # # # # # # #
# # # # # # # # for line in output.splitlines():
# # # # # # # #     line = line.strip()
# # # # # # # #
# # # # # # # #     m = p1.match(line)
# # # # # # # #     if m:
# # # # # # # #         group = m.groupdict()
# # # # # # # #         interface = str(group["interface"].lstrip('"').rstrip('"'))
# # # # # # # #         interface_dict = intf_dict.setdefault(interface, {})
# # # # # # # #         interface_dict['enable'] = str(group["enabled"])
# # # # # # # #         continue
# # # # # # # #
# # # # # # # #     m = p2.match(line)
# # # # # # # #     if m:
# # # # # # # #         group = m.groupdict()
# # # # # # # #         interface_dict['ipv4'] = str(group['ipv4'])
# # # # # # # #         interface_dict['prefix'] = str(group['prefix'])
# # # # # # # #         continue
# # # # # # # #
# # # # # # # # print(parsed_dict)
# # # # # # # #
# # # # # # # # import re
# # # # # # # # output = """
# # # # # # # # ddmi-cat9300-2#
# # # # # # # # Active IPv4-SGT Bindings Information
# # # # # # # #
# # # # # # # # IP Address              SGT     Source
# # # # # # # # ============================================
# # # # # # # # 19.0.0.0/24             35          CLI
# # # # # # # # 19.100.100.100/24      36          LISP
# # # # # # # # """
# # # # # # # #
# # # # # # # # parsed_dict = {}
# # # # # # # # sgt_dict = parsed_dict.setdefault('ipv4_sgt_binding', {})
# # # # # # # #
# # # # # # # # p = re.compile(r'^(?P<ip>.\d+\.\d+\.\d+\.\d+)\/(?P<prefix>.\d+)\s+(?P<sgt>\d+)\s+(?P<src>\w+)')
# # # # # # # #
# # # # # # # # i = 0
# # # # # # # # for line in output.splitlines():
# # # # # # # #     line = line.strip()
# # # # # # # #
# # # # # # # #     m = p.match(line)
# # # # # # # #     if m:
# # # # # # # #         group = m.groupdict()
# # # # # # # #         id = f"bind{i}"
# # # # # # # #         sgtbind_dict = sgt_dict.setdefault(id, {})
# # # # # # # #         sgtbind_dict['ip'] = str(group["ip"])
# # # # # # # #         sgtbind_dict['prefix'] = str(group["prefix"])
# # # # # # # #         sgtbind_dict['sgt'] = str(group["sgt"])
# # # # # # # #         sgtbind_dict['src'] = str(group["src"])
# # # # # # # #         i += 1
# # # # # # # #         continue
# # # # # # # #
# # # # # # # # print(parsed_dict)
# # # # # # # #
# # # # # # # # import re
# # # # # # # #
# # # # # # # # output = """
# # # # # # # # Group Policy traffic-steering permissions
# # # # # # # #
# # # # # # # # Source SGT      Destination SGT      Steering Policy
# # # # # # # # -----------------------------------------------------
# # # # # # # #     35                36              contract_eng1-02
# # # # # # # # """
# # # # # # # #
# # # # # # # # parsed_dict = {}
# # # # # # # # grppolicy_dict = parsed_dict.setdefault('group_policy_traffic_steering_permissions', {})
# # # # # # # #
# # # # # # # # p = re.compile(r'^(?P<srcsgt>\d+)\s+(?P<destsgt>\d+)\s+(?P<policy>.*)')
# # # # # # # #
# # # # # # # # for line in output.splitlines():
# # # # # # # #     line = line.strip()
# # # # # # # #
# # # # # # # #     m = p.match(line)
# # # # # # # #
# # # # # # # #     if m:
# # # # # # # #         group = m.groupdict()
# # # # # # # #         per_instance_dict = grppolicy_dict.setdefault('per_instance_dict', {})
# # # # # # # #         per_instance_dict['srcsgt'] = str(group["srcsgt"])
# # # # # # # #         per_instance_dict['destsgt'] = str(group["destsgt"])
# # # # # # # #         per_instance_dict['policy'] = str(group["policy"])
# # # # # # # #         continue
# # # # # # # #
# # # # # # # # print(parsed_dict)
# # # # # # # #
# # # # # # # #
# # # # # # # # import re
# # # # # # # #
# # # # # # # # output = """
# # # # # # # # ddmi-cat9300-2#
# # # # # # # # Traffic-Steering SGT Policy
# # # # # # # # ===========================
# # # # # # # # SGT: 35-01
# # # # # # # # SGT Policy Flag: 0x41400001
# # # # # # # # Traffic-Steering Source List:
# # # # # # # #   Source SGT: 35-01, Destination SGT: 36-01
# # # # # # # #   steer_type = 80
# # # # # # # #   steer_index = 1
# # # # # # # #   name   = contract_eng1-02
# # # # # # # #   IP protocol version = IPV4
# # # # # # # #   refcnt = 1
# # # # # # # #   flag   = 0x41400000
# # # # # # # #   stale  = FALSE
# # # # # # # #   Traffic-Steering ACEs:
# # # # # # # #     1 redirect 6 any 23 service service_ENG1
# # # # # # # #     2 redirect 17 any 123 service service_ENG1
# # # # # # # #
# # # # # # # # Traffic-Steering Destination List: Not exist
# # # # # # # # Traffic-Steering Multicast List: Not exist
# # # # # # # # Traffic-Steering Policy Lifetime = 86400 secs
# # # # # # # # Traffic-Steering Policy Last update time = 15:29:30 UTC Wed Jul 7 2021
# # # # # # # # Policy expires in 0:11:26:03 (dd:hr:mm:sec)
# # # # # # # # Policy refreshes in 0:11:26:03 (dd:hr:mm:sec)
# # # # # # # # """
# # # # # # # #
# # # # # # # # # Init vars
# # # # # # # # parsed_dict = {}
# # # # # # # # sgt_dict = parsed_dict.setdefault('sgt_policy', {})
# # # # # # # #
# # # # # # # # p1 = re.compile(r'^(?P<idx1>\d+)\s+redirect\s+(?P<idx2>\d+)\s+any\s+(?P<idx3>\d+)\s+service\s+(?P<ace>.*)')
# # # # # # # # i = 0
# # # # # # # # for line in output.splitlines():
# # # # # # # #     line = line.strip()
# # # # # # # #
# # # # # # # #     m = p1.match(line)
# # # # # # # #     if m:
# # # # # # # #         group = m.groupdict()
# # # # # # # #         id = f"ACE{i}"
# # # # # # # #         one_proc_dict = sgt_dict.setdefault(id, {})
# # # # # # # #         one_proc_dict['idx1'] = str(group['idx1'])
# # # # # # # #         one_proc_dict['idx2'] = str(group['idx2'])
# # # # # # # #         one_proc_dict['idx3'] = str(group['idx3'])
# # # # # # # #         one_proc_dict['ace'] = str(group['ace'])
# # # # # # # #         i += 1
# # # # # # # #         continue
# # # # # # # #
# # # # # # # # print(parsed_dict)
# # # # # # # #
# # # # # # # # import re
# # # # # # # #
# # # # # # # # output = """
# # # # # # # # ddmi-cat9300-2#
# # # # # # # # Steering Policy contract_eng1-02
# # # # # # # #     1 redirect protocol 6 src-port any dst-port eq 23 service service_ENG1 (625 matches)
# # # # # # # #     2 redirect protocol 17 src-port any dst-port eq 123 service service_ENG1 (0 match)
# # # # # # # # """
# # # # # # # #
# # # # # # # # # Init vars
# # # # # # # # parsed_dict = {}
# # # # # # # # policy_dict = parsed_dict.setdefault('steering_policy', {})
# # # # # # # #
# # # # # # # # p1 = re.compile(r'^Steering\s+Policy\s+(?P<name>.*)')
# # # # # # # #
# # # # # # # # for line in output.splitlines():
# # # # # # # #     line = line.strip()
# # # # # # # #
# # # # # # # #     m = p1.match(line)
# # # # # # # #     if m:
# # # # # # # #         group = m.groupdict()
# # # # # # # #         per_instance_dict = policy_dict.setdefault('per_instance_dict', {})
# # # # # # # #         per_instance_dict['policy_name'] = str(group['name'])
# # # # # # # #         continue
# # # # # # # #
# # # # # # # # print(parsed_dict)
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # #
# # # # # # # #compare and swap
# # # # # # #
# # # # # # # def compare_swap(node, expect, new):
# # # # # # #     current = ram.get(node)
# # # # # # #     if current == expect:
# # # # # # #         ram.set(node, new)
# # # # # # #     return current
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # #linked list based
# # # # # # #
# # # # # # # def enqueue(x):
# # # # # # #     q = new_record()
# # # # # # #     q.value = x
# # # # # # #     q.next = Null
# # # # # # #
# # # # # # #     #repeat
# # # # # # #         p = tail
# # # # # # #         result = compare_swap(p.next, null,q)
# # # # # # #     size = size + 1
# # # # # # # def dequeue():
# # # # # # #     #repeat
# # # # # # #         p = head
# # # # # # #         if p.next == Null:
# # # # # # #             return "ERROR"
# # # # # # #         else:
# # # # # # #             #repeat until this is not
# # # # # # #             compare_swap(head, p, p.next)
# # # # # # #         self.size -= 1
# # # # # # #         return p.next.value
# # # # # # #
# # # # # # #
# # # # # # # def is_empty(head):
# # # # # # #     #check if the list is empty
# # # # # # #     if head is None:
# # # # # # #         print("list has no element")
# # # # # # #         return
# # # # # # #     #check if the end of the ll size
# # # # # # #     #size = len()
# # # # # # # def find_len(head):
# # # # # # #     i = 0
# # # # # # #     current = head
# # # # # # #     while current:
# # # # # # #         current = current.next
# # # # # # #         i += 1
# # # # # # #     return i
# # # # # # #
# # # # # # # def is_full(length):
# # # # # # #     if self.size <= length:
# # # # # # #         return "size if ull"
# # # # # # #
# # # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # int main()
# # # # # # {
# # # # # #     unsigned int data = 0x1234;
# # # # # #     data = ((data << 8) & 0xff00) | ((data>>8) & 0x00ff);
# # # # # #
# # # # # # }
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # int main()
# # # # # # {
# # # # # #
# # # # # #     int data = 0xaabbccdd;
# # # # # #     int lmostbyte;
# # # # # #     int lmiddlebyte;
# # # # # #     int rmostbyte;
# # # # # #     int rmiddlebyte;
# # # # # #     int result;
# # # # # #
# # # # # #     lmostbyte = (data & 0x000000FF) >> 0;
# # # # # #     lmiddlebyte = (data & 0x0000FF00) >> 8;
# # # # # #     rmiddlebyte = (data & 0x00FF0000) >> 16;
# # # # # #     rmostbyte = (data & 0xFF000000) >> 24;
# # # # # #
# # # # # #     lmostbyte <<= 24;
# # # # # #
# # # # # #     lmiddlebyte <<= 16;
# # # # # #     rmiddlebyte <<= 8;
# # # # # #
# # # # # #     rmostbyte <<= 0
# # # # # #
# # # # # #     result = ( lmostbyte | lmiddlebyte | rmostbyte | rmiddlebyte);
# # # # # #     return result;
# # # # # #
# # # # # #
# # # # # # }
# # # # # #
# # # # # # void delnode(struct node *ref)
# # # # # # {
# # # # # # while (ref -> next != NULL)
# # # # # #     {
# # # # # #         ref->data = ref->next->data;
# # # # # #         ref = ref->next;
# # # # # #
# # # # # #     }
# # # # # #     free(ref)
# # # # # # }
# # # # # #
# # # # # # void dup_delete(struct node **head)
# # # # # # {
# # # # # #     struct node *p , *q, *prev, *temp;
# # # # # #
# # # # # #     p = q = prev = *head;
# # # # # #     q = q-> next;
# # # # # #
# # # # # #     while (p != NULL)
# # # # # #         {
# # # # # #             while ( q != NULL && q->value != p -> value)
# # # # # #             {
# # # # # #                 prev = q;
# # # # # #                 q = q->next;
# # # # # #             }
# # # # # #             if ( q == NULL)
# # # # # #                 {
# # # # # #                     p = p->next;
# # # # # #                     if ( p != NULL)
# # # # # #                     {
# # # # # #                         q = p->next;
# # # # # #                     }
# # # # # #                 }
# # # # # #             else {
# # # # # #                 if (q->value == p->value){
# # # # # #                     prev->next = q->next;
# # # # # #                     temp = q;
# # # # # #                     q = q->next;
# # # # # #                     free(temp);
# # # # # #             }
# # # # # #             }
# # # # # #
# # # # # #         }
# # # # # #
# # # # # # }
# # # # #
# # # # #
# # # # # import re
# # # # # import glob
# # # # # import os
# # # # #
# # # # # out = '''
# # # # # C9300L-24P-4G#dir bootflash:guest-share/ddr/linkchaos/
# # # # # Directory of flash:guest-share/ddr/linkchaos/
# # # # #
# # # # # 417794  -rw-         43430304  Jul 20 2021 14:14:26 +00:00  C9300L-24P-4G_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_6374_20210720-141236-UTC.core.gz
# # # # # 417793  -rw-         43431510  Jul 20 2021 14:14:26 +00:00  C9300L-24P-4G_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_5070_20210720-141206-UTC.core.gz
# # # # # 409617  -rw-         43435792  Jul 20 2021 14:14:26 +00:00  C9300L-24P-4G_1_RP_0_x86_64_crb_linux_iosd_ngwc-universalk9-ms_10032_20210720-141358-UTC.core.gz
# # # # # 409614  drwx             4096  Jul 20 2021 14:12:01 +00:00  __pycache__
# # # # # 409613  -rw-            96105  Jul 20 2021 14:11:47 +00:00  rp_base.cdb
# # # # # 409612  -rw-             1762  Jul 20 2021 14:11:26 +00:00  linkchaos.py
# # # # # 409611  -rw-            58128  Jul 20 2021 14:11:02 +00:00  genie_parsers.py
# # # # # 409610  -rw-            23817  Jul 20 2021 14:11:01 +00:00  ddrlib.py
# # # # #
# # # # # '''
# # # # #
# # # # # pattern = re.compile(r'.*gz')
# # # # # matches = pattern.findall(out)
# # # # # core = []
# # # # # for match in matches:
# # # # #     print(match)
# # # # #     x = match.split()
# # # # #     core.append(x[8])
# # # # # print(core)
# # # # #
# # # # # def get_timestamp(file_name):
# # # # #     return file_name.split("_")[-1].split('.')[0]
# # # # #
# # # # # sorted_list = sorted(core, key=get_timestamp)
# # # # # print(sorted_list)
# # # # #
# # # # # for i in sorted_list:
# # # # #     print(i)
# # # # #
# # # #
# # # #
# # # # 0xffffffff
# # # #
# # # #
# # # # 0x10101
# # # # 0x01010
# # # #
# # # # unsigned int oddbits(unsigned int x)
# # # # {
# # # #     unsigned int odd_bits = x & 0x55555555;
# # # #
# # # #     odd_bits <<= 1;
# # # #
# # # #     return (odd_bits);
# # # #
# # # # }
# # # #
# # # #
# # # # int flipbits (int n , int k)
# # # # {
# # # #     int mask = (1 << k) - 1;
# # # #     return ~n & mask;
# # # #
# # # # }
# # # #
# # # #
# # # # void insert (int value)
# # # # {
# # # #     int key = value % size;
# # # #
# # # #     if (arr[key] == -1)
# # # #         {
# # # #             arr[key] = value;
# # # #             printf("%d inserted at arr[%d]", value, key)
# # # #         }
# # # #         else
# # # #         {
# # # #             *temp = arr[key];
# # # #         while(temp->next)
# # # #             {
# # # #                 temp = temp->next;
# # # #             }
# # # #             temp->next = new_node
# # # #
# # # #         }
# # # # }
# # # #
# # # #
# # # #
# # # #
# # # # #include <stdio.h>
# # # # #define size 10
# # # #
# # # # struct node {
# # # #             int data;
# # # #             struct node *next;
# # # #         };
# # # #
# # # # struct node *arr[size]
# # # #
# # # # void init()
# # # #         {
# # # #
# # # #             int i;
# # # #             for (i=0; i <size; i++)
# # # #                 arr[i] = NULL;
# # # #         }
# # # #
# # # # void inse(int value)
# # # #             {
# # # #             //create  a new node with value
# # # #             struct node *newnode = malloc(sizeof(struct node));
# # # #             newnode->data = value;
# # # #             newn0de->next = NULL;
# # # #
# # # #             //calculate the hask key
# # # #             int key = value % size;
# # # #
# # # #             //check if arr[key] is empty
# # # #             if (arr[key] == NULL)
# # # #             {
# # # #                 arr[key] = newnode;
# # # #         } else {
# # # #             // add the new node at the end of the chain
# # # #
# # # #             struct node *temp = arr[key];
# # # #             while (temp->next)
# # # #                 {
# # # #                     temp = temp->next
# # # #                 }
# # # #                 temp->next = ndenode
# # # #         }
# # # # }
# # # #
# # # #
# # # #             }
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # import re
# # #
# # # entry = '''
# # # ,            ddr-facts         ddr-facts-onbox   ddr-flags-onbox   ddr-rules-onbox    newintf-flags  tac_cpu     testnf-facts   trigger-flags
# # # __pycache__  ddr-facts-bad     ddr-flags         ddr-rules         interface_dynamic  newintf-rules  tcam-facts  testnf-rules
# # # ddr-devices  ddr-facts-offbox  ddr-flags-offbox  ddr-rules-offbox  newintf-facts      pybasic        tcam-rules  trigger-facts
# # # ddr-action.1 ddr-action.2
# # #
# # # '''
# # #
# # # p = re.compile(r'^ddr-action\.(?P<no>\d)')
# # # alist = []
# # # for line in entry.split():
# # #     print(line)
# # #     line = line.strip()
# # #     m = p.match(line)
# # #     if m:
# # #         print("karthik")
# # #         alist.append(line)
# # # print(alist)
# # # print(type(alist))
# # #
# # # for a in alist:
# # #     print(a)
# # #     print(type(a))
# #
# #
# monthly_challenge = {
#     "january": "This is january!",
#     "february": "This is february!",
#     "march": "This is march!",
#     "april": "This is april!",
#     "may": "This is may!",
#     "june": "This is june!",
#     "july": "This is july!",
#     "august": "This is August!",
#     "september": "This is september!",
#     "october": "This is october!",
#     "november": "This is november!",
#     "december": "This is december!",
# }
# #
# #
# # list_it = list(monthly_challenge.keys())
# # print(type(list_it))
# # print(list_it)
#
# print(monthly_challenge)
# monthly_challenge.update({"january": "this is karthik"})
# print(monthly_challenge)
#


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def full_name(self):
        return "{} {}".format(self.first, self.last)

emp1 = Employee("Karthik", "Babu")
emp1.first = "Lakshmi"
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.full_name())