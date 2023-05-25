import unittest
'''
Given a string of words, reverse all the words. For example:
Note: reverse the words not characters in word :)

Given:  'This is the best'

Return: 'best the is This'

'''

def rev_word01(testString):
    return " ".join(reversed(testString.split()))

def rev_word02(testString):
    return " ".join(testString.split()[::-1])

# Above solutions are perfectly fine, but Interviewer is not interested
# but you show him that python can solve this problem, to show him that you know python

def rev_word(testString):

    i = len(testString)
    word = ""
    sent = []

    while i > 0:
        i-=1
        if(testString[i] != " "):  # if element is not space,  which means this is start of word
            word = testString[i]+word # add it to word string

        elif len(word) != 0: # if element is space and word string is not empty
            sent.append(word)
            word=""

    if len(word) != 0: # if element is last and word string is not empty
            sent.append(word)
    return ' '.join(sent)


#rev_word('space after     ')
            
    



class TestSentReversal(unittest.TestCase):

    def test_rev_word(self):
        self.assertEqual(rev_word('    space before'),'before space')
        
        self.assertEqual(rev_word('space after     '),'after space')

        self.assertEqual(rev_word('   Hello John    how are you   '),'you are how John Hello')

        self.assertEqual(rev_word('1'),'1')

        self.assertEqual(rev_word('a e i o u'),'u o i e a')
