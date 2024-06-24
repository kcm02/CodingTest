def solution(N, stages):
    failure_rates = []

    for stage in range(1, N + 1):
        current_users = len([s for s in stages if s >= stage])
        if current_users == 0:
            failure_rate = 0
        else:
            failure_rate = stages.count(stage) / current_users
        failure_rates.append((stage, failure_rate))
    
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in failure_rates]