"""
input: s1='MIKE'
       s2='TOM'
output: 'MTIOKME'
"""

def mergeStr(string1,string2):
    output = ""
    i=0
    j=0
    while (i < len(string1) or (j < len(string2))):
        if(i<len(string1)):
            output+=string1[i]
            i+=1
        if(j<len(string2)):
            output+=string2[j]
            j+=1


    print (output)

mergeStr("MIKE","TOMEOPO")