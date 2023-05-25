def binary_search(arr, elem):

    # [2,4,6,8,10,11,12]

    first = 0
    last = len(arr) - 1 # 6 = 7-1

    found = False

    while first <= last and not found:

        # get middle value
        mid = (first + last) // 2   # (0+6)//2 = 3

        # check if elem is in mid location,
        if arr[mid] == elem:
            found = True
        
        # if mid value is greater than elem, means right side of mid value can be discarded
        # so our last postion will move to mid - 1, cos mid has already been checked
        elif arr[mid] > elem:  
            last = mid -1 
        
        # if mid value is less than elem, means left side of mid value can be discarded
        # so our first postion will move to mid +1
        else: 
            first = mid + 1
    
    return found



def rec_binary_earch(arr,elem):

    found = False
    # base case
    if len(arr) ==  0:
        return False
    
    mid = len(arr) // 2

    if arr[mid] == elem:
        return True

    elif arr[mid] > elem:
        return rec_binary_earch(arr[:mid],elem)
    
    else:
        return rec_binary_earch(arr[mid+1:],elem)
    
    

arr = [1,2,3,4,5,6,7]
rec_binary_earch(arr,8)