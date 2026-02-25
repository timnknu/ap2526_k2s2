import concurrent.futures
import random

def place_points(nPoints):
    print('Our function is called', nPoints)
    nInside = 0
    for i in range(nPoints):
        x = random.random()
        y = random.random()
        r2 = x**2 + y**2
        if r2 < 1:
            nInside += 1
    # nInside/nPoints == (pi * 1**2 / 4) / 1**2 = pi/4
    return (nInside, nPoints)


if __name__ == '__main__':
    nPts = [50_000, 100_000, 500_000, 1_000_000, 5_000_000, 10_000_000, 50_000_000, 100_000_000]

    all_tasks = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for n in nPts:
            task = executor.submit(place_points, n)
            print('Submitting:', task, type(task))
            all_tasks.append(task)
    print('ALL SUBMITTED')

    for future in concurrent.futures.as_completed(all_tasks):
        data = future.result()
        print('DATA:', data)
        one_nInside, one_nPoints = data
        pi_estimate = one_nInside / one_nPoints * 4
        print(one_nInside, one_nPoints, '==>', pi_estimate)
        print()

