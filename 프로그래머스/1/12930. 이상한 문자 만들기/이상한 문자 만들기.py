def solution(s):
    def transform_word(word):
        return ''.join(x.upper() if i % 2 == 0 else x.lower() for i, x in enumerate(word))
    return ' '.join(transform_word(word) for word in s.split(' '))