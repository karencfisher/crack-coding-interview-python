from tree import BinaryTree


def flipBT(tree):
    que = [tree.root]
    while que:
        node = que.pop(0)
        node.left, node.right = node.right, node.left
        if node.left is not None:
            que.append(node.left)
        if node.right is not None:
            que.append(node.right)


t = BinaryTree([1, 2, 3, 4, 5, 6, 7])
print(t)

flipBT(t)
print(t)

