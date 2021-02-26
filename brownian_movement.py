import numpy as np
import matplotlib.pyplot as plt

def step():
    l = 1
    if np.random.rand() < 0.5: l = -1 #the chances of either a "step" to the left or one to the right is 50-50
    return l

#path for 1 particle
N = 2000
path = []
x = 0
path += [x]

for n in range(N):
    x += step()
    path += [x]


#distribution for M = 1000 particles after n steps
M = 1000
xArray = [] # 1 x 1000
for m in range(M):
    x = 0
    for n in range(N):
        x += step()
    xArray += [x]
xArray = np.array(xArray)
print('mean = ', xArray.mean(), ' std = ', xArray.std(), 'sqrt(N) = ', N**0.5)

plt.hist(xArray, bins = range(-60, 61))
#plt.plot(path)
plt.show()

#2D brownian movement
def step_2D():
    l = 1 +0j
    U = np.random.rand()
    if U < 0.25: l = -1 +0j
    if 0.25 <= U < 0.5: l = 0 +1j #we use imaginary numbers for the values of a "step" up or one down
    if 0.5 <= U < 0.75: l = 0 -1j
    return l
#distribution for M = 1000 particles after n steps
M = 1000
N = 100
xArray = []
yArray = []
r = []
Σr = 0
Σr2 = 0
for m in range(M):
    x = 0
    y = 0
    for n in range(N):
        h = step_2D()
        r += [h]
        Σr += h
        Σr2 += h*h
        if h == 1 or h == -1:
            x += h
        else:
            y += (h)**2
    xArray += [x]
    yArray += [y]
rArray = np.array(r)
print('mean = ', rArray.mean(), ' std = ', rArray.std(), 'sqrt(N) = ', N**0.5)
mr = Σr/N
sr = Σr2/N - mr*mr
print('mean = ', mr, ' std = ', sr, 'sqrt(N) = ', N**0.5)

plt.scatter(xArray,yArray)
plt.show()
