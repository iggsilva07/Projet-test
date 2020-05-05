for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            igualE = n//x
            print(f'{n} e igual a {x} * {igualE}')
            break
        else:
            print(f'{n} e um numero primo')
            break