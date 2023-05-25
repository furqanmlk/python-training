"""
intput: dog
output: god
"""
import unittest

def anagram01(st1,st2): 
    
    st1 = st1.replace(' ','').lower()
    st2 = st2.replace(' ','').lower()

    if(len(st1) != len(st2)):
        return False

    for c in st1:
        if c not in st2:
            return False
    
    for c in st2:
        if c not in st1:
            return False

    return True


def anagram(st1,st2):

    st1 = st1.replace(' ','').lower()
    st2 = st2.replace(' ','').lower()

    count = {}

    for ch in st1:
        # checking if each char in st1 exists in count
        if ch in count:
            count[ch] += 1 # ch is in count add 1
        else:
            count[ch] = 1 # ch is not in count assign 1
        
    # at this point count dict updated with occurrance of each char in st1

    # now checking if all char in st2 exist in count dict with thier occurance 
    
    for ch in st2:
        if ch in count:
            count[ch] -= 1
        else:
            return False
    
    for v in count.values():
        if v != 0:
            return False
    
    return True


class TestAnagram(unittest.TestCase):

    def test_anagram(self):
        self.assertFalse(anagram01("hello","helgo"),False)
        self.assertTrue(anagram01('abc','cba'))
        self.assertFalse(anagram01('aabbcc','aabbc'))
        self.assertFalse(anagram01('123','1 2'))
        self.assertTrue(anagram01('go go go','gggooo'))
        self.assertTrue(anagram01('hi man','hi     man'))