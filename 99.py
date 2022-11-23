# 2162

import sys
input = sys.stdin.readline

# CCW 함수
def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    return 0

# 선분 겹침 여부 판별 함수(두 선분이 일직선에 있을때 판별 방법)
def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        return True
    return False

# 선분 교차 판별 함수
def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = ccw(x1, y1, x2, y2, x3, y3)
    abd = ccw(x1, y1, x2, y2, x4, y4)
    cda = ccw(x3, y3, x4, y4, x1, y1)
    cdb = ccw(x3, y3, x4, y4, x2, y2)
    if abc * abd == 0 and cda * cdb == 0:   # 두 선분이 일직선인 경우
        return check(x1, y1, x2, y2, x3, y3, x4, y4)   # 겹치는 선분인지 판별
    elif abc * abd <= 0 and cda * cdb <= 0:     # CCW 결괏값의 곱이 모두 양수가 아닌 경우
        return True                             # 교차한다
    return False

def find(parent, x):
    if parent[x] < 0:   # 음수이면
        return x        # 자기 자신이 부모 노드
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:      # 이미 연결되어 있음
        return
    if a > b:
        # a의 부모 노드에 b가 속한 선분 그룹의 선분 개수를 더하기(음수 절댓값으로 개수 표현)
        parent[a] += parent[b]
        parent[b] = a   # a를 b의 부모 노드로 지정
    else:
        parent[b] += parent[a]
        parent[a] = b

n = int(input())
parent = [-1] * (n + 1) # 선분들의 부모 선분 저장 리스트(-1로 초기화)

array = []      # 선분 저장 리스트

for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(i):
        # 신규 선분과 현재까지 저장된 선분이 교차되는지 확인
        if cross(array[i][0], array[i][1], array[i][2], array[i][3], array[j][0], array[j][1], array[j][2], array[j][3]):
            # 선분이 교차할 때 두 선분은 1개의 그룹으로 지정
            union(parent, i, j)

ans = 0     # 선분 그룹 수
res = 0     # 가장 큰 선분 그룹의 선분 수를 음수로 저장하는 변수

for i in range(n):
    if parent[i] < 0:   # 음수인 parent[i]는 선분 그룹의 부모 노드
        ans += 1
        res = min(res, parent[i])   # 음수의 절댓값이 선분 그룹의 선분 개수(parent[i]의 값 중 가장 작은 수를 저장)

print(ans)
print(-res)
