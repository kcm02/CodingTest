from itertools import permutations

def solution(spell, dic):
    spell_list = list(permutations(spell,len(spell)))
    return 1 if [1 for x in spell_list if ''.join(x) in dic] else 2