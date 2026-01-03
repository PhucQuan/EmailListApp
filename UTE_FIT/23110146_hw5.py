import heapq
from collections import deque
import sys

# Trạng thái xuất phát và đích
start = (1,2,3,
         0,8,7,
         6,4,5)

goal  = (1,2,3,
         7,4,0,
         8,5,6)

# Các hướng đi
MOVES = [('U',-1,0), ('D',1,0), ('L',0,-1), ('R',0,1)]

def pretty(state):
    """In trạng thái 8-puzzle"""
    return "\n".join(" ".join(str(x) if x!=0 else "_" for x in state[i:i+3]) 
                     for i in range(0,9,3))

def neighbors(state):
    """Sinh các trạng thái con hợp lệ"""
    i0 = state.index(0)
    r,c = divmod(i0,3)
    res = []
    for name, dr, dc in MOVES:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr*3 + nc
            lst = list(state)
            lst[i0], lst[ni] = lst[ni], lst[i0]
            res.append((name, tuple(lst)))
    return res

def reconstruct(parent, move, goal):
    """Truy vết lời giải"""
    path=[]; moves=[]; cur=goal
    while cur is not None:
        path.append(cur)
        moves.append(move[cur])
        cur=parent[cur]
    path.reverse()
    moves.reverse()
    moves=moves[1:]  # bỏ bước đầu None
    return path,moves

# --- BFS ---
def bfs(start,goal):
    frontier = deque([start])
    parent={start:None}; move={start:None}
    while frontier:
        s = frontier.popleft()
        if s==goal:
            return reconstruct(parent,move,goal)
        for mv, ns in neighbors(s):
            if ns not in parent:
                parent[ns]=s; move[ns]=mv
                frontier.append(ns)
    return None,None

# --- DFS ---
def dfs(start,goal,limit=5000):
    stack=[start]
    parent={start:None}; move={start:None}
    visited=set()
    while stack and len(visited)<limit:
        s=stack.pop()
        if s in visited: continue
        visited.add(s)
        if s==goal:
            return reconstruct(parent,move,goal)
        for mv, ns in reversed(neighbors(s)):
            if ns not in parent:
                parent[ns]=s; move[ns]=mv
                stack.append(ns)
    return None,None

# --- IDDFS ---
def dls(s,goal,limit,parent,move,depth):
    if s==goal:
        return True
    if depth==limit:
        return False
    for mv, ns in neighbors(s):
        if ns not in parent:
            parent[ns]=s; move[ns]=mv
            if dls(ns,goal,limit,parent,move,depth+1):
                return True
            parent.pop(ns,None); move.pop(ns,None)
    return False

def iddfs(start,goal,max_d):
    for limit in range(max_d+1):
        parent={start:None}; move={start:None}
        if dls(start,goal,limit,parent,move,0):
            return reconstruct(parent,move,goal)
    return None,None

# --- UCS ---
def ucs(start,goal):
    pq=[]; counter=0
    heapq.heappush(pq,(0,counter,start))
    parent={start:None}; move={start:None}; cost={start:0}
    while pq:
        c,_,s = heapq.heappop(pq)
        if c!=cost[s]: continue
        if s==goal:
            return reconstruct(parent,move,goal)
        for mv, ns in neighbors(s):
            nc=c+1
            if ns not in cost or nc<cost[ns]:
                cost[ns]=nc; parent[ns]=s; move[ns]=mv
                counter+=1
                heapq.heappush(pq,(nc,counter,ns))
    return None,None

# ----------------- CHẠY THỬ -----------------
print("Start state:\n", pretty(start))
print("\nGoal state:\n", pretty(goal))
print("\n=============================\n")

for name,func in [("BFS",bfs),("DFS",dfs),("IDDFS(d=5)",lambda s,g:iddfs(s,g,5)),("UCS",ucs)]:
    print(f"--- {name} ---")
    path,moves = func(start,goal)
    if path:
        print("Tìm thấy lời giải!")
        print("Chuỗi bước:", "".join(moves))
        print("Số bước:", len(moves))
        for i,state in enumerate(path):
            print(f"Bước {i}: move={moves[i-1] if i>0 else None}")
            print(pretty(state))
            print("--------")
    else:
        print("Không tìm thấy lời giải (với giới hạn).")
    print()
