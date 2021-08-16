class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # 插入左節點
    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # 插入右節點
    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())

r.insertLeft('b')
print(r.getLeftChild()) # 節點也是BinaryTree類型
print(r.getLeftChild().getRootVal())

r.insertRight('c')
print(r.getRightChild()) # 節點也是BinaryTree類型
print(r.getRightChild().getRootVal())

r.getRightChild().setRootVal('d')
print(r.getRightChild().getRootVal())
###################################################################

# a
# None
# <__main__.BinaryTree object at 0x000001ED525EAF10>
# b
# <__main__.BinaryTree object at 0x000001ED525EAAF0>
# c
# d
