"""
input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
"""
def get_indices_of_item_wights(arr, limit):
  
  output = []
  seen = {}
  
  for i in range(len(arr)):
    target = limit-arr[i]
    if target in seen:
      output.extend((i,seen[target]))
    else:
      seen[arr[i]] = i

  return output