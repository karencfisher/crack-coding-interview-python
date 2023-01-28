'''
Question 4.5

Validate a Binary Search Tree
'''

from tree import BinaryTree


def validateBST(node, minimum=float('-INF'), maximum=float('INF')):
    if node is None:
        return True
    if not minimum <= node.value < maximum:
        return False
    result_l = validateBST(node.left, minimum, node.value)
    result_r = validateBST(node.right, node.value, maximum)
    return result_l and result_r


a = [10, 5, 15, 4, 5, 14, 16]
t = BinaryTree(a)
print(t)

print(validateBST(t.root))
