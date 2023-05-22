def bubble_sort(arr):
    """
    Bubble Sort is the simplest sorting algorithm that works 
    by repeatedly swapping the adjacent elements if they are in wrong order.
    
    """
    swap_happened = True
    
    # This while loop just checking if there is any swap happend, if there is no swap which means list is sorted
    while swap_happened: 
        print('bubble sort status: ' + str(arr))
        swap_happened = False
        for num in range(len(arr)-1): # end of first loop, largest element will be at the end of the array
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5] # original case
# l = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1] # worst case
# l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10] # best case
bubble_sort(l)