def insertionSort(array):
    
    for i in range(1,len(array)): # take element at location 1 first, and while loop will compare this element to all prev element and swap
        
        j = i
        while j > 0 and array[j] < array[j-1]: # check if element starting at position at i is greater than element all the way back to 0 postion, if yes swap
            array[j], array[j-1] = array[j-1], array[j]
            j-=1
            
    return array
    
    
l = [6,1,8,4,10]
insertionSort(l)
print(l)