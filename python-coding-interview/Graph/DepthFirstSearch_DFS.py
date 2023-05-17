# To Understand DFS 
# https://www.kirupa.com/developer/actionscript/depth_breadth_search2.htm

"""
The Depth-first Search algorithm works by traversing a graph branch by branch. 
In other words, before traversing any Node's sibling Nodes, its children nodes must be traversed. 

Solutuon:
Start at the root Node and try simply calling the depthFirstSearch method on all of its children Nodes. 
Then, call the depthFirstSearch method on all children Nodes of each child node. 
Keep applying this logic until the entire graph has been traversed. 

Don't forget to add the current Node's name to the input array at every call of depthFirstSearch.
"""
class Graph:
    
    def _init_(selef, node):
        self.node = node
        self.children = []
    
    def addChild(self, child):
        self.children.append(Graph(child))
    
    def dfs(self,arry):
        # adding node name to arry as we have visited it
        arry.append(self.node) 
        for child in self.chidren:
            child.dfs(arry)
        
        return arry
