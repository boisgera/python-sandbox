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
    Types de données (bibliothèque standard):
    - `NoneType` : `None`.
    - `bool` : `True`, `False`.
    - `int` : `42`, `0`, `-1`, ...
    - `float` : `3.14`, `1.0`, `45.6e22`, ...

    - `str`: "Hello", ...

    - `tuple` : `(1, 2, 3)`, ...
    - `list`: `[1, 2, 3]`, ...
    - `dict`: `{"a": 1, "b": 2}`, ...

    - `module`: `pyxel`, `random`, `numpy`, `time`, ...
    - `function`: `draw`, `update`, ...

    - `exception`: `Exception`, `TypeError`, `ValueError`, ...

    Hors bib standard (NumPy) :

     - `float32`, `float64`,...
     - `uint8`, ...
     - `array`, ...
    """)
    return


@app.cell
def _():
    ord("A")
    return


@app.cell
def _():
    type('A')
    return


@app.cell
def _():
    'Hello' == "Hello"
    return


@app.cell
def _():
    ord("Hello")
    return


@app.cell
def _():
    type("A")
    return


@app.cell
def _():
    type("Hello")
    return


@app.cell
def _():
    type('A').__mro__
    return


@app.cell
def _():
    import random

    return (random,)


@app.cell
def _(random):
    dir(random) # Introspection
    return


@app.cell
def _(random):
    random.Random
    return


@app.cell
def _():
    help(int)
    return


@app.cell
def _():
    type(None)
    return


@app.cell
def _():
    it = iter([1, 2, 3])
    type(it)
    return (it,)


@app.cell
def _(it):
    type(it).__mro__
    return


@app.cell
def _(random):
    random
    return


@app.cell
def _():
    import pyxel
    pyxel.KEY_UP
    return (pyxel,)


@app.cell
def _(pyxel):
    type(pyxel.KEY_UP)
    return


@app.cell
def _():
    def update():
        pass
    update
    return (update,)


@app.cell
def _(update):
    type(update)
    return


@app.cell
def _():
    Exception
    return


@app.cell
def _():
    TypeError
    return


@app.cell
def _():
    TypeError.__mro__
    return


@app.function
def greet(name=None):
    if name is None:
        print("What is your name stranger?")
    else:
        print("Hello,", name)
    return None


@app.cell
def _():
    greet("Sébastien")
    return


@app.cell
def _():
    greet()
    return


@app.cell
def _():
    None
    return


@app.cell
def _():
    value = greet("Sébastien")
    value
    return (value,)


@app.cell
def _(value):
    value is None
    return


@app.cell
def _():
    _a = 1
    if _a:
        print("Trouvé !")
    return


@app.cell
def _():
    _a = None
    if _a:
        print("Trouvé !")
    return


@app.cell
def _():
    bool(None)
    return


@app.cell
def _():
    1 + 2 * 3
    return


@app.cell
def _():
    8 / 3
    return


@app.cell
def _():
    8 // 3 # division euclidienne
    return


@app.cell
def _():
    8 % 3 # modulo
    return


@app.cell
def _():
    8 == (8 // 3) * 3 + (8 % 3)
    return


@app.cell
def _():
    assert 8 == (8 // 3) * 3 + (8 % 3)
    return


@app.cell
def _():
    assert 1 == 2
    return


@app.cell
def _():
    2 ** 3 # power
    return


@app.cell
def _():
    int(5.4)
    return


@app.cell
def _():
    str(5)
    return


@app.cell
def _():
    0xff # Code hexa "ff"
    return


@app.cell
def _():
    hex(255)
    return


@app.cell
def _():
    bin(42)
    return


@app.cell
def _():
    0b101010
    return


@app.cell
def _():
    type(56) == type(-42)
    return


@app.cell
def _():
    2**10000
    return


@app.cell
def _():
    import math
    math.factorial(1000)
    return


@app.cell
def _():
    type(42.0)
    return


@app.cell
def _():
    42 == 42.0
    return


@app.cell
def _():
    3.14 + 2.0
    return


@app.cell
def _():
    3.14 + 2
    return


@app.cell
def _():
    3.0 + 2.0 == 5
    return


@app.cell
def _():
    0.1
    return


@app.cell
def _():
    0.2
    return


@app.cell
def _():
    0.1 + 0.2
    return


@app.cell
def _():
    0.1 + 0.2 == 0.3
    return


@app.cell
def _():
    _f = 0.1
    print(f"{_f:.1000}")
    return


@app.cell
def _():
    _f = 0.2
    print(f"{_f:.1000}")
    return


@app.cell
def _():
    _f = 0.1 + 0.2
    print(f"{_f:.1000}")
    return


@app.cell
def _():
    print(f"{0.1:.1000}")
    print(f"{0.2:.1000}")
    print(f"{0.1 + 0.2:.1000}")
    print(f"{0.3:.1000}")
    return


@app.cell
def _():
    _f = 0.3
    print(f"{_f:.1000}")
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    np.array
    return


@app.cell
def _(np):
    np.float32
    return


@app.cell
def _(np):
    np.float64
    return


@app.cell
def _(np):
    np.float128
    return


@app.cell
def _(np):
    # 1/10 + 2/10 en simple precision
    _f = np.float32(1) / np.float32(10) + np.float32(2) / np.float32(10)
    print(f"{_f:.10000}")
    return


@app.cell
def _(np):
    # 1/10 + 2/10 en double precision
    _f = np.float64(1) / np.float64(10) + np.float64(2) / np.float64(10)
    print(f"{_f:.10000}")
    return


@app.cell
def _(np):
    # 1/10 + 2/10 en quadruple precision
    _f = np.float128(1) / np.float128(10) + np.float128(2) / np.float128(10)
    print(f"{_f:.10000}")
    return


@app.cell
def _():
    print(f"{0.3:.1000}")
    return


@app.cell
def _(np):
    np.float128(1) / np.float128(10) + np.float128(2) / np.float128(10) == 0.3
    return


@app.cell
def _():
    x = 1e-15
    ((1.0 + x) - 1.0) / x # pas égal à 1 en pratique si x est très faible!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour aller plus loin : [ What Every Computer Scientist Should Know About Floating-Point Arithmetic ](https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf)
    """)
    return


