def prims():
    n = int(input("Enter number of vertices: "))

    print("Enter adjacency matrix (0 if no edge):")
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    selected = [False] * n
    selected[0] = True

    print("\nEdge   Weight")
    for _ in range(n - 1):
        min_w = float('inf')
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < min_w:
                            min_w = graph[i][j]
                            x, y = i, j

        print(f"{x} - {y}    {graph[x][y]}")
        selected[y] = True

prims()
