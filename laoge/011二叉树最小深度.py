#找到给定二叉树的最小深度--深度优先与广度优先    节点搜索算法

#创建二叉树内部类
#二叉树节点的定义
class TreeNode(object):
    def __init__(self,item):
        self.elem = item
        self.left = None
        self.right = None

#树的定义
class Tree(object):
    def __init__(self):
        self.root = None #根结点

    def add(self, item):
        node = TreeNode(item)
        if self.root is None:
            self.root = node
            return
        


#深度优先
def method(x, k):
    if root == None:
        return 0

    if (root)
    return 0

#滑动窗口
def method2(x, k):
    return max/k



if __name__ == "__main__":
    nums1 = [1, 3, 5, 7, 9]
    k = 3
    print(method2(nums1, k))
    #arr = list(range(1, 5, 2))
    #print(method2(10))
    #print(method3(7))
