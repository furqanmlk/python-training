# Question Check if tree is Birnary Search Tree

# Answer: Traverse the tree inOrder way and save all the nodes in list
#         verify nodelist is equal to sorted nodeList
#         because inOrder traverse gives sorted nodes

travList = []
def isBST(tree):
    if tree != None:
        isBST(tree.left)
        travList.appent(tree.value)
        isBST(tree.right)

def isSorted(travList):
    return travList == sorted(travList)


# Other way to check if tree is BST (Recommended)

def isBST(tree):
    return isBSTHelper(tree,float("-inf"),float("inf"))

def isBSTHelper(tree,minValue, maxValue):
    if tree is None:
        return False
    
    if tree.value < minValue and tree.value >= maxValue:
        return False
    
    leftValidation = isBSTHelper(tree.left, minValue, tree.value) # max of left is it's node value
    return leftValidation and isBSTHelper(tree.right, tree.value, maxValue) # min of right is it's node value 
    
    