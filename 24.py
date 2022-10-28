# 2023

# dfs를 이용해 소수 판별

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
import math

n = int(input())

# 소수 판별 함수
def prime(x):
    # 2부터 제곱근 까지만 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:      # x가 해당 수로 나누어 떨어지면
            return False    # 소수 X
    return True

def dfs(v):
    if len(str(v)) == n:        # 해당 자릿수 이면
        print(v)
    else:       # n자리 까지 재귀함수 형태로 검색
        # 뒤에 붙는 수 계산
        for i in range(10):
            if i % 2 == 0:      # 짝수라면
                continue        # 더이상 탐색 불필요
            # 뒤에 붙힌 새로운 수가 홀수 이면서 소수일때
            if prime(v * 10 + i):   # 소수이면 자릿수 늘림(먼저 늘려서 확인해주고 맞으면 dfs 실행)
                dfs(v * 10 + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)


"""
자릿수가 한 개인 소수는 2, 3, 5, 7이므로 이 수부터 탐색 시작.
이어서 자릿수가 두 개인 수는 현재수 * 10 + a를 계산 하여 소수인지 판단하고,
소수라면 재귀함수로 자릿수를 하나씩 늘린다.
"""
