INF = 99999

def floyd_warshall():
    n = int(input("Enter number of vertices: "))
    graph = []

    print("Enter the adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    # Floyd-Warshall Algorithm
    for k in range(n):
        print(f"\nUsing vertex {k} as intermediate:")
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

        print("Shortest distance matrix:")
        for i in range(n):
            for j in range(n):
                print(graph[i][j], end=" ")
            print()

floyd_warshall()
