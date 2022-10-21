# 13251

import sys
input = sys.stdin.readline
import math

m = int(input())
array = list(map(int, input().split()))
k = int(input())

n = sum(array)  # 전체 조약돌 개수
total = math.comb(n, k) # 분모(전체에서 k개 선택) => nCk

count = 0   # 분자 변수
for i in array:
    count += math.comb(i, k)    # 5Ck + 6Ck + 7Ck

print(count / total)