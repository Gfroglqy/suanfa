#二分法

def method(x):
    i = -1
    left = 0
    right = x
    while(left <= right):
        mid = left + (right - left)/2
        mid = int(mid)
        if(mid * mid <= x):
            i = mid
            left = mid + 1
        else:
            right = mid - 1
    return i



#牛顿迭代
def method2(x):
    if (x == 0):
        return 0
    return int(sqrt(x, x))
## 递归子函数
def sqrt(i, x):
    res = (i + x/i)/2
    if (res == i):
        return i
    else:
        return sqrt(res, x)

if __name__ == "__main__":
    print(method(24))
    print(method2(6))