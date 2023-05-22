'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'

Input: 'AABBCC'
Output: 'A2B2C2'


'''

import unittest

def strCompression01(st): # Solution will fail for AAABBAA, 
                          #  it will return A5B2 instead A3B2A2
    output = ""
    count = {}

    for ch in st:
        if ch not in count:
            count[ch] = 1
        
        else:
            count[ch]+=1
    
    for (k,v) in count.items():
        output+= k+str(v)
    
    return (output)

def strCompression02(s):

    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # Check for length 0
    if l == 0:
        return ""
    
    # Check for length 1
    if l == 1:
        return s + "1"
    
    #Intialize Values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]: 
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1
            
        # Add to index count to terminate while loop
        i += 1
    
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)
    
    return r


def strCompression(st):

    if len(st) == 0:
        return ''
    
    if len(st) == 1:
        return st[0]+"1"

    char = st[0]
    count = 0
    output = ""
    
    for ch in st:
        if ch == char:
            count+=1
        else:
            output+=char+str(count)
            count=1
            char = ch

    output+=char+str(count)

    return (output)

#strCompression('')


class TeststrCompression(unittest.TestCase):

    def test_strCompression(self):
        
        self.assertEqual(strCompression(''),'')

        self.assertEqual(strCompression('AABBCC'),'A2B2C2')

        self.assertEqual(strCompression('AAABCCDDDDD'),'A3B1C2D5')

        self.assertEqual(strCompression('AAAaaaBBBbbb'),'A3a3B3b3')

        self.assertEqual(strCompression('AAABBBAA'),'A3B3A2')

        

