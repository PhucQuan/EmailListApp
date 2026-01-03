#3 : ma di tuan

N = 8
moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

def is_safe(x,y,board):
    return 0<=x<N and 0<=y<N and board[x][y]==-1

def knight():
    board = [[-1]*N for _ in range(N)]
    board[0][0] = 0
    if not knight_tour(board,0,0,1):
        print("Không có lời giải")
    else:
        for row in board:
            print(row)

def knight_tour(board,x,y,movei):
    if movei == N*N:
        return True
    for dx,dy in moves:
        nx,ny = x+dx,y+dy
        if is_safe(nx,ny,board):
            board[nx][ny] = movei
            if knight_tour(board,nx,ny,movei+1):
                return True
            board[nx][ny] = -1
    return False

knight()



# bai2 con hau 
N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < N and board[i][col + (row - i)] == 1:
            return False
    return True

def solve(board, row=0):
    if row == N:
        print_board(board)
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, row+1)
            board[row][col] = 0
    return False

board = [[0]*N for _ in range(N)]
solve(board)



