from collections import defaultdict


#Depth First Search Algo
#https://favtutor.com/blogs/depth-first-search-python explains it well

def dfs(u, visited, graph):
    visited[u] = True
    for v, direction in graph[u]:
        if not visited[v]:
            if direction == 0:
                direction = 1
            dfs(v, visited, graph)
            print(u, v, direction)

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
    for u in range(1, n + 1):
        if not visited[u]:
            dfs(u, visited, graph)

if __name__ == "__main__":
    main()
