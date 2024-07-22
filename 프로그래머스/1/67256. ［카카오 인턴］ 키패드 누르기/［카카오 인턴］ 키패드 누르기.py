def solution(numbers, hand):
    key_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }
    
    left_hand = (3, 0)  # '*' 키패드 위치
    right_hand = (3, 2) # '#' 키패드 위치
    
    result = []

    left_keys = {1, 4, 7}
    right_keys = {3, 6, 9}
    
    for number in numbers:
        target_position = key_positions[number]
        if number in left_keys:
            result.append('L')
            left_hand = target_position
        elif number in right_keys:
            result.append('R')
            right_hand = target_position
        else:
            left_distance = (abs(left_hand[0] - target_position[0]) +
                             abs(left_hand[1] - target_position[1]))
            right_distance = (abs(right_hand[0] - target_position[0]) +
                              abs(right_hand[1] - target_position[1]))
            
            if left_distance < right_distance:
                result.append('L')
                left_hand = target_position
            elif right_distance < left_distance:
                result.append('R')
                right_hand = target_position
            else:
                if hand == 'left':
                    result.append('L')
                    left_hand = target_position
                else:
                    result.append('R')
                    right_hand = target_position
    
    return ''.join(result)