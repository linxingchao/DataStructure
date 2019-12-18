class TreeNode:
    def __init__(self,data,left:TreeNode=None,right:TreeNode=None):
        self.data = data
        self.leftChild = left
        self.rightChild = right
#简单二叉树，不考虑平衡
class BTree(object):
    def __init__(self,root:TreeNode):
        self.rootNode = root
    #传入的第一个node是rootNode
    def search(self,value,node):
        if(node == None):
            return None
        if(value == node.data):
            return node
        elif value<node.data and node.leftChild!=None:
            return self.search(value,node.leftChild)
        elif value<node.data and node.leftChild == None:
            return None
        elif value>node.data and node.rightChild != None:
            return self.search(value,node.rightChild)
        elif value>node.data and node.rightChild == None:
            return None

   
    #非平衡插入,传入的第一个node是rootNode
    def insert(self,value,node:TreeNode):
        
        if value<node.data:
            if(node.leftChild == None):
                node.leftChild = TreeNode(value)
            else:
                node = node.leftChild
                self.insert(value)

        if value>node.rightChild:
            if node.rightChild == None:
                node.rightChild = TreeNode(value)
            else:
                node = node.rightChild
                self.insert(value)

    def delete(self,valueToDelete,node:TreeNode):
        #当前位置无子节点，
        if node == None:
            return None
        #删除的值小于，向左查找，
        #删除的值大于，向右查找

        elif valueToDelete<node.data:
            node.leftChild = self.delete(valueToDelete,node.leftChild)
            return node
        elif valueToDelete>node.data:
            node.rightChild = self.delete(valueToDelete,node.rightChild)
            return node
        elif valueToDelete == node.data:
            if node.leftChild == None:
                return node.rightChild
            elif node.rightChild == None:
                return node.leftChild
            else:
                node.rightChild = self.lift(node.rightChild,node)
                return node
    
    def lift(self,node:TreeNode,nodeToDelete:TreeNode):
        # 如果 此 函数 的 当前 结点 有 左 子 结点， 
        # # 则 递归 调用 本 函数， 从左 子 树 找出 后继 结点
        if node.leftChild:
            node.leftChild = lift(node.leftChild,nodeToDelete)
            return node
        else:
            nodeToDelete.data = node.data
            return node.rightChild