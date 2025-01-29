from tree import BinaryTree
            
def reverse_bt(tree):
    def reverse(node):
        if node is not None:
            node.left, node.right = node.right, node.left
            reverse(node.left)
            reverse(node.right)
    reverse(tree.root)


if __name__ == '__main__':
    t = BinaryTree([1, 2, 3, 4, 5, 6, 7])
    print(t)

    reverse_bt(t)
    print(t)

