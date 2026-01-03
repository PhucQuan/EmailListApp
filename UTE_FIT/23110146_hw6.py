import heapq

# Trạng thái goal
goal_state = [[1, 2, 3],
              [7, 4, 0],
              [8, 5, 6]]

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def find_pos(value, state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return (i,j)

# Heuristic: Manhattan Distance
def manhattan_distance(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = find_pos(value, goal_state)
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Hàm giải tổng quát: mode = "astar" hoặc "gbfs"
def solve_puzzle(start, mode="astar"):
    pq = []
    g = {to_tuple(start): 0}
    came_from = {}

    # Tính f ban đầu
    if mode == "astar":
        f = manhattan_distance(start) + g[to_tuple(start)]
    else: # greedy best first search
        f = manhattan_distance(start)

    heapq.heappush(pq, (f, start))

    visited = set()

    while pq:
        _, current = heapq.heappop(pq)
        if current == goal_state:
            # reconstruct path
            path = []
            state = to_tuple(current)
            while state in came_from:
                path.append(state)
                state = came_from[state]
            path.append(to_tuple(start))
            return path[::-1]

        visited.add(to_tuple(current))

        for neighbor in get_neighbors(current):
            neighbor_tuple = to_tuple(neighbor)
            tentative_g = g[to_tuple(current)] + 1

            if neighbor_tuple not in visited:
                g[neighbor_tuple] = tentative_g

                if mode == "astar":
                    f = tentative_g + manhattan_distance(neighbor)
                else: # greedy
                    f = manhattan_distance(neighbor)

                heapq.heappush(pq, (f, neighbor))
                came_from[neighbor_tuple] = to_tuple(current)

    return None


# Start state
start_state = [[2,3,7],
               [1,4,5],
               [8,0,6]]

# Giải bằng cả 2 phương pháp
solution_astar = solve_puzzle(start_state, mode="astar")
solution_gbfs  = solve_puzzle(start_state, mode="gbfs")

print("=== A* Search Solution ===")
for step in solution_astar:
    for row in step:
        print(row)
    print("------")

print("\n=== Greedy Best-First Search Solution ===")
for step in solution_gbfs:
    for row in step:
        print(row)
    print("------")
