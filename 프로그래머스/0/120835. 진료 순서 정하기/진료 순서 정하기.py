def solution(emergency):
    return [sorted(emergency, reverse=True).index(x) + 1 for x in emergency]