"""
Consider an array of non-negative integers. 
A second array is formed by shuffling the elements of the first array 
and deleting a random element. 
Given these two arrays, 
find which element is missing in the second array.
"""

"""
Input:   finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:  5 is the missing number

"""

import unittest

def finder(list1,list2): # 

    for x in list1:
        if x in list2:
            list2.remove(x)
        else:
            return x

def finder02(list1,list2):

    dct = {}
    for x in list2: # making dictionry of all the element of list2 with occurance
        if x in dct:
            dct[x]+=1
        else:
            dct[x] = 1

    for x in list1: 
        if x not in dct: # Means element is missing 
           return x  
        if dct[x] == 0:  # Means element occurence is less than list1
            return x
        else: 
            dct[x]-=1

def finder_xor(list1,list2):
    xor_sum = 0

    for num in list1 + list2:
        xor_sum ^= num

    return xor_sum

finder_xor([4,12,9,5,6],[4,9,12,6])

class TestMissingElement(unittest.TestCase):

    def test_missingElement(self):
        self.assertEqual(finder02([5,5,7,7],[5,7,7]),5)
        self.assertEqual(finder02([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        self.assertEqual(finder02([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
