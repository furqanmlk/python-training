# Given an integer array, 
# output all the 'unique pairs' that sum up to a specific value k.

# input : [1,3,2,2],4
# output: 2    i.e. (1,3) (2,2)

import pytest

def test_arrayPairSum():
    assert pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10) == 6
    assert pair_sum([1,2,3,1],3) == 1
    assert pair_sum([1,3,2,2],4)== 2

def pair_sum(numlist,k):
    
    seen = set()
    output = set()
    for x in numlist:
        target = k-x  # this target must be in list if k is sum of this number
        if target not in seen:
            seen.add(x)
        else:
            output.add((target,x))
    return len(output)
