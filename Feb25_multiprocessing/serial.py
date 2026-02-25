import random

nPoints = 50000000
nInside = 0
for i in range(nPoints):
    x = random.random()
    y = random.random()
    r2 = x**2 + y**2
    if r2 < 1:
        nInside += 1
# nInside/nPoints == (pi * 1**2 / 4) / 1**2 = pi/4
print(nInside/nPoints * 4)