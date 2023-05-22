# Write a function that takes in an array of integers of length at least 2. 
# The function should return an array of the starting and ending indices 
# of the smallest subarray in the input array that needs to be sorted in place 
# in order for the entire input array to be sorted. 
# If the input array is already sorted, the function should return [-1, -1].

# Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# Sample output: [3, 9]

# Solution
"""
1) Find the candidate unsorted subarray
    a) Scan from left to right and find the first element which is greater than the next element. 
       Let s be the index of such an element. In the above example , s is 5 (index of 11).
    b) Scan from right to left and find the first element (first in right to left order) 
       which is smaller than the next element (next in right to left order). 
       Let e be the index of such an element. In the above example , e is 8 (index of 6).

2) Check whether sorting the candidate unsorted subarray makes the complete array sorted or not. 
If not, then include more elements in the subarray.
    a) Find the minimum and maximum values in arr[s..e]. 
        Let minimum and maximum values be min and max. min and max for [11, 7, 12, 6] are 6 and 12 respectively.
    b) Find the first element (if there is any) in arr[0..s-1] (from item 1 to 10) which is greater than min(6), 
        change s to index of this element. In example above s would be 3 (index of 7) as 7 is greater than min(6)
    c) Find the last element (if there is any) in arr[e+1..n-1] (from item 7 to 19) 
        which is smaller than max(12), change e to index of this element. 
        In the above example, e is changed to 9 (index of 7)
   
"""

def printUnsorted(arr, n): 
    e = n-1
    # step 1(a) of above algo 
    for s in range(0,n-1): 
        if arr[s] > arr[s+1]: 
            break
          
    if s == n-1: 
        print ("The complete array is sorted") 
        exit() 
  
    # step 1(b) of above algo 
    e= n-1
    while e > 0: 
        if arr[e] < arr[e-1]: 
            break
        e -= 1
  
    # step 2(a) of above algo 
    max = arr[s] 
    min = arr[s] 
    for i in range(s+1,e+1): 
        if arr[i] > max: 
            max = arr[i] 
        if arr[i] < min: 
            min = arr[i] 
              
    # step 2(b) of above algo 
    for i in range(s): 
        if arr[i] > min: 
            s = i 
            break
  
    # step 2(c) of above algo 
    i = n-1
    while i >= e+1: 
        if arr[i] < max: 
            e = i 
            break
        i -= 1