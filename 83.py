# 1947

import sys
input = sys.stdin.readline

n = int(input())
mod = int(1e9)

d = [0] * 1000001
d[1] = 0
d[2] = 1

for i in range(3, n + 1):
    d[i] = ((i - 1) * (d[i - 2] + d[i - 1])) % mod

print(d[n])

# 문제 유형 기억 해두기(완전 순열) -> 자기 모자 못쓰는 문제와 같은 유형