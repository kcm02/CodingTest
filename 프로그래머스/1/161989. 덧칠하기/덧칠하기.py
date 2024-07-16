def solution(n, m, section):
    count = 0
    index = 0
    while index < len(section):
        last_section_index = section[index] + m - 1
        while index < len(section) and section[index] <= last_section_index:
            index += 1
        count += 1
    return count