@app.cell
def _():
    message = "Hello!"
    print(message)
    return (message,)


@app.cell
def _(message):
    message
    return


@app.cell
def _():
    'Hello!' == "Hello"
    return


@app.cell
def _():
    "J'aime les frites"
    return


@app.cell
def _():
    'J\'aime les frites'
    return


@app.cell
def _():
    "\"J'aime les frites\" dit Sébastien"
    return


@app.cell
def _():
    print("\"J'aime les frites\" dit Sébastien")
    return


@app.cell
def _():
    print("""
    "J'aime les frites" ...
    dit Sébastien,
    "et pas que!"
    """)
    return


@app.cell
def _():
    print('''
    "J'aime les frites" ...
    dit Sébastien,
    "et pas que!"
    ''')
    return


@app.cell
def _():
    print("Les frites 🍟 c'est pas mal ...")
    return


@app.cell
def _():
    ord("A")
    return


@app.cell
def _():
    ord("é")
    return


@app.cell
def _():
    ord("🍟") # unicode code point
    return


@app.cell
def _():
    0x1F35F
    return


@app.cell
def _():
    print("L'emoji des frites: \U0001F35F")
    return


@app.cell
def _():
    _name = "Sébastien"
    _age = 51
    _message = "Mon nom est " + _name + " et mon âge est " + str(_age) + "."
    print(_message)
    return


