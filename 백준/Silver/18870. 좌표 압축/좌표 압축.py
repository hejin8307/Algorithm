import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
number_sort = list(sorted(set(number)))

idx = {number_sort[i] : i for i in range(len(number_sort))}

for i in number :
    print(idx[i], end=' ')

