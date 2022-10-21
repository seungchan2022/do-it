import sys
input = sys.stdin.readline

n = int(input())
mod = int(1e9)
d = [[0] * 10 for _ in range(101)]    # 10: 숫자 0 ~ 9

# 1자리 일때
for i in range(1, 10):
    d[1][i] = 1

# 2자리 이상
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][1]
        elif j == 9:
            d[i][j] = d[i - 1][8]
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

print(sum(d[n]) % mod)


"""
        각 자리수에서 맨 뒤에 올수 있는 숫자의 개수(0~9)

            0  1  2  3  4  5  6  7  8  9
자리수(1)   0  1  1  1  1  1  1  1  1  1
자리수(2)   1  1  2  2  2  2  2  2  2  1
자리수(3)   1  3  3  4  4  4  4  4  3  2


i = 자리수

j = 맨 뒤에 갈 수 있는 경우의 수.(0 ~ 9)

j = 0        dp[i][j] = dp[i - 1][1]

j = 1 ~ 8    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

j = 9        dp[i][j] = dp[i - 1][8]

"""