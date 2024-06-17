def solution(keyinput, board):
    dx = {"left": -1, "right": 1, "up": 0, "down": 0}
    dy = {"left": 0, "right": 0, "up": 1, "down": -1}

    x, y = 0, 0
    max_x, max_y = (board[0] - 1) // 2, (board[1] - 1) // 2

    for direction in keyinput:
        nx, ny = x + dx[direction], y + dy[direction]

        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            x, y = nx, ny

    return [x, y]
