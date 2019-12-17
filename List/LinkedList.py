#单向链表
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
        if self == None or self.index_of(index) == None:
            raise RuntimeError("failed")
        current_index = 0;
        current_node = self.firstNode
        
        if index == 0:
            if(self.firstNode.next == None):
                current_node = self.firstNode
                self.firstNode = None
            else:
                current_node=self.firstNode
                self.firstNode = self.firstNode.next
            return current_node
        while current_index<index:
            if(current_index+1 == index):
                if(current_node.next.next.next!=None):
                    deleteNode = current_node.next
                    current_node.next = current_node.next.next
                    return deleteNode
                else:
                    deleteNode = current_node.next
                    current_node.next = None
                    return deleteNode
            current_index+=1
            current_index = current_node.next
                    
    def delete_by_value(self,value):
        if(self.index_of(value) == -1):
            return None
        current_node = self.firstNode
        if(self.firstNode.next == None and self.firstNode.data == value):
            self.firstNode = None
        while(current_node.next!=None):
            if(self.firstNode.data == value):
                self.firstNode = self.firstNode.next
            else:
                if(current_node.next.data == value):
                    if(current_node.next.next!=None):
                        current_node.next = current_node.next.next
                    else:
                        current_node.next = None
    

    
    
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