@app.cell
def _():
    _name = "Sébastien"
    _age = 51
    print(f"Mon nom est {_name} et mon âge est {_age}.") # f-strings
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Manips sur les chaines de caractères :
    - concaténation de chaines de caractères,
    - comparer (égalité, ordre "alphabétique")
    - longueur d'une de carac
    - rechercher + substitution
    - split (mots, lines, etc..)
    - parcourir / itérer
    - chaines -> code binaires
    - "slicing"
    - ...
    """)
    return


@app.cell
def _():
    "AAA" + "BBB"

    return


@app.cell
def _():
    "AAA" == "BBB"
    return


@app.cell
def _():
    "AAA" == "AAA"
    return


@app.cell
def _():
    "A" < "B"
    return


@app.cell
def _():
    "a" < "A"
    return


@app.cell
def _():
    "Hello World!".lower()
    return


@app.cell
def _():
    "Hello World!".upper()
    return


@app.cell
def _():
    l = ["Z", "X", "A", "B"]
    l.sort()
    l
    return


@app.cell
def _():
    len("Sébastien")
    return


@app.cell
def _():
    len("🍟")
    return


@app.cell
def _():
    len("\U0001F35F")
    return


@app.cell
def _():
    len("🇫🇷")
    return


@app.cell
def _():
    flag = "🇫🇷"
    flag[0]
    return (flag,)


@app.cell
def _(flag):
    flag[1]
    return


@app.cell
def _():
    name = "Sébastien"
    return (name,)


@app.cell
def _(name):
    name[0]
    return


@app.cell
def _(name):
    name[-1]
    return


@app.cell
def _(name):
    name[-2]
    return


@app.cell
def _(name):
    name[0:3]
    return


@app.cell
def _(name):
    name[1:-1]
    return


@app.cell
def _(name):
    name[:3]
    return


@app.cell
def _(name):
    name[3:]
    return


@app.cell
def _(name):
    name[:3] + name[3:]
    return


@app.cell
def _(name):
    name[::2]
    return


@app.cell
def _(name):
    name[1] = "e" # les chaines de caractères sont non modifiables !
    return


@app.cell
def _(name):
    name[:1] + "e" + name[2:]
    return


@app.cell
def _(name):
    name.replace("é", "e")
    return


@app.cell
def _():
    text = """
    sjdqlkqsjdlqskd
    ksdlsdlsjdkdsjkeywordshdsdjshdk
    hdsjkdhskd jhdks kdshsdkj
    """
    "keyword" in text
    return (text,)


@app.cell
def _(text):
    text.find("keyword")
    return


@app.cell
def _():
    _text = """
    sjdqlkqsjdlqskd
    ksdlsdlsjdkdsj keyword hdsdjshdk
    hdsjkdhskd jhdks kdshsdkj
    """
    words = _text.split()
    words
    return (words,)


@app.cell
def _(words):
    "keyword" in words
    return


@app.cell
def _():
    _text ="""
    kjlssssssssssssssssss
    sjdqlkqsjdlqskd
    ksdlsdlsjdkdsj keyword hdsdjshdk
    hdsjkdhskd jhdks kdshsdkj
    """
    newline = "\n"
    lines = _text.split(newline)
    lines
    return (lines,)


@app.cell
def _(lines):
    print("\n".join(lines))
    return


@app.cell
def _():
    _text ="""
    kjlssssssssssssssssss
    sjdqlkqsjdlqskd
    ksdlsdlsjdkdsj keyword hdsdjshdk
    hdsjkdhskd jhdks kdshsdkj
    """
    _text.splitlines()
    return


@app.cell
def _():
    for c in "Sébastien":
        print(c)
    return


@app.cell
def _():
    for _word in "J'espère qu'il y a des frites ce midi ...".split():
        print(_word) 
    return


@app.cell
def _():
    "Sébastien".encode("latin-1")
    return


@app.cell
def _():
    type("Sébastien".encode("latin-1"))
    return


@app.cell
def _():
    list("Sébastien".encode("latin-1"))
    return


@app.cell
def _():
    "Sébastien".encode("utf-8")
    return


@app.cell
def _():
    "Sébastien".encode("utf-8") == "Sébastien".encode("latin-1")
    return


@app.cell
def _():
    "Sébastien".encode("latin-1").decode("utf-8")
    return


@app.cell
def _():
    "Sébastien".encode("utf-8").decode("latin-1")
    return


if __name__ == "__main__":
    app.run()
