def method1(p, d, t):
    #print(n, k, m)
    while t:
        p = (p+d)%n
        t -= 1
        if List[p] == 0:
            t += 1
    return p

if __name__ == '__main__':
    n, k, m = map(int, input('n, k, m = ').split(','))
    left = n
    List = []
    for i in range(1, n+1):
        List.append(i)
    print(List)
    p1 = n
    p2 = 1

    while left:
        p1 = method1(p1, 1, k)
        p2 = method1(p2, -1, m)
        print(p1)
        left -= 1
        if p2 != p1:
            print(p2)
            left -= 1
        List[p1] = List[p2] = 0
        print(",")


