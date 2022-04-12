from pprint import pprint
import copy
from itertools import chain
from collections import Counter


D = [
    [["a", "b"], ["c"], ["f", "g"], ["g"], ["e"]],
    [["a", "d"], ["c"], ["b"], ["a", "b", "e", "f"]],
    [["a"], ["b"], ["f", "g"], ["e"]],
    [["b"], ["f", "g"]]
]

def get_init_support(D):
    """"""
    
    D_copy = copy.deepcopy(D)
    
    _ = (chain(*s) for s in D_copy)

    _ = (set(s) for s in _)

    _ = (Counter(s) for s in _)

    init_support = sum(_, start=Counter())
    
    return init_support

pprint(get_init_support(D))

# >>> Counter({'f': 4, 'b': 4, 'e': 3, 'g': 3, 'a': 3, 'c': 2, 'd': 1})
