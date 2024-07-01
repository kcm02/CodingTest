def solution(record):
    user = {}
    answer = []
    
    for row in record:
        parts = row.split()
        cmd = parts[0]
        
        if cmd in ["Enter","Change"]:
            user_id, name = parts[1], parts[2]
            user[user_id] = name
            
        if cmd == "Enter":
            answer.append((user_id, "님이 들어왔습니다."))
        elif cmd == "Leave":
            user_id = parts[1]
            answer.append((user_id, "님이 나갔습니다."))
    
    return [user[user_id] + message for user_id, message in answer]