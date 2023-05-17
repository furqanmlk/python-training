class Node:
    
    def __init__(self,data=None):
        self.data = data
        self.next = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        myData = []
        current = self.head
        while current is not None:
            myData.append(str(current.data))
            current = current.next
        
        return "->".join(myData)
    
    def add_to_start(self,new_data):
        # https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
        
        # Convert new_data to Node if it is not node
        if not isInstance(new_data,Node):
            new_data = Node(new_data)
            
        # Example (head)2.next->5.next->7.next->9(tail)
        
        new_node = Node(new_data) # converting data to node
        
        # point new_node next to Head (head is the first node)
        new_node.next = self.head  # new_node.next->(head)2.next->5.next->7.next->9(tail)
        
        # Mode head point to new_node
        self.head = new_node  # (head)new_node.next->2.next->5.next->7.next->9(tail)
    
    def add_to_end(self,new_data):
        
        new_node = Node(new_data) # converting data to node
        
        # linked list is empty simply Mode head point to new_data
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node # (head)2.next->5.next->7.next->9(tail).next->new_node
        
        self.tail = new_node # (head)2.next->5.next->7.next->9.next->new_node(tail)
    
    def search(self, val):
        current = self.head
        while current is not None:
            if current.data == val:
                return True
            current = current.next
            
        return False
        
    def add_to_after(self,reqNode,new_data):
        
        # Example data : 2->5->7->9
        # reqNode = 5, new_data = 6
        # expected: 2->5->6->7->9
        if not isinstance(new_data,Node):
            new_data = Node(new_data)
        
        current = self.head
        while current is not None:
            if current.data == reqNode:
                new_data.next = current.next # 6.next = 5.next (i.e. 7)
                current.next = new_data # 5.next = 6 
                break
            current = current.next

    def removeByIndex(self, index):
        #Example data = 10->20->30->40->50->60
        # delete node at positon 3 (i.e. 40)
        current = self.head
        for i in range(index-1): # we want to access prev node (30) so we can access next (40)
            current = current.next
        
        print(current.data)   
        # at this point we are at prev position (30) of deleting node
        temp = current.next.next # temp = 30.next(40).next(50) = 50
        current.next = None # current(30).next(40) = None
        current.next = temp
        
            

mylist = LinkedList()
mylist.add_to_end(1)
mylist.add_to_end(2)
mylist.add_to_end(3)
mylist.add_to_end(4)
mylist.add_to_end(6)
mylist.add_to_after(4,5)

print(mylist.search(10)) # Flase
print(mylist.search(6)) # True
print(mylist) # 1->2->3->4->5->6
mylist.removeByIndex(3) # removing value 4
print(mylist) # 1->2->3->5->6