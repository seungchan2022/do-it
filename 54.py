# 1516

from collections import deque

n = int(input())
indegree = [0] * (n+1)
time = [0] * (n+1)  # 건물 짓는데 걸리는 시간 리스트
graph = [[] for _ in range(n+1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    # 각 건물 짓는데 걸리는 시간 기록
    time[i] = data[0]
    # 그래프 데이터 입력
    for x in data[1:-1]:
        graph[x].append(i)  # 선수과목이 x이므로 x -> i
        indegree[i] += 1    # 진입차수는 들어오는 노드 입장이므로 i


def topology_sort():
    result = [0] * (n + 1)    # 결과 리스트
    q = deque()
    # 초기에 진입차수 0인 노드들 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        # 큐에서 꺼낸 노드 번호에 해당하는 건물을 짓는데 걸리는 시간 저장
        # 선수 건물 짓는데 걸리는 시간이 포함 되어 있음
        # 즉. '선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간'이 저장됨
        result[now] += time[now]
        for i in graph[now]:
            indegree[i] -= 1
            # i번호 건물을 짓기 전에 먼저 지어야 하는 선수 건물 짓는데 걸리는 시간으로 갱신
            result[i] = max(result[i], result[now])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()