"""
Given an array of integers (positive and negative) find the sum of largest continuous subarray.

Input:  [1,2,-1,3,4,-1] # 

Output: 9

"""

import unittest

def largeContSum(list1):

    if len(list1) == 0:
        return 0
    
    max_sum = current_sum = list1[0]

    for num in list1[1:]: # start element from first, as 0 is already been taken for max and crnt
        if(current_sum+num > num):
            current_sum = current_sum+num
        else:
            current_sum = num

        if(current_sum > max_sum):
            max_sum = current_sum
    
    return max_sum    

class TestLargeContSum(unittest.TestCase):

    def test_largeContSum(self):
        self.assertEqual( largeContSum([1,2,-1,3,4,-1]),9 ) 
        self.assertEqual( largeContSum([1,2,-1,3,4,10,10,-10,-1]),29 ) 
        self.assertEqual( largeContSum([-1,1]),1 ) 
        self.assertEqual( largeContSum([-1,-1,-1,-1,-1,10]),10 ) 
