#找出所有形如abc*de的算式
def method1(x):
    count = 0
    for i in range(100, 1000):
        for j in range(10, 100):
            sign = 1
            line1 = j%10*i
            line2 = int(j/10*i)
            res = i*j
            info = str(i)+str(j)+str(line1)+str(line2)+str(res)
            #print(info)
            for k in info:
                if k not in str(x):
                    sign = 0
                    break
            if sign:
                count += 1
                print('%5d\nX%4d\n-----\n%5d\n%4d\n-----\n%5d'%(i, j, line1, line2, res))
                print('The number of sulotion is:%5d\n'%count)

    return 'end'

if __name__ == '__main__':
    a = input('number:')
    print(a)
    print(method1(a))

