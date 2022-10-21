# 17472

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())

land = []   # 땅인 부분
array = []

for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(m):
        if array[i][j] == 1:
            land.append((i, j))

def find_land(visited, a, b, num):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == 1:
                visited[nx][ny] = True
                array[nx][ny] = num
                start.append((nx, ny, num))
                q.append((nx, ny))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 바다이면 temp에 다리의 길이를 넣어주고 dfs, 땅이고 길이가 2이상이면 bridge에 append
def make_straight(nx, ny, dx, dy, num, temp):
    global result 
    nx += dx
    ny += dy
    if  0 <= nx < n and 0 <= ny < m:
        if array[nx][ny] == 0:
            temp[nx][ny] = temp[nx - dx][ny - dy] + 1
            make_straight(nx, ny, dx, dy, num, temp)
        elif temp[nx - dx][ny - dy] >= 2:
            bridge.append((temp[nx - dx][ny - dy], num, array[nx][ny]))

# start의 값을 가지고 dfs(make_straight)로 다리를 이을 수 있는지 체크
def make_bridge():
    for x, y, num in start:
        temp = [[0] * m for _ in range(n)]
        for dx, dy in direction:
            make_straight(x, y, dx, dy, num, temp)

def check_all_connected():
    temp = 0
    for i in range(1, num_island + 1):
        if i == 1:
            temp = find_parent(parent, i)
        elif temp != find_parent(parent, i):
            return False
    return True

start = []
visited = [[False] * m for _ in range(n)]
num_island = 1      # 구역의 개수
# 각 땅을 돌면서 bfs(find_land)로 연결된 땅에 구역 번호를 매겨준다
for i, j in land:
    if not visited[i][j]:
        visited[i][j] = True
        array[i][j] = num_island
        start.append((i, j, num_island))    # (x좌표, y좌표, 구역 번호)
        find_land(visited, i, j, num_island)
        num_island += 1
num_island -= 1

direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]
# 구역의 부모리스트 자기 자신으로 설정
parent = [i for i in range(num_island + 1)]

bridge = []     # 연결할 수 있는 다리의 정보(다리의 길이, 시작구역 번호, 도착구역 번호)
make_bridge()
bridge.sort()   # 다리길이가 짧은 순서로 정렬

result = 0
for len, start, end in bridge:
    # 각 구역의 부모가 다르면
    if find_parent(parent, start) != find_parent(parent, end):
        result += len
        union_parent(parent, start, end)

# 모든 구역의 부모가 같은지 확인
if check_all_connected():
    print(result)
else:
    print(-1)