'''
Question 3.4
'''
from stack import Stack


class Queue:
    def __init__(self):
        self.__in_stack = Stack()
        self.__out_stack = Stack()
        self.__length = 0

    def __update(self):
        while self.__in_stack:
            value = self.__in_stack.pop()
            self.__out_stack.push(value)

    def isEmpty(self):
        return self.__length == 0

    def enqueue(self, value):
        self.__in_stack.push(value)
        self.__length += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        if len(self.__out_stack) == 0:
            self.__update()
        self.__length -= 1
        return self.__out_stack.pop()


def tests():
    q = Queue()

    # enques some values, deque first three, enque 3 more, check
    # dequeued values abide by FIFO rule
    passes = True
    a = [5, 1, 4, 7, 8, 10, 9]
    for i in a:
        q.enqueue(i)

    x = [q.dequeue() for _ in range(3)]
    result = x == a[:3]
    if result:
        print('First three dequed properly')
    else:
        print('First three dequed incorrectly')
        passes = False

    # refresh
    b = [11, 12, 13]
    for i in b:
        q.enqueue(i)

    x = [q.dequeue() for _ in range(4)]
    result = x == a[3:]
    if result:
        print('Next four values dequed properly')
    else:
        print('next four values dequed incorrectly')
        passes = False

    empty = q.isEmpty()
    print(f'Queue emptied (should be False): {empty}')
    if empty:
        passes = False

    x = [q.dequeue() for _ in range(3)]
    result = b == x
    if result:
        print('Last three values dequeued properly')
    else:
        print('Last three values dequeued incorrectly')
        passes = False

    empty = q.isEmpty()
    print(f'Queue now empty (should be True): {empty}')
    if not result or not empty:
        passes = False

    print(f'tests pass: {passes}')

if __name__ == '__main__':
    tests()
