# 2775

import sys
input = sys.stdin.readline

for tc in range(int(input())):

    k = int(input())    # 층
    n = int(input())    # 호

# 수가 많지 않으므로 모든 경우의수를 다 구하고 찾기
    d = [[0] * 15 for _ in range(15)]

    # dp 테이블 초기화
    for i in range(1, 15):
        d[i][1] = 1
        d[0][i] = i

    # 점화식에 따라 dp 테이블 갱신
    # d[i][j] = d[i - 1][1] + ... + d[i - 1][j -1] + d[i - 1][j]
    # d[i - 1][1] + ... + d[i - 1][j - 1] = d[i][j - 1]
    # 따라서, d[i][j] = d[i][j - 1] + d[i - 1][j]
    for i in range(1, 15):
        for j in range(2, 15):
            d[i][j] = d[i -1][j] + d[i][j - 1]

    print(d[k][n])

"""
t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력



마지막으로 반복문이 끝나면 k층 n호까지 사는 거주민들이 리스트에 담겨져있으니
마지막 인덱스를 출력하면 k층 n호에 사는데 필요한 거주민 수를 출력할 수 있다.

"""
