#给定一个未经排序的整数数组，找到最长的连续递增子序列，返回序列长度
import numpy as np

#贪心算法
def method1(x):
    left = 0
    num = 0
    for i in range(1, len(x)):
        if x[i] <= x[i-1]:
            left = i
        num = max(num, i-left+1)

    return num

if __name__ == '__main__':
    a = np.random.randint(0, 100, size=[20])    #创建随机整数数组，[1，5]实际是二维
    print(a)
    #print(a.shape)
    print(method1(a))