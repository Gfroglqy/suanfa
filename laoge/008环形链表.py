#给定一个链表，判断链表中是否有环

#定义链表
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None
    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        print("节点", data, "==>", self.cur_node)
        return node
    def printInfo(self, node):
        while node:
            print('node', node, 'calue', node.val, 'next', node.next)
            node = node.next


#暴力
def method(x):

    return 0

#暴力--b   迭代思维
def method2(x):

    return 0



if __name__ == "__main__":
    print(method(6))
    #arr = list(range(1, 5, 2))
    #print(method2(10))
    #print(method3(7))
