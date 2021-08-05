# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# # is_balanced("({a+b})")     --> True
# # is_balanced("))((a+b}{")   --> False
# # is_balanced("((a+b))")     --> True
# # is_balanced("))")          --> False
# # is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

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

def is_match(ch1, ch2):
    match_dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    return match_dict[ch1] == ch2

def parvalid(str):

    s = Stack()
    for ch in str:
        if ch == '(' or ch == '[' or ch == '{':
            s.push(ch)
        if ch == ')' or ch == ']' or ch == '}':
            if s.size() == 0:
                return False
            if not is_match(ch, s.pop()):
                return False

    return s.size() == 0

if __name__ == '__main__':
    print(parvalid("({a+b})"))
    print(parvalid("))((a+b}{"))
    print(parvalid("((a+b))"))
    print(parvalid("((a+g))"))
    print(parvalid("))"))
    print(parvalid("[a+b]*(x+2y)*{gg+kk}"))