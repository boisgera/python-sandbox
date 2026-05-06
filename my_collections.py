import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - listes
    - n-uplets
    - dictionnaires
    - ensembles
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # N-uplets
    """)
    return


@app.function
def divide(a, b):
    return a // b, a % b # ou (a // b, a % b)


@app.cell
def _():
    q, r = divide(10, 3)
    return q, r


@app.cell
def _(q):
    q
    return


@app.cell
def _(r):
    r
    return


@app.cell
def _():
    pair = divide(10, 3)
    type(pair)
    return (pair,)


@app.cell
def _(pair):
    q_, r_ = pair
    return


@app.cell
def _():
    x = -1
    y = +1
    # échange ?
    tmp = x
    x = y
    y = tmp
    print(f"x = {x}, y = {y}")
    # ou
    x, y = y, x # ou (x, y) = (y, x)
    print(f"x = {x}, y = {y}")
    #
    _pair = (y, x)
    (x, y) = _pair
    print(f"x = {x}, y = {y}")
    #
    x = 1
    y = 2
    z = 3
    y, z, x = x, y, z
    print(x, y, z)

    return


@app.cell
def _():
    l = [0.0, 100.0]
    l[1] = 99.0
    l
    return


@app.cell
def _():
    _t = (0.0, 99.0)
    _t[1] = 100.0
    return


@app.cell
def _():
    _t = (0.0, 100.0)
    #_t[1] = 99.0
    _s = (_t[0], 99.0)
    _s
    return


@app.cell
def _():
    _t = (0.0, 100.0)
    _l = list(_t)
    _l[1] = 99.0
    _t = tuple(_l)
    print(_t)
    return


@app.cell
def _():
    _t = (1, 2, 3)
    return


@app.cell
def _():
    _t = ()
    type(_t)
    return


@app.cell
def _():
    len(())
    return


@app.cell
def _():
    _t = (1 + 1)
    type(_t)
    return


@app.cell
def _():
    _t = ((2))
    type(_t)
    return


@app.cell
def _():
    _t = (
        1, 
        2, 
        3, 
        4, 
        5, 
        6, 
        7, 
        8, 
        9, 
        10,
    )
    return


@app.cell
def _():
    _t = (1, 2, 3,)
    return


@app.cell
def _():
    _t = (1,)
    type(_t)
    return


@app.cell
def _():
    _t = (
        1,
        2,
        3,
    )
    return


@app.cell
def _():
    _t = ((()))
    len(_t)
    return


@app.cell
def _():
    tuple([1]) == (1,)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dictionnaires
    """)
    return


@app.cell
def _():
    d = {"zero": 0, "un": 1, "deux": 2}
    d
    return (d,)


@app.cell
def _(d):
    d["zero"]
    return


@app.cell
def _(d):
    d["trois"] = 3
    d
    return


@app.cell
def _(d):
    d["quatre"]
    return


@app.cell
def _(d):
    d.get("trois")
    return


@app.cell
def _(d):
    d.get("quatre") is None
    return


@app.cell
def _(d):
    d.get("zozo", -1) == -1
    return


@app.cell
def _(d):
    d
    return


@app.cell
def _(d):
    d.update({"quatre": 4, "cinq": 5})
    d
    return


@app.cell
def _():
    {"a":1, "b": 2}
    return


@app.cell
def _():
    {"b": 2, "a": 1}
    return


@app.cell
def _():
    {"a": 1, "b": 2} == {"b": 2, "a": 1}
    return


@app.cell
def _(d):
    for elt in d:
        print(elt)
    return


@app.cell
def _(d):
    for key in d:
        print(key, d[key])
    return


@app.cell
def _(d):
    for _pair in d.items():
        print(_pair)
    return


@app.cell
def _(d):
    for val in d.values():
        print(val)
    return


@app.cell
def _(d):
    list(d)
    return


@app.cell
def _():
    succ = {}
    for i in range(10):
        succ[i] = i + 1
    print(succ)
    return


