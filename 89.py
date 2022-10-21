# 13398

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [[0] * n for _ in range(2)]

dp[0][0] = array[0]  # 1개는 반드시 선택
dp[1][0] = array[0]

if n > 1:
    result = -int(1e9)
    for i in range(1, n):
        # 아무런 원소를 제거 하지 않았을때
        # max(이전까지의 연속합 + i번째 원소, i번째 원소)
        dp[0][i] = max(dp[0][i - 1] + array[i], array[i])
        # 특정 원소를 제거 하는 경우
        # max(i번째 원소를 제거하는 경우, i번째 이전에서 이미 특정 원소를 제거하여 i번째 원소를 더하는 경우)
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + array[i])
        
        # dpp 진행중 가장 큰 값으로 갱신
        result = max(result, dp[0][i], dp[1][i])
    print(result)

else:
    print(dp[0][0])


"""
dp : 연속합을 구하기 위한 누적합
dp[0][i]: 특정 원소를 제거하지 않은 경우
dp[1][i]: 특정 원소를 제거한 경우

if n > 1:
    1. dp[0][i] = max(dp[0][i - 1] + array[i], dp[i])
        -> 아무런 원소를 제거하지 않고 일반적인 연속합 구하는 경우
    2. dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + array[i])
        1) i번째 원소를 제거 하는 경우
            -> 위에서 구한 i - 1번째 연속 합의 최대값 그대로 대입
        2) i번째 이전의 원소를 이미 제거하여 이전에 구해놓은 dp값에 현재 i값을 더해 주는 경우
            -> i번째 이전의 원소를 제거한 연속합 값 + 현재 원소 i값

"""