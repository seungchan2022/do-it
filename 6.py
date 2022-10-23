# 특정한 합을 가지는 부분 연속 수열 찾기

n = int(input())      # 찾고자 하는 부분합

# 1 ~ n까지 원소를 가지는 배열 만들고 투포인터 알골리즘 수행
data = [i for i in range(1, n + 1)]

count = 0       # 부분합의 개수
interval_sum = 0   # 부분합
end = 0     # 끝점

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < n and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == n:
        count += 1
    # 부분합이 m보다 크거나 같으면 start를 1 증가시키기 때문에 이전 start값을 빼주어야 한다.
    interval_sum -= data[start]

print(count)
----------------------------------------------------------------------------------------------
n = int(input())

count = 1   # 자기 자신은 1가지 경우가 무조건 나오므로 1로 설정
start = 1    
end = 1
sum = 1

while end != n:
    if sum == n:
        count += 1
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(count)

"""
투 포인터 알고리즘

업데이트 하는 순서 주의
if sum == n: 경우의 수 증가, end 증가, sum 갱신
elif sum > n: sum 갱신, start증가
else: end 증가, sum 갱신
"""
