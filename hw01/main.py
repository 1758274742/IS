for a in range(1,10):
    for b in range(1,a):
        print(end='       ')
    for c in range(a,10 ):
        print('{}*{}={:<2}'.format(a, c, a*c),end=' ')
    print()
