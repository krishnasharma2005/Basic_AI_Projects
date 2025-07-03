from collections import deque

# Hospital grid (0 = healthy, 1 = infected)
hospital = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
]

import numpy as np
from collections import deque

def virus_spread(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    healthy_count = 0

    # Identify initial infected cells and count healthy cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 0:
                healthy_count += 1

    # If there are no healthy people, return 0 time
    if healthy_count == 0:
        return 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    time_taken = 0

    # Perform BFS to spread the infection
    while queue:
        r, c, time = queue.popleft()
        time_taken = max(time_taken, time)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                grid[nr][nc] = 1  # Infect the cell
                queue.append((nr, nc, time + 1))
                healthy_count -= 1

    #Check if all cells are infected
    return time_taken if healthy_count == 0 else -1  # -1 means some cells remain uninfected

# Example Input (User-defined)
N, M = map(int, input("Enter grid dimensions (N M): ").split())
grid = []

print("Enter grid row-wise (0 for healthy, 1 for infected):")
for _ in range(N):
    grid.append(list(map(int, input().split())))

# Run the simulation
result = virus_spread(grid)

# Print Final Grid and Output
print("\nFinal Infected Grid:")
print(np.array(grid))

if result != -1:
    print("\nTime Taken for Complete Infection:", result)
else:
    print("\nSome cells could not be infected.")
