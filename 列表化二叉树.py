# 構建簡單的二叉樹列表
def BinaryTree(r):
    return [r, [], []]

# 插入左子樹
def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root

# 插入右子樹
def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
print(insertLeft(r, 4))
print(insertRight(r, 6))
# print(len(r.pop(1)))
print(insertLeft(r, 5))
print(insertRight(r, 7))
print(getRootVal(r))

setRootVal(r, 9)
print(r)

left = getLeftChild(r)
right = getRightChild(r)
print(left)
print(right)

insertRight(left, 8)
insertLeft(left, 1)
print(r)
print(left)
print(right)
#########################################################

# [3, [4, [], []], []]
# [3, [4, [], []], [6, [], []]]
# [3, [5, [4, [], []], []], [6, [], []]]
# [3, [5, [4, [], []], []], [7, [], [6, [], []]]]
# 3
# [9, [5, [4, [], []], []], [7, [], [6, [], []]]]
# [5, [4, [], []], []]
# [7, [], [6, [], []]]
# [9, [5, [1, [4, [], []], []], [8, [], []]], [7, [], [6, [], []]]]
# [5, [1, [4, [], []], []], [8, [], []]]
# [7, [], [6, [], []]]
