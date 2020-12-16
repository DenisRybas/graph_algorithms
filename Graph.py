graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

counter_dfs = 0


def iterative_dfs(graph, start, path=[]):
    global counter_dfs
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
            counter_dfs += 1
            path = path + [v]
            q = graph[v] + q
    return path


counter_bfs = 0


def iterative_bfs(graph, start, path=[]):
    global counter_bfs
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
            counter_bfs += 1
            path = path + [v]
            q = q + graph[v]
    return path


print(iterative_dfs(graph, 'A'))
print(counter_dfs)
print('-----------------')
print(iterative_bfs(graph, 'A'))
print(counter_bfs)
