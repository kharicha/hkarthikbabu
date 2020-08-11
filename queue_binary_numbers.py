from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print ("Queue is empty")

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def produce_bin(n):
    numq = Queue()
    numq.enqueue("1")

    for i in range(n):
        front = numq.front()
        print(front)
        numq.enqueue(front + "0")
        numq.enqueue(front + "1")
        numq.dequeue()


if __name__ == '__main__':
   produce_bin(10)


