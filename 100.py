# 2166

import sys
input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

array.append(array[0])

a = 0
b = 0

for i in range(len(array) - 1):
    a += array[i][0] * array[i + 1][1]
    b += array[i][1] * array[i + 1][0]

result = abs(a - b) / 2
print(round(result, 1))