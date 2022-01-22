import random

FILENAME = 'random_process.txt'

e, n = 10 ** -6, 0

for _ in range(10):
    with open(FILENAME, "a") as f:
        while True:
            rv = random.random()
            n = n + 1
            if rv < e:
                print(f'Done. n={n}, rv={rv:.9f}')
                f.write(f'Done. n={n}, rv={rv:.9f}\n')
                break