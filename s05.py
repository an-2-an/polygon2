def rectangle2(m, n, symbol='#', fill=True):
    print(symbol * n)
    for row in range(m-2):
        if fill:
            print(symbol * n)
        else:
            print(symbol + ' ' * (n - 2) + symbol)
    print(symbol * n)


rectangle2(m=7, n=19, symbol='+', fill=False)

