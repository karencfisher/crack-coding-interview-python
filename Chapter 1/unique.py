'''
Question 1.1
'''

def unique(s):
    '''
    Utilizing added data structure (set)
    O(n) time, O(n) space
    '''
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

def unique2(s):
    '''
    O(1) space but O(n^2) time
    '''
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return False
    return True



a = 'aabc'
print(unique2(a))
