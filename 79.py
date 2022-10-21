# 1010

import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    
    # dp테이블 초기화
    d = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = 1
        d[i][1] = i
        d[i][i] = 1
        
    # 점화식에 따라 dp 테이블 갱신
    for i in range(2, m +1):
        for j in range(1, i):
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j]
            
    print(d[m][n])