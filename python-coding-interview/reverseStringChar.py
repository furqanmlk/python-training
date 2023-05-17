def revString(mystring):
    return mystring[::-1]

def revStringBuiltin(mystring):
    return "".join(reversed(mystring))

def revStrWhile(mystring): # Time complexity of this function is O(n*n)
    output =""
    i = len(mystring)-1
    while (i >= 0): # O(n)
        output+=mystring[i] # O(n), Cos it's adding the whole string that we've created 
                            # character by character to create a new copy of output.
        i-=1
    return output

def revStr(mystring): # this is function also has O(n*n)
    output = ""
    for x in mystring: 
        output = x + output 
    return output

def revStrWithArray(mystring): # this function has O(n)
    output =[]
    listlen = len(mystring)-1
    while listlen >= 0:
        output.append(mystring[listlen])
        listlen-=1
    return ''.join(output)
print(revStrWithArray("abcd"))

# print(revString("testing"))
# print(revStrWhile("testing"))
# print(revStrFor("testing"))
# print(revStringBuiltin("testing"))