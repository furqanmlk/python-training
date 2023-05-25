"""
input: B4A1D3
output: ABD134
"""

def sortStringWithNum(myString):
    alpha = []
    digit = []
    for ch in myString:
        if(ch.isalpha()):
            alpha.append(ch)
        else:
            digit.append(ch)
    print (alpha)
    print (digit)
    test = ''.join(sorted(alpha) + sorted(digit))
    print (test)

"""
input: a4b3c4
output: aaaabbbcccc
"""
def printChar(myString):
    char = ""
    output = ""
    for ch in myString:
        if ch.isalpha():
            char= ch
        else:
            output+=int(ch)*char
    print (output)

"""
input: a4z3c4
output: aaaacccczzz (Sorted)
"""
def printCharSorted(myString):
    char = ""
    output = ""
    for ch in myString:
        if ch.isalpha():
            char = ch
        else:
            output+=int(ch)*char
    sorti = sorted(output)
    print (''.join(sorti))

"""
input: aaaabbbcccc
output: 4a3b4c
"""
def countChar(myString):
    char = myString[0]
    count = 0
    output = ""
    for ch in myString:
        if ch == char:
            count+=1
        else:
            output+=str(count)+char
            count=1
            char = ch
    output+=str(count)+char
    print (output)

countChar("aaaabbbccccaaa")

# printCharSorted("a4bz3c4")
# sortStringWithNum("B4A1D3")

