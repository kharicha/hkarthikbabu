#1 hello world

input_string = input()
print("Hello World")
print(input_string)

#2 Data types

i = 4
d = 4.0
s = 'HackerRank '

i_i = int(input())
d_d = float(input())
s_s = input()

print(i + i_i)
print(d + d_d)
print(s + s_s)

#3 Operators

meal_cost = float(input())
# tip_percent = int(input())
# tax_percent = int(input())
#
# tip = meal_cost * (tip_percent / 100)
# tax = meal_cost * (tax_percent / 100)
# total_cost = meal_cost + tip + tax
# print(round(total_cost))

#4 conditional statements

n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range(2, 6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#5 class vs instance

class Person():
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = initialAge

    def get_age(self):
        return self.age

    def year_passes(self):
        self.age += 1

    def amiOld(self):
        if self.age < 13:
            print("You are Young")
        elif self.age < 18:
            print("You are teenager")
        else:
            print("You are old")

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amiOld()
    for j in range(0, 3):
        p.year_passes()
    p.amiOld()
    print("")

#6 Loops

#Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.

n = int(input())
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(n*i))
    product = n * i
    print( '{} x {} = {}'.format(n, i, product))

#7 Given a string, , of length  that is indexed from  to ,
# print its even-indexed and odd-indexed characters as  space-separated strings on a single line

n = int(input())
for i in range(n):
    s = input()
    eve = ''
    odd = ''
    for i in range(len(s)):
        if i == 0:
            eve += s[i]
        elif i%2 == 0:
            eve += s[i]
        else:
            odd += s[i]
    print('{} {}'.format(eve, odd))

#8 Arrays - reverse an array

n = int(input())
arr = []
for i in range(n):
    g = int(input())
    arr.append(g)
print(arr)
print(arr[::-1])

#9 Dictionary

n = int(input())
d = dict()
for i in range(n):
    ph = input().strip().split(' ')
    d[ph[0]] = ph[1]

for key, val in d.items():
    print('{} =  {}'.format(key, val))

query = input()
while query:
    pn = d.get(query)
    if pn:
        print(query + "=" + pn)
    else:
        print("Not Found")
    query = input()

#10 Recursion

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

#11 Binary Numbers

n = int(input().strip())

current_consecutive_1s = 0
max_consecutive_1s = 0
while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_consecutive_1s += 1
        if current_consecutive_1s > max_consecutive_1s:
            max_consecutive_1s = current_consecutive_1s
    else:
        current_consecutive_1s = 0
    n = n // 2

print(max_consecutive_1s)

#12 2D Arrays

#13 Inheritance

class Person():
    def __init__(self, fn, ln, id):
        self.fn = fn
        self.ln = ln
        self.id = id

    def printperson(self):
        print("Name:", self.ln + ",", self.fn)
        print("ID:", self.id)

class Student(Person):
    def __init__(self, fn, ln, id, sc):
        Person.__init__(self, fn, ln, id)
        self.sc = sc

    def cal(self):
        sum = 0
        for a in self.sc:
            sum += a
        avg = sum // len(self.sc)

        if avg < 40:
            return 'T'
        elif avg < 55:
            return 'D'
        elif avg < 70:
            return 'P'
        elif avg < 80:
            return 'A'
        elif avg < 90:
            return 'E'
        else:
            return 'O'

line = input().split()
fn = line[0]
ln = line[1]
id = line[2]
sc = list(map(int, input().split()))
print(sc)
s = Student(fn, ln, id, sc)
s.printperson()
print("Grade:", s.cal())

# 14 Abstract classes
from abc import ABCMeta, abstractmethod

class Book():
    def __init__(self, title, aut):
        self.title = title
        self.aut = aut

    @abstractmethod
    def display(): pass


