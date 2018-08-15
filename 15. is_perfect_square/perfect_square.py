import cmath
def is_perfect_square(n, **kwarg):
    """Babylonian algorithm"""

    complex = kwarg.get('complex') if kwarg.get('complex') else False

    # handling strings
    if type(n) is str: raise TypeError

    # handling 1
    if n == 1: return True

    # handling complex numbers
    if complex:
        n = cmath.sqrt(n)
        return not (n.real%1 or n.imag%1)

    # handling negative numbers
    if n < 0: return False
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

if __name__ == '__main__':
    print(is_perfect_square(100j, complex=True))
    print(is_perfect_square(-1000, complex=True))
    #print(is_perfect_square(512, complex=False))
