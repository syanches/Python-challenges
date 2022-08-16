class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

# stack = Stack()
# print(stack.is_empty())

# stack.push(19)
# stack.push(1)
# stack.push(3)
# stack.push(44)

# print(stack.is_empty())

# item = stack.pop()

# print(item)

# print(stack.is_empty())

# for i in range(0,6):
#     stack.push(i)


# print(stack.peek())
# print(stack.size())

# stack_new = Stack()
# for c in "Hello":
#     stack_new.push(c)

# print(stack_new.items)

# reverse = ""

# for i in range(len(stack_new.items)):
#     reverse += stack_new.pop()

# print(reverse)


# class Queue():
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return self.items == []

#     def enqueue(self, item):
#         self.items.insert(0, item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)

# a_queue = Queue()
# print(a_queue.is_empty())

# for i in range(5):
#     a_queue.enqueue(i)

# print(a_queue.items)

# for i in range(5):
#     a_queue.dequeue()

# print(a_queue.items)


# import time
# import random

# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return self.items == []

#     def enqueue(self, item):
#         self.items.insert(0, item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)

#     def simulate_line(self, till_show, max_time):
#         pq = Queue()
#         tix_sold = []

#         for i in range(100):
#             pq.enqueue("кинофанат" + str(i))

#         t_end = time.time() + till_show
#         now = time.time()
#         while now < t_end and not pq.is_empty():
#             now = time.time()
#             r = random.randint(0, max_time)
#             time.sleep(r)
#             person = pq.dequeue()
#             print(person)
#             tix_sold.append(person)
        
#         return tix_sold

# queue = Queue()
# sold = queue.simulate_line(100, 1)
# print(sold)


stack = Stack()
word = "позавчера" 
reverse = ""
for letter in word:
    stack.push(letter)

print(stack.items)

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)

list = [1,2,3,4,5]
reversed_list = []

stack_list = Stack()
for i in list:
    stack_list.push(i)

for i in range(len(stack_list.items)):
    reversed_list.append(stack_list.pop())

print(reversed_list)