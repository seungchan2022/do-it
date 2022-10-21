from collections import deque

a, b, c = map(int ,input().split())

q = deque()
q.append((0, 0))    # a, b의 양이 0일때부터 탐색

visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True    # 방문 처리

answer = []

# a 물통과 b 물통의 경우의수 저장
# 물의 총량은 C물통의 용량으로 정해져 있으므로 
# A물통에 담긴 물을 x, B물통에 담긴 물을 y, C물통에 담긴 물을 z라고 하면 z = c - x - y가 성립한다. 
# 따라서 x, y 두 변수만으로도 경우의 수를 표현할 수 있다.
def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():
    while q:
        # x: 현재 a 물통에 있는 물의 양, y: 현재 b 물통에 있는 물의 양, z: 현재 c 물통에 있는 물의 양
        x, y = q.popleft()
        z = c - x - y

        # a 물통이 비어있는 경우에 c 물통에 남아 있는 물의 양 저장
        if x == 0:
            answer.append(z)

        # 물이 이동할수 있는 모든 경우의수 탐색(그림 그리면서 풀기)
        
        # a -> b
        water = min(x, b - y)
        pour(x - water, y + water)
        # a -> c
        water = min(x, c - z)
        pour(x - water, y)

        # b -> a
        water = min(y, a - x)
        pour(x + water, y - water)
        # b -> c
        water = min(y, c - z)
        pour(x, y - water)

        # c -> a
        water = min(z, a - x)
        pour(x + water, y)
        # c -> b
        water = min(z, b - y)
        pour(x, y + water)

bfs()

answer.sort()
for i in answer:
    print(i, end=' ')