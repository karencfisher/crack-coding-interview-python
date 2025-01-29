'''
Question 4.2

From sorted list build binary search tree with least levels
'''

class Node:
    def __init__(self, payload):
        self.payload = payload
        self.left = None
        self.right = None
        
def make_BST(items):
    def bst(items, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(items[mid])
        node.left = bst(items, start, mid-1)
        node.right = bst(items, mid+1, end)
        return node
    start, end = 0, len(items) - 1
    return bst(items, start, end)

if __name__ == '__main__':
    from tree import serialize_tree
    items = [1, 2, 4, 7, 9, 13, 18, 25, 27]
    print(f'Original list: {items}')
    bst = make_BST(items)
    print(f'Serialized BST: {serialize_tree(bst)}')
    