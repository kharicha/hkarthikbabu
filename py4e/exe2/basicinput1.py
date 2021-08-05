#1, Get the input from the user and welcome with the entered name
# wel = input("Please specify your Name:")
# print("Hello", wel)

#2 Get the hour worked and the hourly rate, calculate and provide the gross pay
# hour = int(input("Please specify the hour worked: "))
# rate = float(input("Please specify the hourly rate "))
#
# print("Gross Pay =", hour*rate)

#3 Prompts the user for celsius temp, convert and print the temp in fahrenheit

# temp = float(input("Please enter the temp in celsius: "))
# print("Temp in fahrenheit is ", (temp  * 1.8) + 32)

#4 Rewrite the pay compuation of problem 2 > if the employee works more than 40hours rate = 1.5 times of rate
# hours = 45
# rate = 10
# pay = 475

# hour = int(input("Please specify the hour worked: "))
# rate = float(input("Please specify the hourly rate "))
#
# if hour > 40:
#     print("Gross Pay =", (hour - 40) * (rate * 1.5) + (40 * rate))
# else:
#     print("Gross Pay =", hour * rate)

#5 Rewrite the pay compuation of problem using try/except method

# try:
#     hour = int(input("Please specify the hour worked: "))
#     rate = float(input("Please specify the hourly rate "))
# except:
#     print("error, please enter numeric value")
#     quit()
#
# if hour > 40:
#     print("Gross Pay =", (hour - 40) * (rate * 1.5) + (40 * rate))
# else:
#     print("Gross Pay =", hour * rate)

#6 Prompt user with score and passed on that award grade
# SCORE = 0.95
# output : A

# try:
#     score = float(input("Please enter the score: "))
# except:
#     print("error, please enter numeric value")
#     quit()
#
# if score < 0 or score > 1.0:
#     print("score provided is out of range")
# elif score >= 0.9:
#     print ("A")
# elif score >= 0.8:
#     print ("B")
# elif score >= 0.7:
#     print ("C")
# elif score >= 0.6:
#     print ("D")
# else:
#     print("F")

#7 Pay calculation into a function

# def computepay(hour, rate):
#     if hour > 40:
#         pay = (hour - 40) * (rate * 1.5) + (40 * rate)
#     else:
#         pay = (hour * rate)
#     return pay
#
# hour = int(input("Please specify the hour worked: "))
# rate = float(input("Please specify the hourly rate "))
#
# gross = computepay(hour, rate)
# print("Gross is ", gross)

#8 Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered,
# print out the total, count, and average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and skip to the next number.

# count = 0
# total = 0
#
# while True:
#     str_val = input("Please specify the hour worked: ")
#     if str_val == 'done':
#         break
#     try:
#         val = float(str_val)
#     except:
#         print("error, please enter numeric value")
#         continue
#
#     total = total + val
#     count += 1
#
# print("Total:  count:  Average: ",total, count, total//count)

#9 Write another program that prompts for a list of numbers as above and at the end prints out both the maximum
# and minimum of the numbers instead of the average.

# min = 0
# max = 0
# count = 0
#
# while True:
#     str_val = input("Please specify the hour worked: ")
#     if str_val == 'done':
#         break
#     try:
#         val = float(str_val)
#     except:
#         print("error, please enter numeric value")
#         continue
#
#     if count == 0:
#         min = val
#         max = val
#     elif val < min:
#         min = val
#     elif  val > max:
#         max = val
#
#     count +=1
#
# print("min:  max:  ", min, max)

#10 Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the colon character
#and then use the float function to convert the extracted string into a floating point number.

# str = 'X-DSPAM-Confidence:0.8475'
# print(float((str[str.find(":")+1:])))

#11 Write a program to read through a file and print the contents of the file (line by line) all in upper case.
# Executing the program will look as follows:

# fd = open("file_name", r)
# for line in fd:
#     print(line.upper())

#12 Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

# valli = []
#
# while True:
#     str_val = input("Please specify the numbers: ")
#     if str_val == 'done':
#         break
#     try:
#         val = float(str_val)
#     except:
#         print("error, please enter numeric value")
#         continue
#     valli.append(val)
#
# print('min', sorted(valli)[0], 'max:', sorted(valli)[len(valli)-1])
# print('min:', min(valli), 'max:', max(valli))

