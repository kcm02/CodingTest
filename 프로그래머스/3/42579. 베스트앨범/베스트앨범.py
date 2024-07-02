def solution(genres, plays):
    answer = []
    music = {}
    total = {}
    
    for i in range(len(genres)):
        music[i] = plays[i]
        
        if genres[i] in total:
            total[genres[i]].append((i, plays[i]))
        else:
            total[genres[i]] = [(i, plays[i])]
    
    sorted_genres = sorted(total.items(), key=lambda x: -sum(play for _, play in x[1]))
    
    for genre, songs in sorted_genres:
        sorted_songs = sorted(songs, key=lambda x: (-x[1], x[0]))
        answer.extend([song[0] for song in sorted_songs[:2]])
    
    return answer