def solution(quiz):
    return [("O" if eval(ox.replace("=", "==")) else "X") for ox in quiz]