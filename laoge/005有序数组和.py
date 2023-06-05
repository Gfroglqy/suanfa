#在有序数组中找到两个数，两个数和=target

#利用升序特性优化   二分查找
def method(x, target):
    for i in range(len(x)):
        low = i
        high = len(x) - 1
        while(low <= high):
            mid = low + (high - low)/2
            mid = int(mid)
            if (x[mid] == target - x[i] and i != mid):     #且两下标不等
                return (i, mid)
            elif(x[mid] > target - x[i]):
                high = mid - 1
            else:
                low = mid + 1
    return 0

#双指针
def method2(x, target):
    low = 0
    high = len(x) - 1
    while(low < high):
        if (x[low] + x[high] == target):
            return [low, high]
        elif(x[low] + x[high] > target):
            high = high - 1
        else:
            low += 1
    return 0

if __name__ == "__main__":
    print(method([1, 2, 3, 4, 5, 6], 10))
    #arr = list(range(1, 5, 2))
    print(method2([1, 2, 3, 4, 5, 6], 12))
