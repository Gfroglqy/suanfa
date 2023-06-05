#将n枚硬币摆成阶梯型，第k行刚好有k枚硬币，给定n，找出完整阶梯的总行数

#暴力--self
import math


def method(x):
    sum = 0
    if (x == 1):
        return 1
    for i in range(1, x+1):
        sum += i
        if (sum > x):
            return i-1
    return 0

#暴力--b   迭代思维
def method2(x):
    for i in range(1, x):
        x = x - i
        if (x <= i):
            return i
    return 0

#二分查找
def method3(x):
    low = 0
    high = x
    while(low <= high):
        mid = int(low + (high - low)/2)
        cost = (mid * mid + mid)/2
        if (cost == x):
            return mid
        elif(cost > x):
            high = mid - 1
        else:
            low = mid + 1
    return high             #当硬币数为2时，需要返回high指针，为1

#牛顿迭代
def method4(x):
    if (x == 0):
        return 0
    return int(digui(x, x))

def digui(x, n):
    res = (x + (2*n - x)/x)/2
    res = int(res)
    if(res == x):
        return x
    else:
        return digui(res,x)

if __name__ == "__main__":
    print(method(6))
    #arr = list(range(1, 5, 2))
    print(method2(10))
    print(method3(7))
    print(method4(7))