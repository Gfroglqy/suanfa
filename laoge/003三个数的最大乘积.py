#在数组中找到由三个数组成的最大乘积

#普通方法
def method(x):
    x.sort()    #数组进行排序               复杂度基于排序  n*log(n)
    l = len(x)
    maxnum = max(x[0]*x[1]*x[l-1], x[l-3]*x[l-2]*x[l-1])
    return maxnum

#线性扫描
def method1(x):
    min1 = float('-inf')
    min2 = float('-inf')
    max1 = float('inf')
    max2 = float('inf')
    max3 = float('inf')

    for i in x:
        if (i < min1):
            min2 = min1
            min1 = i
        elif(i < min2):
            min2 = i
        if(i > max1):
            max3 = max2
            max2 = max1
            max1 = i
        elif(i > max2):
            max3 = max2
            max2 = i
        elif(i > max3):
            max3 = i

    return max(min2*min1*max1, max3*max2*max1)

if __name__ == "__main__":
    print(method([1, 2, 3, 4, 5, 6]))
    print(method1([1, 2, 3, 4, 5, 6]))
