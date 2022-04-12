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


def generate_seed_set(prev_freq_seq, min_support=2):
    """"""
    
    _ = {k: (min_support - 1) for k in prev_freq_seq.keys()}  # subtract 1 from `min_support` to keep min frequent items
    
    _ = Counter(_)
    
    _ = prev_freq_seq - _
    
    seed_set = list(_.keys())
    
    return seed_set
    

init_support = get_init_support(D)
# pprint(init_support)
# >>> Counter({'f': 4, 'b': 4, 'e': 3, 'g': 3, 'a': 3, 'c': 2, 'd': 1})

pprint(generate_seed_set(init_support))
# >>> ['f', 'b', 'a', 'c', 'e', 'g']


