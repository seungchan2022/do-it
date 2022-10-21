# 14501

import sys
input = sys.stdin.readline

n = int(input())
t = [0] * (n + 1)   # 각 상담을 완료하는데 걸리는 시간
p = [0] * (n + 1)   # 각 상담을 완료했을때 받을 수 있는 금액
# d[i] = i번째 날 부터 퇴사일 까지 벌 수 있는 최대 수입
d = [0] * (n + 2)   # n + 1 일때 dp테이블을 구해야 하므로 n + 2로 설정

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):   # 리스트 뒤에서 부터 확인
    # 오늘 시작되는 상담을 했을 때 퇴사일 까지 끝나지 않는 경우
    # i + t[i]: i번째 상담일 + i번째 상담을 완료하는데 걸리는 시간
    if i + t[i] > n + 1:
        d[i] = d[i + 1]
    
    # 오늘 시작되는 상담을 했을 때 퇴사일 안에 끝나는 경우
    else:
        # i번째 상담이 끝난 다음부터 퇴사일 까지 최대 수입 + i번째 상담 비용
        d[i] = max(d[i + 1], d[i + t[i]] + p[i])

# 1일부터 퇴사일 까지 벌 수 있는 최대 비용
print(d[1])