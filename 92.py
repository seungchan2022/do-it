n, l, r = map(int, input().split())

mod = 1000000007

# dp[n][l][r]: 빌딩 n개를 왼쪽에서 l개, 오른쪽에서 r개가 보이도록 배치할 수 있는 모든 경우의 수
dp = [[[0 for k in range(r + 1)] for j in range(l + 1)] for i in range(n + 1)]
dp[1][1][1] = 1     # 건물이 1개일 때 배치될 경우의수

for i in range(2, n + 1):
    for j in range(1, l + 1):
        for k in range(1, r + 1):
            # 가장 작은 빌딩을 왼쪽에 놓는 경우 + 오른쪽 + 사이(n - 2(양끝))
            dp[i][j][k] = (dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] + dp[i - 1][j][k] * (i - 2)) % mod

print(dp[n][l][r])


"""
3차원 배열 생성하기

3d_array = [[[0 for _ in range(column)] for _ in range(row)] for _ in range(level)]
2~3중 반복문을 선언함에 따라서 'range'의 파라미터는 열(컬럼) → 행(로우) → 층(레벨)의 순서로 선언하면 되며, 최초 초기화할 값 (0, None... 등)에 따라 선언이 완료된다.
"""