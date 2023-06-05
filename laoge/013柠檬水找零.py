#一杯水5美元，一次买一杯，5，10，20

#贪心算法
def method1(x):
    five = 0
    ten = 0
    for i in range(len(x)):
        if x[i] is 5:
            five += 1
        elif x[i] is 10:
            if five is 0:
                return False, five, ten
            five -= 1
            ten += 1
        if x[i] is 20:
            if ten is 0:
                if five < 3:
                    return False, five, ten
                else:
                    five -= 3
            else:
                if five < 1:
                    return False, five, ten
                else:
                    ten -= 1
                    five -= 1
    return True, five, ten

if __name__ == '__main__':
    a = [5, 5, 20, 10]
    b = [5, 5, 5, 10, 20]
    print(method1(a))
    print(method1(b))