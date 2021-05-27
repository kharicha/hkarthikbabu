# from collections import deque
# import time
# import threading
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
#
#     def dequeue(self):
#         if len(self.buffer) == 0:
#             print ("Queue is empty")
#
#         return self.buffer.pop()
#
#     def is_empty(self):
#         return len(self.buffer) == 0
#
#     def size(self):
#         return len(self.buffer)
#
# foodq = Queue()
#
# def place_order(orders):
#     for order in orders:
#         print("Placing order", order)
#         foodq.enqueue(order)
#         time.sleep(0.5)
#
# def serve_order():
#     time.sleep(1)
#     while not foodq.is_empty():
#         order = foodq.dequeue()
#         print("Now Serving order", order)
#         time.sleep(2)
#
# if __name__ == '__main__':
#     orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#
# t1 = threading.Thread(target=place_order, args=(orders,))
# t2 = threading.Thread(target=serve_order)
#
# t1.start()
# t2.start()

#heapify - min heap

# import time
# import heapq as hq
#
# # jobs to be executed
# jobs = [(2, 'task_1'), (5, 'task_2'), (1, 'task_4'),
#         (4, 'task_5'), (3, 'task_3'), (1, 'task_8')]
#
# # interrupts
# interrupts = [(1, 'intr_1'), (2, 'intr_2'), (13, 'intr_3')]
#
# #arrange jobs
# hq.heapify(jobs)
# print(jobs)

