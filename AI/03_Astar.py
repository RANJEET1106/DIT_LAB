import heapq

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def is_valid(r, c, rows, cols, grid):
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0

def print_path(parents, end):
    path = []
    while end:
        path.append(end)
        end = parents.get(end)
    path.reverse()
    print("Path found:")
    for r, c in path:
        print(f"({r},{c})", end=" ")
    print()

def a_star(grid, start, goal, rows, cols):
    sr, sc = start
    gr, gc = goal

    open_set = []
    heapq.heappush(open_set, (0, 0, (sr, sc)))  # (f, g, (row, col))
    visited = [[False]*cols for _ in range(rows)]
    parents = {}

    while open_set:
        f, g, (r, c) = heapq.heappop(open_set)

        if visited[r][c]:
            continue
        visited[r][c] = True

        if (r, c) == (gr, gc):
            print_path(parents, (r, c))
            return

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, grid) and not visited[nr][nc]:
                new_g = g + 1
                h = heuristic(nr, nc, gr, gc)
                heapq.heappush(open_set, (new_g + h, new_g, (nr, nc)))
                if (nr, nc) not in parents:
                    parents[(nr, nc)] = (r, c)

    print("No path found.")

# Input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter grid (0 = empty, 1 = obstacle):")
grid = [list(map(int, input().split())) for _ in range(rows)]

sr, sc = map(int, input("Enter start (row col): ").split())
gr, gc = map(int, input("Enter goal (row col): ").split())

if not is_valid(sr, sc, rows, cols, grid) or not is_valid(gr, gc, rows, cols, grid):
    print("Invalid start or goal.")
else:
    a_star(grid, (sr, sc), (gr, gc), rows, cols)
