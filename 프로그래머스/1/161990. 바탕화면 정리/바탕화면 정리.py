def solution(wallpaper):
    min_row, min_col, max_row, max_col = float('inf'), float('inf'), float('-inf'), float('-inf')

    for i, row in enumerate(wallpaper):
        for j, value in enumerate(row):
            if value == "#":
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)

    return [min_row, min_col, max_row + 1, max_col + 1]