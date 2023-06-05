import numpy as np

def method(n):
    x = 0
    y = n-1
    ns = 1
    matrix = np.random
    while(ns <= n*n):
        while(x<n and y>=0):
            if matrix[[x], [y]] == None:
                matrix[[x], [y]] = ns
                ns += 1
                x += 1
        while ( y > 0):
            if matrix[[x], [y-1]] == None:
                matrix[[x], [y-1]] = ns
                ns += 1
                y -= 1
        while (x > 0):
            if matrix[[x-1], [y]] == None:
                matrix[[x-1], [y]] = ns
                ns += 1
                x -= 1
        while (y<n):
            if matrix[[x], [y+1]] == None:
                matrix[[x], [y+1]] = ns
                ns += 1
                y += 1
    return matrix

if __name__ == '__main__':
    method(3)