#合并两个有序数组

#双指针
def method(x, y):
    res = []
    i, j = 0, 0
    while(x != None or y != None):
        if x[i] < y[j]:
            res.append(x[i])
            x.pop(x[i])
        else:
            res.append(y[j])
            y.pop(y[j])


    return res

#暴力--b   迭代思维
def method2(x):

    return 0



if __name__ == "__main__":
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8, 10]
    print(method(nums1, nums2))
    #arr = list(range(1, 5, 2))
    #print(method2(10))
    #print(method3(7))
