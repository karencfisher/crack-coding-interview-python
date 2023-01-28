'''
Question 3.2

The basic approach here is using a secondary stack to keep track of
the min values pushed to the stack at any point in time. When a value
<= the top item in the min stack, it is pushed on to both stacks. When
a value is popped off the stack, if it correponds to the top value in
the min stack, both are popped off.

Inherits from the stack base class (stack.py). Operations all O(1) time.
'''
from stack import Stack


class MinStack(Stack):
    def __init__(self):
        super(MinStack, self).__init__()
        self.__min_stack = []

    def push(self, value):
        if self.isEmpty():
            self.__min_stack.append(value)
        elif value <= self.min():
            self.__min_stack.append(value)
        super(MinStack, self).push(value)

    def pop(self):
        if self.isEmpty():
            return None
        value = super(MinStack, self).pop()
        if value == self.min():
            assert len(self.__min_stack) > 0, 'min stack empty!'
            self.__min_stack.pop()
        return value

    def min(self):
        if self.isEmpty():
            return None
        assert len(self.__min_stack) > 0, 'min stack empty!'
        return self.__min_stack[-1]


def tests():
    stack = MinStack()
    stack.push(5)
    print(stack.min())

    stack.push(3)
    print(stack.min())

    stack.push(5)
    print(stack.min())
    print(stack.peek())

    stack.pop()
    print(stack.min())
    print(stack.peek())

    stack.pop()
    print(stack.min())

    stack.pop()
    print(stack.min())

    stack.push(5)
    print(stack.min())

if __name__ == '__main__':
    tests()
