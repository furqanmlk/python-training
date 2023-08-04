# Time O(n) n= number of elements including sub array 
# Space O(d) d= number of sub array

import pytest

def test_productSum():
    li = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    assert productSum(li) == 12 # Output : 12

def productSum(array, multiplier=1):
    # Sample input: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    summ = 0
    sum = 0
    for element in array:
        if type(element) is list:
            sum+= productSum(element,multiplier+1)
        else:
            summ+=element
    
    return summ*element

