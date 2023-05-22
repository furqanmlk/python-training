"""
input : This is Python
output: Python is This
"""

def revWordOrderWhile(mySentance):
    splited = mySentance.split()
    output = ""
    i = len(splited)-1
    while i>=0 :  
        output+=splited[i] + " "
        i-=1
    return output

def revWordOrderSlice(mySentance):
    splitted = mySentance.split() # this will create list 
    output = ' '.join(splitted[::-1]) # reversing list and joiing element with space
    return output

print (revWordOrderSlice("Python is good language for learn") )