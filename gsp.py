from pprint import pprint
import copy
from itertools import chain, product, combinations
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
    
    assert min_support > 0
    
    _ = {k: (min_support - 1) for k in prev_freq_seq.keys()}  # subtract 1 from `min_support` to keep min frequent items
    
    _ = Counter(_)
    
    _ = prev_freq_seq - _
    
    seed_set = list(_.keys())
    
    return seed_set


def generate_c_2_candidates(L_1):
    """"""
    
    C_2 = list(product(*[L_1, L_1]))
    C_2 = list([[i], [j]] for i, j in C_2)
    
    C_2_two_item_sets = list(combinations(L_1, 2))
    C_2_two_item_sets = list([[i, j]] for i, j in C_2_two_item_sets)
    
    C_2.extend(C_2_two_item_sets)
    
    return C_2


def is_subsequence(sequence, main_sequence):
    """"""
    
    if len(sequence) > len(main_sequence):
        return False
    
    for i, itemset in enumerate(main_sequence):
        
        if set(sequence[0]) <= set(itemset):
            
            if len(sequence) == 1:
                
                return True
            return is_subsequence(sequence[1:], main_sequence[i+1:])
    
    return False


#def generate_candidates(k):
    #""""""
    #L_km1  # the set of all frequent (k-1)-sequences -> use to generate a superset of the set of all frequent k-sequences (L_k)
    #L_k  # the set of all frequent k-sequences
    
    #return C_k  # the set of candidate k-sequences
    
    

init_support = get_init_support(D)
# pprint(init_support)
# >>> Counter({'f': 4, 'b': 4, 'e': 3, 'g': 3, 'a': 3, 'c': 2, 'd': 1})

L_1 = generate_seed_set(init_support)
# >>> ['f', 'b', 'a', 'c', 'e', 'g']

C_2 = generate_c_2_candidates(L_1)
# >>> [[['f'], ['f']],
# [['f'], ['e']],
# [['f'], ['g']],
# [['f'], ['a']],
# [['f'], ['c']],
# [['f'], ['b']],
# [['e'], ['f']],
# [['e'], ['e']],
# [['e'], ['g']],
# [['e'], ['a']],
# [['e'], ['c']],
# [['e'], ['b']],
# [['g'], ['f']],
# [['g'], ['e']],
# [['g'], ['g']],
# [['g'], ['a']],
# [['g'], ['c']],
# [['g'], ['b']],
# [['a'], ['f']],
# [['a'], ['e']],
# [['a'], ['g']],
# [['a'], ['a']],
# [['a'], ['c']],
# [['a'], ['b']],
# [['c'], ['f']],
# [['c'], ['e']],
# [['c'], ['g']],
# [['c'], ['a']],
# [['c'], ['c']],
# [['c'], ['b']],
# [['b'], ['f']],
# [['b'], ['e']],
# [['b'], ['g']],
# [['b'], ['a']],
# [['b'], ['c']],
# [['b'], ['b']],
# [['f', 'e']],
# [['f', 'g']],
# [['f', 'a']],
# [['f', 'c']],
# [['f', 'b']],
# [['e', 'g']],
# [['e', 'a']],
# [['e', 'c']],
# [['e', 'b']],
# [['g', 'a']],
# [['g', 'c']],
# [['g', 'b']],
# [['a', 'c']],
# [['a', 'b']],
# [['c', 'b']]]

# pprint(is_subsequence([["a"], ["a"]], D[0]))
# >>> False
# pprint(is_subsequence([["a"], ["a"]], D[1]))
# >>> True
# pprint(is_subsequence([["a"], ["a"]], D[2]))
# >>> False
# pprint(is_subsequence([["a"], ["a"]], D[3]))
# >>> False