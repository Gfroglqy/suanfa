def answers(start, y, ans):
    num = 0
    for (i, j) in zip(ans, start):
        if i == y and i != j:
            start[num] = y
            break
        else:
            num += 1
    return start

def method1(x, y, start, ans):
    if y in x:
        if x[y]>0:
            x[y] -= 1
            start = answers(start, y, ans)
            print(start)
        else:
            print('Error！')
            return -1
    else:
        print('Error！')
        return -1
    res = all(i == 0 for i in x.values())
    #print(res)
    if res:
        return 1
    return start

def make_dict(x):
    dic = dict()
    for i in x:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

if __name__ == '__main__':
    ans = input('Computer Word:')
    start = []
    for i in range(len(ans)):
        start.append('_')
    print(start)
    dic = make_dict(ans)
    Round = 6
    while Round > 0:
        Left = Round
        print(Left, ' round left!')
        x = input('input:')
        res = method1(dic, x, start, ans)
        if res == -1:
            Round = Round + res
        elif res == 1:
            print('You win!')
            break
        else:
            start = res
    if Round == 0:
        print('You lose!')