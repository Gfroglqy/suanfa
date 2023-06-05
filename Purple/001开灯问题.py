# p39

def method(n, k):
    a = []
    y = 1
    if n < k:
        return 0
    for i in range(n):
        a.append(0)
    for i in range(n):
        for j in range(1, k+1):
            if (i+1)%j == 0:
                if a[i] == 0:
                    a[i] = 1
                else:
                    a[i] = 0
    for i in range(n):
        if a[i] == 1:
            print(i+1)
    return 0

def method2(N, K):
    a = []
    first = 1
    for i in range(N):
        a.append(0)
    for i in range(1, K+1):
        for j in range(1, N):
            if(j%i == 0):
                if a[j] == 0:
                    a[j] = 1
                else :
                    a[j] = 0
    for i in range(1, N):
        if(a[i]):
            if first:
                first = 0
            else:
                print(" ")
                print(i)
    print("\n")
    return 0


if __name__ == '__main__':
    method(7, 3)            #   1 0 0 0 1 1 1
    #print(method2(7, 3))