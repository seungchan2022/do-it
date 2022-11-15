# 14501

n = int(input())
t = []      # 각 상담을 완료하는데 걸리는 시간
p = []      # 각 상담을 완료했을때 받을 수 있는 금액
# dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 금액
dp = [0] * (n + 1)  # 1차원 dp 테이블 초기화
max_value = 0   # 뒤에서 부터 계산할때, 현재까지의 최대 상담 금액

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트 뒤에서 부터 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i     # 상담이 기간안에 끝나는지 확인하는 변수 ex) 6일에 4일짜리 상담이면 10일째부터 새로운 상담 가능
    # 상담이 기간안에 끝나는 경우
    if time <= n:
        # i일에 상담을 하게 되면 얻는 금액 + i일에 하는 상담에 소요되는 time 이후의 날짜로부터 얻는 최대 금액
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어난 경우
    else:
        dp[i] = max_value

print(max_value)

"""
1일 차에 상담을 진행하면 3일에 걸쳐 4일부터 다시 상담 가능
그러므로 1일차에 상담을 진행하면 최대이익:1일차 상담금액 + 4일부터의 최대 상담 금액
즉, 뒤쪽부터 매 상담에 대해 '현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤(dp[t[i] + i])'
dp[i] = i번째 날부터 마지막 날까지 낼수 있는 최대 이익
dp[i] = max(p[i] + dp[t[i] +i], max_value), max_value: 뒤에서부터 계산할때, 현재 까지의 최대 상담 금액
"""
