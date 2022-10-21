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