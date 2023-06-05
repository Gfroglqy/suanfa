#对于给定数组，找到其中三个长度组成的面积不为零的三角形最大周长

#贪心算法
def method1(x):
    x.sort()
    print(x)
    for i in range(len(x)-1, 1):
        print(i)
        if(x[i-1] + x[i-2] > x[i]):
            return x[i-1] + x[i-2] + x[i]

    return 0

if __name__ == '__main__':
    a = [3, 6, 2, 3]
    #a.sort()
    #print(a)
    print(method1(a))