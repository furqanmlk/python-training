import unittest
"""
input: a4b3c4

output: aaaabbbcccc

"""

def strDecompression(st):

    if len(st) == 0:
        return ""

    if len(st) == 1:
        return st
    
    i = 0
    output = ""

    while i < len(st)-1:

        output+= int(st[i+1])*st[i]
        i+=2
    
    return output
        

class TeststrDecompression(unittest.TestCase):

    def test_strDecompression(self):

        self.assertEqual(strDecompression("A3B3C3"),"AAABBBCCC")

        self.assertEqual(strDecompression("A3B3A3"),"AAABBBAAA")

        self.assertEqual(strDecompression("A1"),"A")