@app.cell
def _():
    nd = {0.1: "a", 0.2: "b"}
    return (nd,)


@app.cell
def _(nd):
    type(list(nd)[0])
    return


@app.cell
def _():
    omg_d = {0: "entier zéro", 0.0: "réel zéro", False: "faux"}
    print(omg_d)
    return


@app.cell
def _():
    0 == False
    return


@app.cell
def _():
    0 == 0.0
    return


@app.cell
def _():
    #d[3] = "trois"
    #d
    return


@app.cell
def _():
    record = {("Sébastien", 51) : "Sebastien.Boisgerault@minesparis.psl.eu"}
    print(record)
    return


@app.cell
def _():
    _record = {["Sébastien", 51] : "Sebastien.Boisgerault@minesparis.psl.eu"}
    print(_record)
    return


@app.cell
def _():
    hash(("Sébastien", 51))
    return


@app.cell
def _():
    immutable = ([1], [2], [3])
    print(immutable)
    return (immutable,)


@app.cell
def _(immutable):
    _l = immutable[0]
    _l[0] = 999
    print(immutable)
    return


@app.cell
def _():
    _l = [1, 2, 3]
    _s = _l.copy()
    _s.append(4)
    print(_l, _s)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Ensembles
    """)
    return


@app.cell
def _():
    {1, 2, 3}
    return


@app.cell
def _():
    set([1, 2, 3])
    return


@app.cell
def _():
    print(list(set([1, 3, 4, 2, 2, 1, 4, 2])))
    return


@app.cell
def _():
    type({}) # None? ens. vide.? Dict. vide?
    return


@app.cell
def _():
    set()
    return


@app.cell
def _():
    set([])
    return


@app.cell
def _():
    for _elt in {6, 7, 88, 2}:
        print(_elt)
    return


@app.cell
def _():
    {6, 7, 88, 2} == {88, 2, 6, 7}
    return


@app.cell
def _():
    7 in {6, 7, 88, 2}
    return


@app.cell
def _():
    "caramba" in {6, 7, 88, 2}
    return


@app.cell
def _():
    {[1], [2], [3]}
    return


@app.cell
def _():
    "a" == "A"
    return


@app.cell
def _():
    {"a", "A"}
    return


@app.cell
def _():
    {0, 0.0, False}
    return


@app.cell
def _():
    {0, 0, 0}
    return


@app.cell
def _():
    0.1 + 0.2 == 0.3
    return


@app.cell
def _():
    {0.1 + 0.2, 0.3}
    return


@app.cell
def _():
    s1 = {0, 1, 2, 3}
    s2 = {2, 3, 4, 5}
    return s1, s2


@app.cell
def _(s1, s2):
    s1 | s2 # union de s1 et s2
    return


@app.cell
def _(s1, s2):
    s1 & s2 # intersection de s1 et s2
    return


@app.cell
def _(s1, s2):
    s1 - s2 # difference de s1 et s2
    return


@app.cell
def _(s1, s2):
    s1 ^ s2 # xor / difference symmétrique
    return


@app.cell
def _():
    0b11111100 & 0b00000011 # et "bit-à-bit"
    return


@app.cell
def _():
    0b11111100 and 0b00000011 # et logique
    return


@app.cell
def _():
    0b11111100 | 0b00000011
    return


@app.cell
def _():
    0b11111111
    return


@app.cell
def _():
    0b11111100 ^ 0b00000011
    return


@app.cell
def _():
    ~0b11111100 # bitwise not (two's complement)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # "Compréhensions"
    """)
    return


@app.function
def is_prime(n):
    if n < 0:
        raise ValueError("Negative arguments not accepted")
    if n == 0 or n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


@app.cell
def _():
    is_prime(-7)
    return


@app.cell
def _():
    is_prime(0)
    return


@app.cell
def _():
    is_prime(1)
    return


@app.cell
def _():
    is_prime(2)
    return


