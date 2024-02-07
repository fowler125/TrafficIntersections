from collections import defaultdict

def dfs(u, visited, graph, output):
    visited[u] = True
    for v, direction in graph[u]:
        if not visited[v]:
            if direction == 0:
                direction = 1
            output.append((u, v, direction))
            dfs(v, visited, graph, output)

def main():
    n, m = map(int, input().split())

    # Create graph
    graph = defaultdict(list)
    two_way_streets = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        if c == 1:
            graph[a].append((b, 1))
        else:
            two_way_streets.append((a, b))
            graph[a].append((b, 0))
            graph[b].append((a, 0))

    # Initialize visited array
    visited = [False] * (n + 1)

    # Perform DFS to determine traffic directions
    output = []
    for u in range(1, n + 1):
        if not visited[u]:
            dfs(u, visited, graph, output)

    # Output directions for two-way streets
    for street in two_way_streets:
        a, b = street
        direction = 2
        for u, v, d in output:
            if (u == a and v == b) or (u == b and v == a):
                direction = d
                break
        print(a, b, direction)

if __name__ == "__main__":
    main()
