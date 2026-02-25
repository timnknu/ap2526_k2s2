import multiprocessing as mp
import random

def place_points(nPoints):
    print('Our function is called')
    nInside = 0
    for i in range(nPoints):
        x = random.random()
        y = random.random()
        r2 = x**2 + y**2
        if r2 < 1:
            nInside += 1
    # nInside/nPoints == (pi * 1**2 / 4) / 1**2 = pi/4
    return nInside


if __name__ == '__main__':
    print('There are', mp.cpu_count(), 'cores')
    with mp.Pool(
            #processes=4
    ) as pool:         # start 4 worker processes
        nPts = [50000000 ] * 30
        print(nPts)
        result = pool.map(place_points, nPts)
        print(result)
    pi_estimate = sum(result) / sum(nPts) * 4
    print(pi_estimate)

