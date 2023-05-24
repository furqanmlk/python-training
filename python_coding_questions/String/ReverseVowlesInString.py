def reverseVowel(strr):
    vowels = ['a','e','i','o','u']
    strr = list(strr)
    start = 0, end = len(strr)-1
    while start < end:
        if strr[start] not in vowels: # start from the left
            start +=1 # it is not vowel go to next
        elfi strr[end] not in vowels:
            end -=1 # it is not vowel go to next
        else:
            # start and end are are vowel, swap them
            strr[start], strr[end] = strr[end], strr[start]
            start +=1
            end -=1

reverseVowel("hello") --> "holle"
reverseVowel("leetcode") --> "letcede"