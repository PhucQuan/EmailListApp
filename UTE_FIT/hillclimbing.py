import random

goal_state = [[0,1,2],
              [5,4,3],
              [6,7,8]]

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

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

def hill_climbing(start, max_steps=1000):
    current = start
    current_h = misplaced_tiles(current)

    for step in range(max_steps):
        if current == goal_state:
            print(f"Goal reached in {step} steps!")
            return current, True

        neighbors = get_neighbors(current)
        if not neighbors:
            break

        # chọn neighbor ngẫu nhiên trong số những cái tốt hơn
        better_neighbors = [n for n in neighbors if misplaced_tiles(n) < current_h]
        if better_neighbors:
            current = random.choice(better_neighbors)
            current_h = misplaced_tiles(current)
        else:
            return current, False  # kẹt

    return current, False

def random_restart(start, restarts=10):
    for i in range(restarts):
        print(f"Attempt {i+1}:")
        result, success = hill_climbing(start)
        for row in result:
            print(row)
        print("----")
        if success:
            print("Solved with hill climbing + random restart!")
            return
    print("Failed after all restarts!")

# Start state
start_state = [[2,3,7],
               [1,6,8],
               [0,5,4]]

random_restart(start_state, restarts=5)
