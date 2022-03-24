from collections import deque

# 2차원배열 상하좌우 탐색
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
move_type = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + move_type[i][0]
            ny = y + move_type[i][1]
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


# 그래프 간선 탐색
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque(start)
    while q:
        v = q.popleft()
        for j in graph[v]:
            if not visited[j]:
                q.append(j)
                visited[j] = True
