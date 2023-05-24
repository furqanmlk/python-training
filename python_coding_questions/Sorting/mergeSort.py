def merge_sorted(array1, array2):
    
    sorted_array=[]
    i,j = 0,0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            sorted_array.append(array1[i])
            i+=1
        else:
            sorted_array.append(array2[j])
            j+=1
    
    # if both lists are not same in length, then some element from larger list will remain out
    # so after above while loop, only one list will be used, other list still be left to be added
    
    while i < len(array1): # append array1 remaining items
        sorted_array.append(array1[i])
        i+=1
    
    while j < len(array2): # append array2 remaining items
        sorted_array.append(array2[j])
        j+=1
    
    print(sorted_array)
    
l1 = [1,3,6,9]
l2 = [2,4,6,8]

merge_sorted(l1,l2)