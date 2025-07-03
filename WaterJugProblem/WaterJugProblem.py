from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])
    path = {}

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:
            solution = []
            while (x, y) in path:
                solution.append((x, y))
                x, y = path[(x, y)]
            solution.append((0, 0))
            solution.reverse()
            return solution

        if (x, y) in visited:
            continue
        visited.add((x, y))

        possible_states = [
            (jug1, y),   # Fill Jug1
            (x, jug2),   # Fill Jug2
            (0, y),      # Empty Jug1
            (x, 0),      # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Jug1 to Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Jug2 to Jug1
        ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)
                path[state] = (x, y)

    return "No solution found"

# Example: 4-liter and 3-liter jugs, target = 2 liters
jug1 = 4
jug2 = 3
target = 2

solution_path = water_jug_bfs(jug1, jug2, target)
print("Steps to solve the Water Jug Problem:")
for step in solution_path:
    print(step)
