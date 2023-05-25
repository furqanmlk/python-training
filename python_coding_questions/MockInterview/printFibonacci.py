'''
fibonacci Numbers = 0 1 1 2 3 5 8 13 21  ( sum of last two numbers)

fibonacci(1) --> 0   ( print firt fib number)
fibonacci(2) --> 0 1  (print firt two fib num)
fibonacci(3) --> 0 1 1  ( print first three fib num)
fibonacci(4) --> 0 1 1 2 

'''

def fibonacci_01(n):

    # First two fib numbers
    a = 0
    b = 1

    if n == 1: # Print first fib num
        print (a)
    elif n == 2: # print first two fib num
        print(a,b,end=" ")
    
    else:
        print(a,b,end=" ")
        for x in range(2,n): # starting from 2nd element, first two numbers have been taken care
            c = a + b # 0 + 1 = 1 ( third element)
            a = b # moving a value to next ( now a = 1)
            b = c # moving b value to next ( now b = sum of last two)
            print (b,end = " ")

    
def  fibonacci_02(n):

    if n<0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibonacci_02(n-1) + fibonacci_02(n-2))

print (fibonacci_02(9))