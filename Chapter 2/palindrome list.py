'''
Question 2.6

Uses stack to keep track of items. Up to first half of the
list, just push items on to the stack; on second half 
(skipping mid item if odd length) pop top item off stack.
If stack empty or item mismatches, return False.

At completion stack should be empty, or return False.

O(n*m) time (m is number of characters), O(n) space 
(due to implementing stack).
'''
from link_list import LinkList


def is_list_palindrome(l):
    m = l.length // 2
    odd = l.length % 2 != 0
    stack = []
    node = l.head
    count = 0
    while node:
        count += 1
        chars = list(str(node.data))
        if count <= m:
            stack += chars
        elif not(count == m + 1 and odd):
            for c in chars:
                x = stack.pop()
                if x != c:
                    return False
        node = node.next
    return len(stack) == 0


def tests():
    # palindrome
    a = ['i', 'am', 'a', 'ma', 'i']
    l = LinkList(a)
    print(is_list_palindrome(l))

    # not palindrome
    a = ['i', 'am', 'a', 'am', 'i']
    l = LinkList(a)
    print(is_list_palindrome(l))

    # palindrome
    a = [12, 22, 21]
    l = LinkList(a)
    print(is_list_palindrome(l))

    # not palindrome
    a = [12, 22, 12]
    l = LinkList(a)
    print(is_list_palindrome(l))

    # palindrome
    a = ['a', 'q', 'b', 'b', 'q', 'a']
    l = LinkList(a)
    print(is_list_palindrome(l))

    # not palindrome
    a = ['a', 'q', 'a', 'b', 'q', 'a']
    l = LinkList(a)
    print(is_list_palindrome(l))

    # not palindrome
    a = ['a', 'q', 'b', 'q', 'b', 'a']
    l = LinkList(a)
    print(is_list_palindrome(l))

    # not palindrome
    a = ['x', 'a', 'q', 'b', 'b', 'q', 'a']
    l = LinkList(a)
    print(is_list_palindrome(l))

    # palindrome
    a = ['x', 'a', 'x', 'a', 'x', 'a', 'x']
    l = LinkList(a)
    print(is_list_palindrome(l))

    a = ['a', 'b', 'a']
    l = LinkList(a)
    print(is_list_palindrome(l))

    a = ['a', 'a', 'b']
    l = LinkList(a)
    print(is_list_palindrome(l))

    a = ['a']
    l = LinkList(a)
    print(is_list_palindrome(l))

    a = []
    l = LinkList(a)
    print(is_list_palindrome(l))

if __name__ == '__main__':
    tests()
