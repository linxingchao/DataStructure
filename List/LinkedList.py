#单向链表
class node(object):
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self,firstNode:node = None):
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

    #索引
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

    #插入
    def insert_at_index(self,index,tempnode:node):
        if(self.read(index) == None):
            raise RuntimeError("None")
        if(index == 0):
            node.next = self.firstNode
            self.firstNode = node
        else:
            current_node = self.firstNode
            current_index = 0
            while current_node.data!=None and current_node.next!=None:
                if(current_index!=index-1):
                    current_index+=1
                    current_node = current_node.next
                else:
                    tempnode.next = current_node.next
                    current_node.next = tempnode
                    break

                    
        
    #删除
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
                if(current_node.next.next!=None):
                    deleteNode = current_node.next
                    deleteNode.next = None
                    current_node.next = current_node.next.next
                    return deleteNode
                else:
                    deleteNode = current_node.next
                    deleteNode = None
                    current_node.next = None
                    return deleteNode
            current_index+=1
            current_node = current_node.next
    #删除            
    def delete_by_value(self,value):
        if(self.index_of(value) == -1):
            return None
        current_node = self.firstNode
        current_index = 0
       
        while True:
            if(current_node == self.firstNode and current_node.next == None and current_node.data == value):
                self.firstNode = None
            elif current_node == self.firstNode and current_node.data == value:
                self.firstNode = self.firstNode.next
                current_node = self.firstNode
            else:
                if(current_node.next == None):
                    break;
                if current_node.next.data == value and current_node.next.next!=None:
                    current_node.next = current_node.next.next
                elif current_node.next.data == value and current_node.next.next == None:
                    current_node.next = None
                if(current_node.next.data!=value):
                    current_node = current_node.next
                    
                
                

            
    

    
    
node1 = node("1")
node2 = node("2")
node3 = node("3")
node4 = node("4")
node1.next = node2
node2.next = node3
node3.next = node4

node5 = node("5")
list1 = LinkedList(node1) 
#1,2,5,3,4
list1.insert_at_index(2,node5)

node6 = node("5")
list1.insert_at_index(2,node6)
list1.delete_by_value("5")
current_node = list1.firstNode
while True:
    print(current_node.data)
    if(current_node.next == None):
        break
    current_node = current_node.next

