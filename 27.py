from collections import deque

n, m = map(int, input().split())    # N x M 크기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 0인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 
    return graph[n - 1][m - 1]

print(bfs(0, 0))