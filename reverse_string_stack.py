#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def rev(string):
    s = Stack()

    for ch in string:
        s.push(ch)

    rstr = ''
    while s.size() > 0:
        rstr += s.pop()

    return rstr

if __name__ == '__main__':
    print(rev("We will conquere COVI-19"))
    print(rev("I am the king"))



