import sys
from collections import Counter

n = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for i in range(n)]

# 산술평균
print(round(sum(number)/len(number)))

# 중앙값
number.sort()
def get_median(number) :
    idx = len(number) // 2
    if len(number) % 2 == 1:
        return number[idx]
    return (number(idx) + number(idx+1)) / 2

print(get_median(number))

# 최빈값
numberCount = Counter(number).most_common()
if len(numberCount) > 1 and numberCount[0][1] == numberCount[1][1] :
    print(numberCount[1][0])
else :
    print(numberCount[0][0])


# 범위
print(max(number) - min(number))