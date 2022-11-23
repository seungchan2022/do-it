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


----------------------------------------------

import sys
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

array.append(array[0])

result = 0
for i in range(n):
    # 0과 두점
    result += (array[i][0] * array[i + 1][1]) - (array[i + 1][0] * array[i][1])

print(round(abs(result/ 2), 1))

# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0