class MyBook(Book):
    def __init__(self, title, aut, pri):
        Book.__init__(self, title, aut)
        self.price = pri

    def display(self):
        print("Title: ", self.title)
        print("Author: ", self.aut)
        print("Price: ", self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

#15 Scope

class Diff():
    def __init__(self, ele):
        self.elements = ele
        self.md = 0

    def computediff(self):
        s_ele = sorted(self.elements)
        print(s_ele)
        min_ele = s_ele[0]
        max_ele = s_ele[-1]

        self.md = max_ele - min_ele

_ = input()
a = [int(e) for e in input().split(' ')]

d = Diff(a)
d.computediff()

print(d.md)

#same above problem which we could solve using iterative method
#the integers is between 1 - 100

    def computediff(self):
       min_ele = 101
       max_ele = 0
       for e in self.elements:
           if e < min_ele:
               min_ele = e
            if e > max_ele:
                max_ele = e
        self.md = max_ele - min_ele

#16 Linked List

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node

class Solution:
    def display(self, head):
        if head == None:
            return -1
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)

#17 Exceptions - String to Integer

s = input().strip()

try:
    int_value = int(s)
    print(int_value)

except ValueError:
    print("Bad String")

#18 throwing exceptions

class Cal():

     def power(self, n, p):
         if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
         else:
              return pow(n, p)

myCalculator=Cal()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)

#19 Stack and Queue

from collections import deque

class Solution():

    def __init__(self):
        self.queue = deque()
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def enqueue(self, value):
        self.queue.appendleft(value)

    def pop(self):
        return self.stack.pop()

    def dequeue(self):
        return self.queue.pop()


s = input()
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.push(s[i])
    obj.enqueue(s[i])

isPalindrome=True

for i in range(l // 2):
    if obj.pop()!=obj.dequeue():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print ("The word, "+s+", is a palindrome.")
else:
    print ("The word, "+s+", is not a palindrome.")

sum of n numbers with iterative and recusrion

def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(sum(100))

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
print(sum(100))

#20 BST - Creation and height of the tree

class Node():
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Solution():
    def insert(self, root, data):
        if root == None:
            root = Node(data)
        else:
            if data <= root.data:
                curr = self.insert(root.left, data)
                root.left = curr
            else:
                curr = self.insert(root.right, data)
                root.right = curr
        return root

    def getHeight(self, root):

        if not root:
            return -1

        elif not root.left and not root.right:
            return 0

        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)

        return max(lh, rh) + 1


T = int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print (height)

#21BST Level Order Traversal using Queue

class Node():
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

class Solution():
    def insert(self, root, data):
        if root == None:
            root = Node(data)
        else:
            if data <= root.data:
                curr = self.insert(root.left, data)
                root.left = curr
            else:
                curr = self.insert(root.right, data)
                root.right = curr
        return root

    def levelOrder(self, root):

        if root is None:
            return

        queue = []
        queue.append(root)
        res = []

        while len(queue) > 0:
            print(queue[0].data)
            res.append(queue[0].data)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print(res)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)

#22 Linked List - Remove duplicates

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        # 3 condition s for inserting a new node to a LL
        # CHECK HEAD ID AVAILABLE
        p = Node(data)
        if head == None:
            head = p
        # check if there is next for the head
        elif head.next == None:
            head.next = p
         # if above 2 conditions are not met the we need to iterate through last of the list and add this new node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = p
        return head

    def display(self,head):
        current = head
        while current:
            print(current.data)
            current = current.next

    def removeDuplicates(self, head):

        if not head:
            return None
        curr = head
        while curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head



mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);

#22 Prime Number

n = int(input())
if n > 1:
    for i in range(2,n):
        if (n%i) == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#23 Nested Logic

return_day, return_month, return_year = [int(e) for e in input().strip().split(' ')]
due_day, due_month, due_year = [int(e) for e in input().strip().split(' ')]

if return_year < due_year:
    print (0)
elif return_year == due_year:
    if return_month == due_month:
        if return_day <= due_day:
            print (0)
        elif return_day > due_day:
            fine = 15 * (return_day - due_day)
            print ("{} Hakcos".format(fine))
    elif return_month > due_month:
        fine = 500 * (return_month - due_month)
        print("{} Hakocs".format(fine))
    else:
        print(0)
else:
    print ('10000 Hackos')

#24 Insert Node at a specifc location in the Linked List

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if head == None:
        head = new_node
    elif position == 0:
        new_node.next = head
        head = new_node
    else:
        pos = 0
        prev = None
        curr = head
        while (pos < position) and curr.next:
            prev = curr
            curr = curr.next
            pos += 1
        prev.next = new_node
        new_node.next = curr
    return head