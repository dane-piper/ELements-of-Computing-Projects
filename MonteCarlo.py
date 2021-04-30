import random
from math import pi


import math
import os
import random
import re
import sys

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

    # function for testing. displays the contents of your queue
    def display(self):
        for item in self.queue:
            print(item + ", ", end="")
        print()
#
# This is the 'main' function, make the program work by writing HELPER FUNCTIONS.
#
# The function is expected to return a List of strings.
# The function accepts a list of strings numbers as parameter.
#
#input is a char and returns a number value from dictionary
def chartonum(c, dict):
    return dict.get(c, '')
def sort(numbers, dict):
    longest = len(numbers[0])
    for lens in range(1, len(numbers)):
        current = len(numbers[lens])
        if current > longest:
            longest = current
    print(longest)
    queues = []
    length = len(numbers)
    for i in range(35):
        queues.append(Queue())
    for n in range(longest):
        for idx in range(len(numbers)):
            nums = numbers.pop(0)
            x = chartonum(nums[-n], dict)
            print(x)
            queues[x].enqueue(nums)
        for que in queues:
            que.display()
            size = que.size()
            for l in range(size):
                numbers.append(que.dequeue())
        print('pass: ' + str(n))
    return numbers
def main():
    # We went ahead and created the dictionary for you
    dict = {
        '0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,
        'a': 10,'b': 11,'c': 12,'d': 13,'e': 14,'f': 15,'g': 16,'h': 17,'i': 18,
        'j': 19,'k': 20,'l': 21,'m': 22,'n': 23,'o': 24,'p': 25,'q': 26,'r': 27,
        's': 28,'t': 29,'u': 30,'v': 31,'w': 32,'x': 33,'y': 34,'z': 35
    }
    numbers = ['311', '96', '495', '137', '158', '84', '145', '63','10000']
    sort(numbers, dict)

main()
