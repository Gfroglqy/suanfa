class mn():
    def __init__(self, m, n):
        self.m = m
        self.n = n

def method1(x, y):
    if x > y:
        return 0
    Fenzi = 1
    Fenmu1 = 1
    Fenmu2 = 1
    for i in range(1, y+1):
        Fenzi = Fenzi * i
    for i in range(1, x+1):
        Fenmu1 = Fenmu1 * i
    for i in range(1, y-x+1):
        Fenmu2 = Fenmu2 * i
    return Fenzi/(Fenmu1*Fenmu2)

if __name__ == '__main__':
    x, y = map(int, input('m, n:').split())
    #print(x, y)
    a = mn(x, y)
    ans = method1(a.m, a.n)
    ans = int(ans)
    print(ans)
