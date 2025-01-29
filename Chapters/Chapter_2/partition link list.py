'''
Question 2.4
Expanded also to quicksort a linked list (unstable inplace sort)

partitioning: O(n) time O(1) space (in place)
quicksort: typical case O(n log n) time
'''

from link_list import LinkList, Node
from sys import maxsize


def swap_nodes(node_1, node_2):
    '''
    Instead of resplicing links in the list, just swap the payloads
    '''
    node_1.data, node_2.data = node_2.data, node_1.data

def partition(head, tail):
    i = Node(-maxsize)
    i.next = head
    j = head
    while j != tail:
        if j.data < tail.data:
            i = i.next
            swap_nodes(i, j)
        j = j.next
    swap_nodes(i.next, tail)
    return i, i.next

def quicksort(head, tail):
    if head and head != tail:
        prev, pivot = partition(head, tail)
        if prev.data == -maxsize:
            quicksort(head, pivot)
            quicksort(pivot.next, tail)
        else:
            quicksort(head, prev)
            quicksort(pivot, tail)


def test():
    # generate an array of 100 random integers and sort the
    # array
    import random
    a = [random.randint(0, 100) for _ in range(100)]
    l = LinkList(a)
    print(f'{l}\n')

    quicksort(l.head, l.tail)
    print(l)

if __name__ == '__main__':
    test()



