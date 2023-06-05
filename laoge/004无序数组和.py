#在数组中找到两个数，两个数和=target

#普通方法
def method(x, target):
    n = len(x)
    for i in range(n):
        for j in range(i + 1, n):
            if (x[i] + x[j] == target):
                return i, j

    return 0

#java中使用hashmap，python中使用dict
def method2(x, target):
    val = list(range(0, len(x)))
    dictmap = dict(zip(x, val))
    for i in x:
        if (dictmap.get((target - i), False)):            #使用dict.get方法，如能找到key，则返回value，否则返回False
            return (dictmap[i], dictmap[target - i])
    return 0

if __name__ == "__main__":
    print(method([1, 2, 3, 4, 5, 6], 10))
    #arr = list(range(1, 5, 2))
    print(method2([1, 2, 3, 4, 5, 6], 10))
