from pprint import pprint
import copy
from itertools import chain, product, combinations
from collections import Counter


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


def prune_k_2(C_2, D, min_support):
    """"""
    
    L_2 = []
    
    for c in C_2:
        
        _ = sum(is_subsequence(c, d) for d in D)
        
        if _ >= min_support:
            
            L_2.append(c)
    
    return L_2


def generate_km1_subsequences(C_k):
    """"""
    
    raise NotImplementedError()
