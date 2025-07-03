import heapq

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    def __lt__(self, other):
        return self.f < other.f #priority queue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) #Manhattan Distance function

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    closed_set = set()
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)
    came_from = {}
    while open_set:
        current = heapq.heappop(open_set)
        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        closed_set.add(current.position)
        for dx, dy in DIRECTIONS:
            neighbor_pos = (current.position[0] + dx, current.position[1] + dy)
            if not (0 <= neighbor_pos[0] < rows and 0 <= neighbor_pos[1] < cols):
                continue
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue
            if neighbor_pos in closed_set:
                continue
            # Create new node
            g_cost = current.g + 1
            h_cost = heuristic(neighbor_pos, goal)
            neighbor_node = Node(neighbor_pos, current, g_cost, h_cost)
            heapq.heappush(open_set, neighbor_node)
    return None

def print_grid(grid, path):
  #path = '*', walls = '#', empty space = '.'
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in path:
                print(" * ", end="")
            elif grid[i][j] == 1:
                print(" # ", end="")
            else:
                print(" . ", end="")
        print()

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

#empty grid
grid = [[0] * cols for _ in range(rows)]

num_obstacles = int(input("Enter number of obstacles: "))
print("Enter obstacle positions as 'row col': ")
for _ in range(num_obstacles):
    x, y = map(int, input().split())
    grid[x][y] = 1
start_x, start_y = map(int, input("Enter start position (row col): ").split())
goal_x, goal_y = map(int, input("Enter goal position (row col): ").split())

path = a_star_search(grid, (start_x, start_y), (goal_x, goal_y))

if path:
    print("\nShortest Path Found:")
    print_grid(grid, path)
    print("Path Steps:", path)
else:
    print("No path found!")
