def bellman_ford():
    n = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))
    edges = []

    print("Enter edges (u v weight):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    src = int(input("Enter source vertex: "))

    dist = [9999] * n
    dist[src] = 0

    for i in range(n - 1):
        print("\nIteration", i + 1)
        for u, v, w in edges:
            if dist[u] != 9999 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

        print("Shortest distance from source:")
        for v in range(n):
            print("Vertex", v, "Distance =", dist[v])

bellman_ford()
