import unittest
"""
You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. Flip it in-place along its horizontal axis.

Example:

Input :  [[1,2,3],[4,5,6],[7,8,9]]

Output : [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
              
"""
def flip_matrix(matrix):

    result = []
    siz = len(matrix)-1

    while siz >= 0:
        result.append(matrix[siz])
        siz-=1
    
    return result

flip_matrix([[1,0,0],[0,0,1]])

class TestreverseArrayOfArrayElem(unittest.TestCase):

    def test_reverseArrayOfArrayElem(self):

        self.assertEqual(flip_matrix([[1,0,0],[0,0,1]]), [[0, 0, 1], [1, 0, 0]])
        self.assertEqual(flip_matrix([[1,2,3],[4,5,6],[7,8,9]]), [[7, 8, 9], [4, 5, 6], [1, 2, 3]])
