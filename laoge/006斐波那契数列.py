#求斐波那契数列第n位的值

import numpy as np

#暴力递归
def method(x):
    if(x == 0):
        return 0
    if(x == 1):
        return 1
    return method(x - 1) + method(x - 2)

#去重递归  数组
def method2(x):
    arr = np.zeros(x + 1)
    #print(arr)
    return recurse(arr, x)

def recurse(arr, x):
    if (x == 0):
        return 0
    if (x == 1):
        return 1
    if (arr[x] != 0):
        return arr[x]
    return recurse(arr, x-1) + recurse(arr, x-2)

#双指针迭代
def method3(x):
    low = 0
    high = 1

    if(x == 0):
        return 0
    elif (x == 1):
        return 1

    for i in range(2, x+1):
        sum = low + high
        low = high
        high = sum

    return high

if __name__ == "__main__":
    print(method(10))
    #arr = list(range(1, 5, 2))
    print(method2(10))
    print(method3(10))
