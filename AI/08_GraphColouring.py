class GraphColoring:
    def __init__(self, V):
        self.V = V
        self.adj = [[0 for _ in range(V)] for _ in range(V)]
        self.colors = [-1 for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u][v] = 1
        self.adj[v][u] = 1

    def is_safe(self, u, c):
        for v in range(self.V):
            if self.adj[u][v] == 1 and self.colors[v] == c:
                return False
        return True

    def graph_coloring_util(self, u):
        if u == self.V:
            return True

        for c in range(self.V):  # Max V colors
            if self.is_safe(u, c):
                self.colors[u] = c
                if self.graph_coloring_util(u + 1):
                    return True
                self.colors[u] = -1  # backtrack

        return False

    def graph_coloring(self):
        if self.graph_coloring_util(0):
            print("Solution exists with the following coloring:")
            for i in range(self.V):
                print(f"Vertex {i} -> Color {self.colors[i]}")
        else:
            print("Solution does not exist")

def main():
    V = int(input("Enter number of vertices: "))
    gc = GraphColoring(V)

    E = int(input("Enter number of edges: "))
    print("Enter edges (u v) where u and v are vertex indices:")
    for _ in range(E):
        u, v = map(int, input().split())
        gc.add_edge(u, v)

    gc.graph_coloring()

if __name__ == "__main__":
    main()