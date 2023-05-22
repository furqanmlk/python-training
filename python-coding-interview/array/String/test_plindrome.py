import unittest

def is_palindrome(input_string):
    
    '''
    is_palindrome("madam") -> True

    is_palindrome("aabb") -> False

    is_palindrome("race car") -> False

    is_palindrome("") -> True

    '''
    # Solution 01
    #return input_string == input_string[::-1]
    
    # Solution 02
    result = ''
    
    for e in input_string:
        result = e + result
    
    return input_string == result

class TestPlindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome(""),True)
        self.assertEqual(is_palindrome("Apple"),False)
        self.assertEqual(is_palindrome("hello"),False)
        self.assertEqual(is_palindrome("madam"),True)


