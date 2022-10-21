# 14425

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = set()

for i in range(n):
    s.add(input())

count = 0

for i in range(m):
    k = input()
    if k in s:
        count += 1

print(count)