def solution(park, routes):
    ly, lx = len(park), len(park[0])
    start = [(y, x) for y in range(ly) for x in range(lx) if park[y][x] == "S"][0]
    y, x = start
    
    directions = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    
    for route in routes:
        op, n = route.split()
        dy, dx = directions[op]
        n = int(n)

        ny, nx = y, x
        valid_move = True
        for i in range(1, n + 1):
            ny, nx = y + dy * i, x + dx * i
            if not (0 <= ny < ly and 0 <= nx < lx) or park[ny][nx] == "X":
                valid_move = False
                break

        if valid_move:
            y, x = ny, nx

    return [y, x]
