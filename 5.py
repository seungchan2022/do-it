import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))     # 원래 리스트
s = [0] * n     # 합 배열
c = [0] * m     # 나머지가 같은 인덱스를 계산하는 리스트
answer = 0
s[0] = a[0]

for i in range(1, n):
    s[i] = s[i - 1] + a[i]

for i in range(n):
    data = s[i] % m
    if data == 0:
        answer += 1
    c[data] += 1

for i in range(m):
    # 나머지가 같은 것끼리 빼면 0이므로 나누어 떨어진다
    if c[i] > 1:
        answer += (c[i] * (c[i] - 1)) // 2

print(answer)

-----------------------------------------------------------------------------------------------

# 조합 

import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())

a = list(map(int, input().split()))
s = [0] * n     # 합 배열
c = [0] * m     # 나머지가 같은 인덱스를 계산하는 리스트(ex m=3이면 c의 원소는 0, 1, 2)
answer = 0
s[0] = a[0]

for i in range(1, n):
    s[i] = s[i - 1] + a[i]  # 합 배열 저장

for i in range(n):
    temp = s[i] % m
    if temp == 0:
        answer += 1
    c[temp] += 1

for i in range(m):
    if c[i] > 1:
        # c[i]의 값이 같은 것들 중에서 2개는 뽑는 경우
        answer += math.comb(c[i], 2)

print(answer)
