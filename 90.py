# 9252

import sys
sys.setrecursionlimit(1000)

a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        # 행과 열의 문자가 같으면
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(a)][len(b)])

result = []
# LCS 구현 함수
def lcs(r, c):
    if r == 0 or c == 0:    # LCS 길이가 0이면
        return
    # 맨 마지막 부터 탐색 하면서 문자열이 같으면 해당 문자 저장후 왼쪽 위로 이동
    if a[r - 1] == b[c - 1]:
        result.append(a[r - 1])
        lcs(r - 1, c - 1)
    # 다르면 max(왼, 위)이동
    else:
        if dp[r - 1][c] > dp[r][c - 1]:     # 위
            lcs(r - 1, c)   
        else:   # 왼
            lcs(r, c - 1)

# 문자열 생성
lcs(len(a), len(b))

result.reverse()
for i in result:
    print(i, end='')
