import pytest


def test_getFibonacci():
    assert getFibonacci_recursive(6) == 5

    assert getFibonacci_while(6) == 5

# Fibonacci No = [0,1,1,2,3,5,8,13,21,34,55]

# Write a function that takes in an integer n and returns the nth Fibonacci number.

# Input = 6
# Output = 5 (in Fib list, 5 is at 6th location)

# Solution 01 --> Recurrsive Time O(n2) | Space O(n)
def getFibonacci_recursive(n):
    if n==1:
        return 0
    elif n == 2:
        return 1
    else: 
        return getFibonacci_recursive(n-1) + getFibonacci_recursive(n-2) # Sum of prev two Number

# Solution 02 --> Itirative Time O(n) | Space O(1)
# We can optimize the space used in method 2 by storing the previous two numbers only 
# because that is all we need to get the next Fibonacci number in series.

def getFibonacci_while(n):
    
    lastTwo = [0,1]
    counter = 3
    while counter <=n :
        sum = lastTwo[0] + lastTwo[1]
        lastTwo[0]=lastTwo[1]
        lastTwo[1] = sum
        counter+=1
        
    return sum

# Solution 03 --> Memoization (Dynamic Programming) Time O(n) | Space O(n)
# We can avoid the repeated work done is the method 1 by storing the Fibonacci numbers calculated so far.

def getFibonacci_memoiz(n,memoiz={1:0,2:1}):
     
     # In DB we save resued data, and reuse when we need
    if n in memoiz:
        return memoiz[n]
    else:
        memoiz[n] = getFibonacci_memoiz(n-1, memoiz) + getFibonacci_memoiz(n-2,memoiz)
        return memoiz[n]


    