"""
Given two unsorted arrays of distinct elements, 
the task is to find all pairs from both arrays whose sum is equal to x.
"""

"""
nput :  arr1 = [-1, -2, 4, -6, 5, 7]
        arr2 = [6, 3, 4, 0]  
        x = 8
Output : [(5, 3), (4, 4)]
         

Input : arr1 = [1, 2, 4, 5, 7] 
        arr2 = [5, 6, 3, 4, 8]  
        x = 9
Output : [(1, 8), (4, 5), (5, 4)]
"""

import unittest

def pari_sum(list1,list2,x):

    output = []
    for k in list1:
        if (x-k) in list2:
            output.append((k,x-k))

    return (output)



class TestPairSumTwoArray(unittest.TestCase):

    def test_pairSumTwoArray(self):
        self.assertEqual(pari_sum(   [1, 2, 4, 5, 7],   [5, 6, 3, 4, 8],  9),
                        [(1, 8), (4, 5), (5, 4)])

        self.assertEqual(pari_sum(  [-1, -2, 4, -6, 5, 7],   [6, 3, 4, 0],  8),
                        [(4, 4),(5,3)])

        self.assertEqual(pari_sum(  [-1, -2, 4, -6, 5, 7],   [6, 3, 4, 0, 1, 2, 3],  8),
                        [(4, 4),(5,3),(7,1)])