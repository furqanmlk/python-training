import unittest
'''
Given a string,determine if it is compreised of all unique characters

Inoput: 'abcde'
Output: True

Input: 'abade'
Output: False
'''

def findUniqueCh01(st): # This is good solution but not accepted in interview
    return len(set(st)) == len(st)


def findUniqueCh(st):
    
    count = []

    for ch in st:
        if ch not in count:
            count.append(ch)
        else:
            return False
    
    return True


class TestfindUniqueCh(unittest.TestCase):

    def test_findUniqueCh(self):

        self.assertEqual(findUniqueCh(""),True)

        self.assertEqual(findUniqueCh("goo"),False)

        self.assertEqual(findUniqueCh("abcdefg"),True)

        self.assertEqual(findUniqueCh("aabbccaabb"),False)


