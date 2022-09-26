import numpy as np

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_len(self, other):
        return np.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

def Get_minlen(p, T):
    m = p.get_len(T[0])
    for t in T:
        m = min(m, p.get_len(t))
    return m

def Avg_len(P, T):
    m = 0
    for p in P:
        m += Get_minlen(p, T)
    
    return m/np.size(P)

def partial_derivate(P, T, var, dx):
    T1 = np.copy(T)
    T2 = np.copy(T)
    i = var // 2
    p = T[i]

    if var % 2 == 0:
        p1 = Point(p.x+dx, p.y)
        p2 = Point(p.x-dx, p.y)
    else:
        p1 = Point(p.x, p.y+dx)
        p2 = Point(p.x, p.y-dx)

    T1[i] = p1
    T2[i] = p2

    #print((Avg_len(P, T1)-Avg_len(P, T2))/(2*dx))

    return (Avg_len(P, T1)-Avg_len(P, T2))/(2*dx)

def Gradient(P, T, N, lr, dx):

    Tf = np.copy(T)
    for i in range(N):
        R = np.array([])
        k = 0
        for t in Tf:
            t.x -= lr * partial_derivate(P, Tf, k, dx)
            t.y -= lr * partial_derivate(P, Tf, k+1, dx)
            k += 2
            R = np.append(R, Point(t.x, t.y))
        Tf = np.copy(R)

    return Tf
        

