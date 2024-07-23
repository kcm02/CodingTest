import re

def solution(new_id: str) -> str:
    new_id = re.sub(r'[^a-zA-Z0-9._-]', '', new_id.lower())
    new_id = re.sub(r'\.{2,}', '.', new_id)
    new_id = new_id.strip('.')
    
    if not new_id:
        new_id = "a"
    
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id
