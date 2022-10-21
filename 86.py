# 2193

import sys
input = sys.stdin.readline

n = int(input())

d = [[0] * 2 for _ in range(n + 1)]
d[1][0] = 0
d[1][1] = 1


for i in range(2, n + 1):
    d[i][0] =  d[i - 1][0] + d[i - 1][1] 
    d[i][1] = d[i - 1][0]

print(d[n][0] + d[n][1])

# https://cijbest.tistory.com/17  (1차원 배열로 푸는법)