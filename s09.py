import random
random.seed(42)

FILENAME = 'nums.txt'

with open(FILENAME, "w") as f:
    while True:
        rv = random.randint(1, 100)
        f.write(f'value={rv}\n')
        if rv == 100:
            break

