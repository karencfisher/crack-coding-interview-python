class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, array):
        self.root = self.__make_tree(array)
    
    def __make_tree(self, array):
        if len(array) == 0:
            return None
        que = []
        root = Node(array[0])
        que.append(root)
        for i in range(1, len(array), 2):
            node = que.pop(0)
            if array[i] != None:
                node.left = Node(array[i])
                que.append(node.left)
            if array[i + 1] != None:
                node.right = Node(array[i + 1])
                que.append(node.right)
        return root

    def __str__(self):
        nodes = []
        que = [self.root]
        while len(que) > 0:
            row = []
            for _ in range(len(que)):
                node = que.pop(0)
                if node is not None:
                    row.append(str(node.value))
                    que.append(node.left)
                    que.append(node.right)
                else:
                    row.append(str(node))
            nodes.append(' '.join(row) + '\n')
        return ''.join(nodes)  
