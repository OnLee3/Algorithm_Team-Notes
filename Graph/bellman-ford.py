INF = int(1e9)

n, m = map(int, input().split())

graph = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))


def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            start_node = graph[j][0]
            next_node = graph[j][1]
            next_cost = graph[j][2]
            if distance[start_node] != INF and distance[next_node] > distance[start_node] + next_cost:
                distance[next_node] = distance[start_node] + next_cost
                if i == n-1:  # 음수 사이클 판별
                    return True
    return False


if bf(1):
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
