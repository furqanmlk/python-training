def seq_search(arr,elem):

    pos = 0
    found = False

    while pos < len(arr) and not found:

        if arr[pos] == elem:
            found = True
        
        else:
            pos+=1
    
    return found


def ordered_sq_search(arr,elem):

    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:

        if arr[pos] == elem:
            found = True
        
        elif arr[pos] > elem:
            stopped = True
        
        else:
            pos+=1
    
    return False

arr = [12,13,14,16,18,20]
ordered_sq_search(arr,17)