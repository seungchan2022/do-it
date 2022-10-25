from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
array = list(map(int, input().split()))
q = deque()

for i in range(n):
    # 큐의 마지막 위치에서부터 들어오느값(현재 값)보다 큰 값은 큐에서 제거
    while q and q[-1][1] > array[i]:    # 들어갈 숫자보다 큰 것들은 전부 pop
        q.pop()     # 큐의 마지막 원소들을 제거하므로 popleft (X)

    q.append((i, array[i]))     # 큐의 마지막 위치에 현재 값 저장((인덱스, 값))

    # 큐의 1번째 위치에서부터 L의 범위를 벗어난 값 (array index-L <= index)을 큐에서 제거
    while q and q[0][0] <= i -l: # i - L + 1 인덱스 이전인 것들을 pop
        q.popleft()

    print(q[0][1], end=' ')
