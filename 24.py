# 2023

import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

n = int(input())

# 소수 구하는 함수
def prime(a):
    for i in range(2, int(a / 2 + 1)):
        if a % i == 0:
            return False
    return True

def dfs(k):
    if len(str(k)) == n:
        print(k)
    else:   # n자리 까지 재귀함수 형태로 탐색
        for i in range(1, 10):
            if i % 2 == 0:  # 짝수이면
                continue    # 탐색 불필요
            if prime(k * 10 + i):   # 소수이면
                dfs(k * 10 + i)     # 자릿수 늘림

dfs(2)
dfs(3)
dfs(5)
dfs(7)