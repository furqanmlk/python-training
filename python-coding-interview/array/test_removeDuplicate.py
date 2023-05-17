'''
input = [1,1,2,2,3,3,4]
output = [1,2,3,4]
'''

def remove_Duplicate(arr):
    output = []

    for x in arr:
         if x not in output:
             output.append(x)
    return output

# remove duplicate without extra array, return the len of sorted element
'''
input = [1,1,1,1,2,2,2,3,3,4]
output = 5    i.e [1,2,3,4]
'''
def remove_Duplicate_Inplace(arr):
    head = 0

    for x in range(len(arr)):

        # if new num (x) is not same as head, which means we got new uniq num so incread head value
         if arr[x] != arr[head]: 
             head+=1
             arr[head] = arr[x]  # move head to next value and assign new uniq value to it
    
    return head + 1

# Same as above but without manuplate original array
def remove_dup_inplace(arr):
    seen = 0
    current = 0

    for x in range(len(arr)):
        if arr[x] != arr[current] :
            seen+=1
            current = x
    
    return seen + 1


input = [1,1,1,1,2,2,2,3,3,4]
print (remove_dup_inplace(input))