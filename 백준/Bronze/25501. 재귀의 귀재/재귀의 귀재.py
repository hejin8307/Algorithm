import sys

n = int(sys.stdin.readline())
words = [str(sys.stdin.readline().strip()) for i in range(n)]

def recursion(s, l, r):
    global c
    c += 1
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in words:
    c = 0
    print(isPalindrome(i), c)