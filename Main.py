import numpy as np
import matplotlib.pyplot as plt
import Scripts as sc
import random

W = 500
H = 300
Wnum = 3
Hnum = 10
N = 5

Wsize = W/(Wnum+1)
Hsize = 20
l = int((H-2*Hsize) / Hnum)
L = int(l*3/2)

    # Calculate the points
P = np.array([])
for i in range(Wnum):
    for j in range(Hnum):
        P = np.append(P, sc.Point((i+1)*Wsize-L/2, Hsize + j*l + l/2))
        P = np.append(P, sc.Point((i+1)*Wsize+L/2, Hsize + j*l + l/2))

T = np.array([])
for i in range(N):
    x = random.uniform(Wsize, W-Wsize)
    y = random.uniform(Hsize, H-Hsize)
    T = np.append(T, sc.Point(x, y))

print(f'Distance moyenne initiale:{int(sc.Avg_len(P, T))}')

    # Calculate the Final points
Tf = sc.Gradient(P, T, 1000, 5, 1e-3)

print(f'Distance moyenne finale:{int(sc.Avg_len(P, Tf))}')

    # Draw the simulation
fig, ax = plt.subplots(figsize=(10, 10*H/W))

plt.plot([0, W, W, 0, 0], [0, 0, H, H, 0], color='black')
for i in range(Wnum):
    plt.plot([(i+1)*Wsize, (i+1)*Wsize], [Hsize, Hsize + Hnum*l], color='black')
    for j in range(Hnum + 1):
        plt.plot([(i+1)*Wsize-L, (i+1)*Wsize+L], [Hsize + j*l, Hsize + j*l], color='black')
        
for t in T:
    plt.plot(t.x, t.y, 'o', color='red')
    plt.scatter(t.x, t.y, s = 9000, alpha = .2, color = 'red')
for t in Tf:
    plt.plot(t.x, t.y, 'o', color='green')
    plt.scatter(t.x, t.y, s = 9000, alpha = .2, color = 'green')

plt.show()
