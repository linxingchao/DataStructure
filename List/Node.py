class node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self,firstNode:node):
        self.firstNode = firstNode
    def read(self,index):
        current_node = self.firstNode
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index+=1
            if(current_index<index and current_node.next == None):
                return None
        return current_node.data

    def index_of(self,value):
        if(self.firstNode == None):
            return -1
        current_index = 0
        current_node = self.firstNode
        if(value == current_node.data):
            return current_index
        while value != current_node.data:
            current_node = current_node.next
            current_index+=1
            if(current_node.data == value):
                return current_index
            elif current_node.next == None:
                return -1
    def insert_at_index(self,index,tempnode:node):
        if(self.read(index) == None):
            raise RuntimeError("insert failed")
        node = self.read(index)
        if(node.next!=None):
            tempnode.next = node.next
        node.next = tempnode
        
    
    def delete_at_index(self,index):

        
    def delete_by_value(self,value):
    
    
node1 = node("1")
node2 = node("2")
node3 = node("3")
node4 = node("4")
node1.next = node2
node2.next = node3
node3.next = node4
    
list1 = LinkedList(node1) 
data = list1.read(5)
#print(data)
index = list1.index_of("5")
print(index);
