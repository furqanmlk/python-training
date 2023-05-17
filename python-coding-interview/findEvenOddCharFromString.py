"""
input: '0123456789'
output: Even Char are 02468
        Odd Char are 13579
"""

def findEvenOddChar(myString):
    evenStr = ["Even Char are"]
    oddStr = ["Odd Char are"]
    for i in range(len(myString)):
        if(i%2):
            oddStr.append(myString[i])
        else:
            evenStr.append(myString[i])
    print (evenStr)
    print (oddStr)

def findEvenOddCharSlice(myString):
    evenChar = myString[0::2]
    print (evenChar)
    oddChar = myString[1::2]
    print(oddChar)
            

findEvenOddChar("0123456789")
