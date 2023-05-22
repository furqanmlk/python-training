"""
intput: This is my Python
output: nohtyP my si siht
"""

def revWordChar(mySentance):
    splitted = mySentance.split()
    output = ""
    for eachWord in splitted:
        output+=eachWord[::-1] + " "
    return output

def revWordCharJoin(mySentance):
    splitted = mySentance.split()
    l = []
    for eachWord in splitted:
        l.append(eachWord[::-1])
    
    return ' '.join(l)

print (revWordCharJoin("This is my Python"))

# REVERS every second word present in the given string
def revSecWord(mySentance):
    splitted = mySentance.split()

    for i in range(len(splitted)):
        if(i%2):
            splitted[i] = splitted[i][::-1]

    return ' '.join(splitted)


print (revSecWord("first second third second fifth second"))

