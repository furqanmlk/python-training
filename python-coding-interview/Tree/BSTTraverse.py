# O(n) time | O(n) space

def inorder(tree, arry):
    if tree:
        inorder(tree.left,arry)
        arry.append(tree.value)
        inorder(tree.left,arry)
    return arry


def postOrder(tree, arry):
    if tree:
        inorder(tree.left,arry)
        inorder(tree.left,arry)
        arry.append(tree.value)
    return arry 

def preOrder(tree, arry):
    if tree:
        arry.append(tree.value)
        inorder(tree.left,arry)
        inorder(tree.left,arry)
    return arry 