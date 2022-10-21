import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
array = list(map(int, input().split()))
count = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if array[i] + array[j] == m:
            count += 1

print(count)


"""
8 ~ 12

array.sort()
i = 0
j = n - 1

while i < j:
    if array[i] + array[j] < m:
        i += 1
    elif array[i] + array[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
"""