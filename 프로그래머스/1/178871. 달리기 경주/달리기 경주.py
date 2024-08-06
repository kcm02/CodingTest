def solution(players, callings):
    index_map = {player: i for i, player in enumerate(players)}
    for call in callings:
        n = index_map[call]
        players[n-1], players[n] = players[n], players[n-1]
        index_map[call] = n-1
        index_map[players[n]] = n
    return players