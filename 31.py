n = int(input())
k = int(input())

start = 1       # 시작 index(배열 a, b는 index 1부터 시작)
end = k         # 종료 index
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0       # mid 보다 작은수의 개수
    for i in range(1, n + 1):
        # mid를 i로 나눈 값과 n 중에서 작은 값  +
        count += min(mid // i, n)
    if count < k:   # 현재 mid보다 작은 수의 개수가 k보다 작음
        start = mid + 1
    else:           # 현재 mid보다 작은 수의 개수가 k보다 크거나 같음
        end = mid - 1
        answer = mid

print(answer)

"""
2차원 리스트: N행이 N의 배수이므로 K번째 수는 K를 넘지 않음 
    => 1 ~ k 번째 안에 정답
중앙값 보다 작거나 같은 수의 개수: 중앙값 // i(행의 인덱스) (단, N보다 크면 N)
    => min(mid // i, N)

따라서, mid보다 작은 수의 개수가 K보다 작으면 start = mid - 1
        mid보다 작은 수의 개수가 K보다 크거나 같으면 end = mid + 1 하면서 정답을 중앙값으로 갱신하면서 이진 탐색 진행
"""