@app.cell
def _():
    is_prime(7)
    return


@app.cell
def _():
    is_prime(8)
    return


@app.cell
def _():
    numbers = range(100)
    return (numbers,)


@app.cell
def _(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    prime_numbers    
    return


@app.cell
def _():
    [n for n in range(100) if is_prime(n)] # "filter"
    return


@app.cell
def _():
    square_numbers = []
    for _n in range(10):
        square_numbers.append(_n ** 2)
    square_numbers
    return


@app.cell
def _():
    [n ** 2 for n in range(10)] # "map"
    return


@app.cell
def _():
    print([n ** 2 for n in range(10) if is_prime(n)]) # "filter" + "map"
    return


@app.cell
def _():
    print({n ** 2 for n in range(10) if is_prime(n)}) # "filter" + "map"
    return


@app.cell
def _():
    print([n // 2 for n in range(10)])
    return


@app.cell
def _():
    print({n // 2 for n in range(10)})
    return


@app.cell
def _():
    print({
        n : n ** 2 for n in range(10) if is_prime(n)
    }) # "filter" + "map"
    return


@app.cell
def _():
    list(filter(is_prime, range(10)))
    return


@app.cell
def _():
    return


@app.function
def is_even(n):
    return n % 2 == 0


@app.cell
def _():
    filter(is_even, range(10))
    return


@app.cell
def _():
    list(filter(is_even, range(10)))
    return


@app.cell
def _():
    list(filter(lambda n: n % 2 == 0, range(10)))
    return


@app.cell
def _():
    is_even_2 = lambda n: n % 2 == 0
    type(is_even_2)
    return (is_even_2,)


@app.cell
def _(is_even_2):
    is_even_2(7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Expression génératrices
    """)
    return


@app.cell
def _():
    for _i in [n for n in range(100) if is_prime(n)]:
        print(_i)
    return


@app.cell
def _():
    for _i in (n for n in range(100) if is_prime(n)):
        print(_i)
    return


@app.cell
def _():
    genexpr = (n for n in range(100) if is_prime(n))
    type(genexpr)
    return (genexpr,)


@app.cell
def _(genexpr):
    genexpr
    return


@app.cell
def _(genexpr):
    it = iter(genexpr)
    it
    return (it,)


@app.cell
def _(it):
    next(it)
    return


@app.cell
def _(it):
    next(it)
    return


@app.cell
def _(it):
    next(it)
    return


@app.cell
def _():
    max([n for n in range(100) if is_prime(n)])
    return


@app.cell
def _():
    max(n for n in range(100) if is_prime(n))
    return


@app.cell
def _():
    max
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Functions génératrices
    """)
    return


@app.function
def f():
    yield 1
    yield 2
    yield 3


@app.cell
def _():
    for _elt in f():
        print(_elt)
    return


@app.function
def forever(start=0):
    while True:
        yield start
        start = start + 1


@app.cell
def _():
    for _elt in forever(10):
        if _elt == 20:
            break
        print(_elt)
    return


@app.function
def primes():
    n = 0
    while True:
        if is_prime(n):
            yield n
        n = n + 1


@app.cell
def _():
    prime_it = primes()
    return (prime_it,)


@app.cell
def _(prime_it):
    next(prime_it)
    return


@app.cell
def _(prime_it):
    next(prime_it)
    return


@app.cell
def _():
    for _elt in primes():
        if _elt > 20:
            break
        print(_elt)
    return


@app.cell
def _():
    1 == 1
    return


@app.cell
def _():
    a = None
    a is None
    return


@app.cell
def _():
    b = False
    b == 0
    return (b,)


@app.cell
def _(b):
    b is 0
    return


@app.cell
def _():
    1 == 1
    return


@app.cell
def _():
    1 is 1
    return


@app.cell
def _():
    10 is 10
    return


@app.cell
def _():
    2**100 is 2**100
    return


if __name__ == "__main__":
    app.run()
