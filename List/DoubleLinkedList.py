#双向链表

class doubleNode(object):
    def __init__(self,data,pre:doubleNode,next:doubleNode):
        #self = None
        self.pre = pre
        self.next = next

class DoubleLinkedList(object):
    def __init__(self,firstNode):
        #self = None
        self.firstNode = firstNode
 
        