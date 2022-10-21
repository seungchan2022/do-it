# 1456

import math

a, b = map(int, input().split())

# 소수가 아닌 수를 0으로 표현
array = [0] * (10000001)

for i in range(2, len(array)):
    array[i] = i

for i in range(2, int(math.sqrt(len(array)) + 1)):
    if array[i] == 0:
        continue
    for j in range(i + i, len(array), i):    # 배수 지우기
        array[j] = 0

count = 0

for i in range(2, b + 1):
    if array[i] != 0:
        temp = array[i]
        # n제곱한 값이 변수 표현 점위를 넘을 수 있어 이항정리로 해결
        while array[i] <= b / temp:     # => array[i] * array[i] <= b
            if array[i] >= a / temp:    # => array[i] * array[i] >= a
                count += 1
            temp *= array[i]

print(count)




"""
import math
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

array = [True for _ in range(int(math.sqrt(b) + 1))]
array[1] = False    # 1은 소수 X

for i in range(2, int(math.sqrt(b) + 1)):
    if i * i > b:
        break
    if not array[i]:    # 소수가 아니면 무시
        continue
    for j in range(i * i, int(math.sqrt(b) + 1)):
        array[j] = False        # 소수가 아니라는 것을 표시

count = 0

for i in range(1, len(array)):
    if array[i]:
        j = i * i       # j를 2i가 아닌 i*i부터 시작
        while True:
            if j < a:
                j *= i
                continue
            if j > b:
                break
            j *= i
            count += 1

print(count)
"""