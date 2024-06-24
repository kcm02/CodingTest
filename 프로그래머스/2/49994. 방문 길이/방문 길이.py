def solution(dirs):
    directions = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    point = set()
    x,y = 0, 0
    
    for dir in dirs:
        dx, dy = directions[dir]
        nx, ny = x+dx, y+dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = (x, y, nx, ny) if (x, y) < (nx, ny) else (nx, ny, x, y)
            point.add(path)
            x, y = nx, ny
        
    return len(point)