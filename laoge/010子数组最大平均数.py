#给定一个整数数组，找出平均数最大且长度为k的下标连续的子数组，并输出最大平均数

#双指针
def method(x, k):
    i = 0
    j = i + k
    sum = 0
    return sum/k

#滑动窗口
def method2(x, k):
    sum = 0
    n = len(x)
    #求窗口和，初始化sum
    for i in range(k):
        sum += x[i]
    max = sum
    for i in range(k, n):
        sum = sum - x[i - k] + x[i]
        if sum > max:
            max = sum
    return max/k



if __name__ == "__main__":
    nums1 = [1, 3, 5, 7, 9]
    k = 3
    print(method2(nums1, k))
    #arr = list(range(1, 5, 2))
    #print(method2(10))
    #print(method3(7))
