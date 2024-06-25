def solution(board, moves):
    basket = []
    count = 0
    
    for move in moves:
        for i in range(len(board[0])):
            if board[i][move-1]:
                if basket and basket[-1] == board[i][move-1]:
                    count += 2
                    basket.pop()
                else:
                    basket.append(board[i][move-1])
                board[i][move-1] = 0
                break 
    
    return count