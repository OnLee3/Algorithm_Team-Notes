def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if not(visited[y]):
            dfs(y)
