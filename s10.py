FILENAME = 'nums.txt'

s = 0

with open(FILENAME, "r") as f:
    for line in f.readlines():
        line = line.strip()
        ep = line.index('=')
        num = int(line[ep+1:])
        # print(num, end=' ')
        s = s + num

print(f'sum = {s}')
