def solution(box, n):
    length = box[0] // n
    width = box[1] // n
    height = box[2] // n
    
    return length * width * height