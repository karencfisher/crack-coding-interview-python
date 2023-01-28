'''
Question 2.5

O(n) time, O(n) space (creates new list for sum)
'''
from link_list import LinkList, Node


def sum_lists(l1, l2):
    n1, n2 = l1.head, l2.head
    new_l = None
    carry = 0
    while n1 or n2:
        summ = carry
        if n1:
            summ += n1.data
            n1 = n1.next
        if n2:
            summ += n2.data
            n2 = n2.next

        carry = summ // 10
        if new_l is None:
            new_l = LinkList([summ % 10])
        else:
            new_l + Node(summ % 10)
               
    if carry > 0:
        new_l + Node(carry)
    return new_l


def tests():
    l1 = LinkList([7, 1, 6])
    l2 = LinkList([5, 9, 2])
    print(f'{l1} + {l2}')
    l3 = sum_lists(l1, l2)
    print(l3)

    l1 = LinkList([7, 1, 6])
    l2 = LinkList([5, 9, 2, 3])
    print(f'{l1} + {l2}')
    l3 = sum_lists(l1, l2)
    print(l3)

    l1 = LinkList([7, 1, 6, 8])
    l2 = LinkList([5, 9, 2])
    print(f'{l1} + {l2}')
    l3 = sum_lists(l1, l2)
    print(l3)

    # check carry, should be 2->1->2->0->1
    l1 = LinkList([7, 1, 6, 9])
    l2 = LinkList([5, 9, 5])
    print(f'{l1} + {l2}')
    l3 = sum_lists(l1, l2)
    print(l3)

    # empty lists, result should be None
    l1 = LinkList([])
    l2 = LinkList([])
    print(f'{l1} + {l2}')
    l3 = sum_lists(l1, l2)
    print(l3)

if __name__ == '__main__':
    tests()
