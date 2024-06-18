def solution(board):
    n = len(board)
    danger = [[0] * n for _ in range(n)]

    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),         (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger[i][j] = 1
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = 1

    safe_count = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe_count += 1

    return safe_count