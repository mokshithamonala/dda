def kruskal():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    edges = []
    print("Enter edges (u v weight):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    sets = [{i} for i in range(n)]

    print("\nEdge   Weight")
    for w, u, v in edges:
        set_u = set_v = None

        for s in sets:
            if u in s:
                set_u = s
            if v in s:
                set_v = s

        if set_u != set_v:
            print(f"{u} - {v}    {w}")
            sets.remove(set_u)
            sets.remove(set_v)
            sets.append(set_u.union(set_v))

kruskal()
