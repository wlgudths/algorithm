from collections import deque

def bfs(graph, start, n):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)

    return sum(visited[1:])

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
counter = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    counter[i] = bfs(graph, i, n)

min_value = min(counter[1:])
ans = counter.index(min_value)

print(ans)