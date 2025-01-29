'''
Question 4.3

Make linked list pf levels of a tree (as a BST)
'''

from make_bst import make_BST

class LinkedList:
    class Node:
        def __init__(self, payload):
            self.payload = payload
            self.next = None
            
    def __init__(self):
        self.__head = LinkedList.Node(0)
        self.__tail = self.__head
        
    @property
    def llist(self):
        return self.__head.next
        
    def __add__(self, payload):
        self.__tail.next = LinkedList.Node(payload)
        self.__tail = self.__tail.next
        return self
        
    def __str__(self):
        items = ''
        node = self.__head.next
        if node is not None:
            while node.next is not None:
                items += f'{node.payload}-->'
                node = node.next
            items += str(node.payload)
        return items


def list_levels(tree):
    level_list = LinkedList()
    que = [[tree]]
    while que:
        nodes = que.pop(0)
        level_list += [None if node is None else node.payload for node in nodes]
        level = []
        for node in nodes:
            level += [None] if node is None else [node.left]
            level += [None] if node is None else [node.right]
        if any([n is not None for n in level]):
            que.append(level)
    return str(level_list)

if __name__ == '__main__':
    items = [1, 2, 4, 7, 9, 13, 18, 25, 27]
    bst = make_BST(items)
    print(list_levels(bst))
    