n, m = map(int, input().split())
a = list(map(int, input().split()))
start = max(a)      # 시작 index
end = sum(a)        # 종료 index

while start <= end:
    mid = (start + end) // 2
    data = 0        # 레슨의 합     
    count = 0       # 블루레이 개수
    for i in range(n):
        if data + a[i] > mid:
            count += 1
            data = 0        # 새로운 블루레이로 교체
        data += a[i]

    if data != 0:   # 레슨합이 0이 아니면 마지막 블루레이가 필요하므로 count + 1 (이해 X)
        count += 1
    if count > m:   # mid 크기로 모두 저장 불가능 하면(오른쪽 데이터셋)
        start = mid + 1
    else:           # mid 크기로 모두 저장 가능 하면(왼쪽 데이터셋)
        end = mid - 1
    
print(start)

"""
블루레이의 크기가 모두 같고 녹화 순서가 바뀌지 않아야 한다 -> 이진 탐색

블루레이의 최소 크기: 9 => 만약, 9보다 작으면 모든 레슨을 담을수 없다.
블루레이의 최대 크기: sum(array) => 1개의 블루레이에 다 담을수 있다.

data와 count 변수가 while문 밖에 있으면 안되는 이유?
"""