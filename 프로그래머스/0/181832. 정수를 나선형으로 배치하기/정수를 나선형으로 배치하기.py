def solution(n):
    r = [[0] * n for _ in range(n)]
    way = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dx, dy = 0, 1
    x, y = 0, 0

    for num in range(1, n**2 + 1):
        r[x][y] = num
        nx, ny = x + dx, y + dy

        if not (0 <= nx < n and 0 <= ny < n) or r[nx][ny] != 0:
            idx = way.index((dx, dy))
            dx, dy = way[(idx + 1) % 4]

        x, y = x + dx, y + dy

    return r