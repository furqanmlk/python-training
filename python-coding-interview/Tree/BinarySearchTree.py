class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
#        10
#      /   \
#     5    15
#   / \    / \
#  2  7  12   22 
# /
#1
    # Average Time O(Log(n)) | Space O(1)
    # Worst Time O(n) | Space O(1)
    
    def insert(self,value): # let's insert 8
        currentValue = self # (10)
        
        while True:
            # loop 01 --> value (8) is less than currentValue(10) TRUE
            if value < currentValue.value: 
                if currentValue.left = None: # loop 01 --> if left node(5) of currentValue(10) is None, FALSE
                                            
                    currentValue.left = BST(value) # assign new node to that leaf
                    break
                else:
                    currentValue = currentValue.left # loop 01 --> left node(5) is not None then go to Node(5)
                                                     #             currentValue is 5 now
            
            else: 
                  # loop 02 --> value (8) is greater than currentValue (5) TRUE
                  # loop 03 --> value (8) is greater than currentValue (7) TRUE
                if currentValue.right = None: 
                                            # loop 02 --> if right node (7) of currentValue (5) is None FALSE
                                            # loop 03 --> if right node (None) of currentValue (7) is None TRUE
                    currentValue.right = BST(value) # assign new node (8) to that leaf
                    break
                else:
                    currentValue = currentValue.right # loop 02 --> currentValue is 7 is now
        return self
    
    
    # Average Time O(Log(n)) | Space O(1)
    # Worst Time O(n) | Space O(1)
    
    def search(self,value):
        currentNode = self
        while currentNode is not None: # Traverse tree untill reach to leaf
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
        