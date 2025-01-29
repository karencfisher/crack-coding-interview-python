'''
Base class for stack questions (chapter 3)

All operations O(1) time
'''

class Stack:
    def __init__(self):
        self.stack = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def isEmpty(self):
        return self.__length == 0

    def push(self, value):
        self.stack.append(value)
        self.__length += 1

    def pop(self):
        if self.isEmpty():
            return None
        value = self.stack.pop()
        self.__length -= 1
        return value

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]


