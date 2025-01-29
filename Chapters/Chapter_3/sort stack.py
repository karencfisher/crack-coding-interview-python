'''
Question 3.5
'''
from stack import Stack


class SortStack:
    def __init__(self):
        self.__stack = Stack()
        self.__sorting_stack = Stack()

    def push(self, value):
        while not self.__stack.isEmpty() and self.__stack.peek() < value:
            x = self.__stack.pop()
            self.__sorting_stack.push(x)

        self.__stack.push(value)

        while not self.__sorting_stack.isEmpty():
            x = self.__sorting_stack.pop()
            self.__stack.push(x)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack.peek()

    def isEmpty(self):
        return self.__stack.isEmpty()


def tests():
    a = [5, 10, 3, 7, 6, 4, 8, 2, 9, 1]
    s = SortStack()
    for i in a:
        s.push(i)

    # values should pop off in sorted order
    results = []
    while not s.isEmpty():
        results.append(s.pop())
    print(results)

if __name__ == '__main__':
    tests()