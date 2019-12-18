#双向链表

class doubleNode(object):
    def __init__(self,data = None,pre:doubleNode = None,next:doubleNode = None):
        #self = None
        self.data = data
        self.pre = pre
        self.next = next

class DoubleLinkedList(object):
    def __init__(self,firstNode:doubleNode=None,lastNode:doubleNode = None):
        #self = None
        self.firstNode = firstNode
        self.lastNode = lastNode

    def insert_at_end(self,value):
        newnode = doubleNode(value)
        if self == None:
            self.firstNode = newnode
            self.lastNode = newnode
        else:
            tempNode.pre = self.lastNode
            self.lastNode.next = newnode
            self.lastNode = newnode
 
    def remove_from_front(self):
        deleteNode = self.firstNode
        self.firstNode.next.pre = None
        self.firstNode = self.firstNode.next
        deleteNode.next = None
        return deleteNode

#双向链表实现的队列
class QueueByDL(object):
    def __init__(self,queue:DoubleLinkedList):
        self.queue = queue
    def enque(self,value):
        self.queue.insert_at_end(value)
    
    def deque(self):
        removenode = self.queue.remove_from_front()
        return removenode

    def tail(self):
        return self.queue.lastNode.data
    
        
        