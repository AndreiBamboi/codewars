import itertools
def permutations(string):
    values=list(itertools.permutations(list(string)))
    list_clear=[]
    for i in values:
        list_clear.append(''.join(list(i)))
    print(set(list_clear))
    return set(list_clear)

permutations('aabb')