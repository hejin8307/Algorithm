import sys

n = int(sys.stdin.readline())
words = [str(sys.stdin.readline().strip()) for i in range(n)]

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)
