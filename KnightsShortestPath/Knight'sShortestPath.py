from collections import deque

def in_boundaries(x, y, N):
    return 0 <= x < N and 0 <= y < N

def knight_shortest_path(N, start, target):

    queue = deque([(start[0], start[1], 0, [start])])
    visited = set()
    visited.add(start)

    while queue:
        x, y, moves_count, path = queue.popleft()

        if (x, y) == target:
            print(f"Minimum moves required: {moves_count}")
            print("Path followed:")
            for step in path:
                print(step)
            return path

        # Try all 8 possible knight moves
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if in_boundaries(new_x, new_y, N) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, moves_count + 1, path + [(new_x, new_y)]))

    return "Target not reachable"

# Taking user input
N = int(input("Enter board size (N x N): "))
x1, y1 = map(int, input("Enter knight's starting position (x y): ").split())
x2, y2 = map(int, input("Enter target position (x y): ").split())

# Running the function
knight_shortest_path(N, (x1, y1), (x2, y2))
