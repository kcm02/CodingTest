def solution(id_pw, db):
    return "login" if id_pw in db else ("wrong pw" if id_pw[0] in [x for x,y in db] else "fail")