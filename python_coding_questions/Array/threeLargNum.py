"""
Write a function that takes in an array of integers and returns a sorted array of the three largest integers in the input array. 
Note that the function should return duplicate integers if necessary; 
for example,it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
"""

#[1,2,3,4,5,6]
#[4,5,6]

# Time O(n)
# Space O(1) --> Not using variable to store all elements, only saving three numbers
def threeLarge(array):
    threeL = [float("-inf"),float("-inf"),float("-inf")]
    
    for num in array:
        if num > threeL[2]: # First check if num is largest of three, if yes then shift all numbers
            threeL[0] = threeL[1] 
            threeL[1] = threeL[2]
            threeL[2] = num
            
        elif num > threeL[1]: # If num is larger than second large num but less than third, then shift only first two
            threeL[0] = threeL[1]
            threeL[1] = num
        
        elif num > threeL[0]: # If num is larges than first large, but less than other two then just replace first one
            threeL[0] = num
    
    return threeL

# Time O(nLog) --> python uses Quick sort
# Space O(1)

def threeLarge_withSort(array):
    array.sort()
    return array[-3:]
    
print(threeLarge([5,5,5,2,4,5]))