from collections import defaultdict


#Depth First Search Algo
#https://favtutor.com/blogs/depth-first-search-python explains it well

#DFS Parameters (node, visited node, graph input)
def dfs(node, visited, graph):
    #redundancy check visted[node]
    visited[node] = True
    #for every v and direction in graph set [type will be dict]
    for v, direction in graph[node]:
        if not visited[v]:
            if direction == 0:
                direction = 1
            dfs(v, visited, graph)
            print(node, v, direction)

def main():
    #first input n and m are for intersections and streets, this input controls them
    n, m = map(int, input().split())

    # Create graph
    graph = defaultdict(list)
    two_way_streets = []


    #Optimzation oppurtunity, the code is specified to not care how many times the loop is run
    # but by using "_", we can say the code just needs to run an unspecified amount of times
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
