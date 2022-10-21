# 2042

import sys
input = sys.stdin.readline

# 데이터 개수(n), 수의 변경횟수(m), 구간합 구하는 횟수(k)
n, m, k = map(int, input().split())

arr = [0] * (n + 1)
tree = [0] * (n + 1)

# i번째 수 까지의 누적합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result

# i번째 수를 dif(특정값)만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

# start부터 end까지의 구간합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    # 부분 수열 업데이트
    update(i, x)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))



"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
treeHeight = 0      # 트리의 높이
length = n          # 리프 노드의 개수

# 리프 노드의 개수를 2씩 나누어 가면서 높이 계산
while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1  # 리프 노드 시작인덱스
tree = [0] * (treeSize + 1)

# 데이터를 리프노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

# 인덱스 트리 생성함수
def setTree(i):
    while i != 1:   # 인덱스가 루트가 아닐 때 까지
        # 부모노드(인덱스 / 2)에 현재 index의 트리값 더하기
        tree[i // 2] += tree[i]
        i -= 1

setTree(treeSize - 1)   # 초기 트리 생성

# 값 변경 함수
def changeVal(index, value):    # (시작 인덱스, 변경값)
    diff = value - tree[index]  # 변경된 값
    while index > 0:
        tree[index] += diff
        index //= 2

# 구간 합 계산 함수
def getSum(s, e):       # (시작 인덱스, 종료 인덱스)
    partSum = 0     # 구간 합
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return partSum

for _ in range(m + k):
    q, s, e = map(int, input().split())
    if q == 1:
        changeVal(leftNodeStartIndex + s, e)    # (tree에서 시작 인덱스, 변경 값)
    elif q == 2:
        s += leftNodeStartIndex     # tree에서 시작 인덱스
        e += leftNodeStartIndex     # tree에서 종료 인덱스
        print(getSum(s, e))

"""