'''
Classes for link list questions (chapter 2)

building list: O(n) time
adding node: O(1) time
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, array):
        self.head = Node(None)
        self.tail = None
        self.length = 0

        node = self.head
        for item in array:
            node.next = Node(item)
            node = node.next
            self.tail = node
            self.length += 1
        self.head = self.head.next

    def add_node(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1

    def __add__(self, other):
        # overload '+' operator as concatenation
        # 'other' can be another instance of LinkList, or
        # an instance of Node
        if isinstance(other, LinkList):
            self.add_node(other.head)
            self.length += other.length - 1
            self.tail = other.tail
        else:
            self.add_node(other)

    def __len__(self):
        return self.length

    def __str__(self):
        node = self.head
        link_list = []
        while node is not None:
            link_list.append(str(node.data))
            node = node.next
        return '->'.join(link_list)
        

def test():
    # test concatnation of lists
    a = [1, 2, 3]
    b = [4, 5, 6]
    la = LinkList(a)
    la + LinkList(b)
    # concatenate a single node
    la + Node(7)
    # and a value (creating Node)
    la + 8
    print(f'Concatenated list: {la}')
    print(f'length = {len(la)}')

if __name__ == '__main__':
    test()
