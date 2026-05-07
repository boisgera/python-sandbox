import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    type(1)
    return


@app.cell
def _():
    a = 1
    type(a) == int
    return


@app.cell
def _():
    type("Hello!")
    return


@app.cell
def _():
    isinstance(1, int)
    return


@app.cell
def _():
    isinstance("Hello!", int)
    return


@app.cell
def _():
    isinstance(1, object)
    return


@app.cell
def _():
    int.__mro__
    return


@app.cell
def _():
    TypeError.__mro__
    return


@app.cell
def _():
    error = TypeError("ceci n'est pas une pipe")
    return (error,)


@app.cell
def _(error):
    isinstance(error, ValueError)
    return


@app.cell
def _(error):
    isinstance(error, TypeError)
    return


@app.cell
def _(error):
    isinstance(error, Exception)
    return


@app.cell
def _(error):
    isinstance(error, object)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > Tout est objet !!!
    """)
    return


@app.cell
def _():
    def f():
        pass

    isinstance(f, object)
    return


@app.cell
def _():
    import sys

    isinstance(sys, object)
    return


@app.cell
def _():
    z = 1.0 + 2.0j
    z
    return (z,)


@app.cell
def _(z):
    [attr for attr in dir(z) if not attr.startswith("__")]
    return


@app.cell
def _(z):
    z.real
    return


@app.cell
def _(z):
    z.imag
    return


@app.cell
def _(z):
    z.conjugate
    return


@app.cell
def _(z):
    type(z.conjugate)
    return


@app.cell
def _(z):
    z.conjugate()
    return


@app.cell
def _(z):
    w = z.conjugate()
    return (w,)


@app.cell
def _(w):
    w.real, w.imag
    return


@app.cell
def _(w):
    w.conjugate()
    return


@app.cell
def _(w, z):
    z == w.conjugate()
    return


@app.cell
def _(z):
    print(z)
    return


@app.cell
def _(w, z):
    w + z
    return


@app.cell
def _(z):
    z.from_number
    return


@app.cell
def _(z):
    z.from_number(3.14)
    return


@app.cell
def _():
    abs
    return


@app.cell
def _(z):
    abs(z)
    return


@app.cell
def _(z):
    dir(z)
    return


@app.cell
def _(z):
    z.__abs__()
    return


@app.cell
def _(w, z):
    w + z
    return


@app.cell
def _(w, z):
    w.__add__(z)
    return


@app.cell
def _():
    1.0 + 2.0j
    return


@app.cell
def _():
    complex
    return


@app.cell
def _():
    type(1.0 + 2.0j) == complex
    return


@app.cell
def _():
    complex(1.0, 2.0)
    return


@app.class_definition
class Complex1:
    pass


@app.cell
def _():
    c1 = Complex1()
    type(c1) == Complex1
    return (c1,)


@app.cell
def _(c1):
    c1
    return


@app.cell
def _(c1):
    print(hex(id(c1)))
    return


@app.cell
def _(c1):
    isinstance(c1, object)
    return


@app.cell
def _(c1):
    c1 == 2
    return


@app.cell
def _(c1):
    c1.real = 1.0
    c1.imag = 2.0
    return


@app.cell
def _(c1):
    c1.real
    return


@app.cell
def _(c1):
    c1.imag
    return


@app.cell
def _(c1):
    [attr for attr in dir(c1) if not attr.startswith("__")]
    return


@app.function
def Complex1_init(c, real=0.0, imag=0.0):
    c.real = real
    c.imag = imag


@app.cell
def _():
    c2 = Complex1()
    Complex1_init(c2, 1.0, 2.0)
    c2.real
    return


@app.cell
def _():
    Complex1.init = Complex1_init
    return


@app.cell
def _():
    c3 = Complex1()
    Complex1.init(c3, 1.0, 2.0)
    c3.real
    return


@app.cell
def _():
    Complex1.__init__ = Complex1_init
    return


@app.cell
def _():
    c4 = Complex1(1.0, 2.0)
    c4.real
    return


@app.class_definition
class Complex2:
    real: float # optionnel
    imag: float # optionnel
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag


@app.cell
def _():
    c5 = Complex2(1.0, 2.0)
    c5.real
    return


@app.cell
def _():
    complex(1.0)
    return


@app.cell
def _():
    complex()
    return


@app.class_definition
class D:
    x = 0
    def __init__(d, x = None):
        if x is not None:
            d.x = x
        else:
            pass


@app.cell
def _():
    d = D(1.0)
    d.x
    return


@app.cell
def _():
    d2 = D()
    d2.x
    return (d2,)


@app.cell
def _(d2):
    d2.x = 77
    d2.x
    return


@app.cell
def _(d2):
    del d2.x
    return


@app.cell
def _(d2):
    d2.x
    return


@app.cell
def _(d2):
    D.x = 99
    d2.x = 67
    return


@app.cell
def _(d2):
    d2.x, D.x
    return


@app.cell
def _(d2):
    del d2.x
    d2.x
    return


@app.cell
def _(d2):
    d2.y = 97
    D.y
    return


@app.class_definition
class Complex3:
    real: float # optionnel
    imag: float # optionnel
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
    def conjugate(self):
        self.imag = - self.imag
        return self


@app.cell
def _():
    c0 = complex(1.0, 2.0)
    c0.conjugate()
    return (c0,)


@app.cell
def _(c0):
    c0
    return


@app.cell
def _():
    c6 = Complex3(1.0, 2.0)
    w6 = c6.conjugate()
    w6.real, w6.imag
    return (c6,)


@app.cell
def _(c6):
    c6.real, c6.imag
    return


@app.class_definition
class Complex4:
    real: float # optionnel
    imag: float # optionnel
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex4(self.real, -self.imag)


@app.cell
def _():
    c7 = Complex4(1.0, 2.0)
    w7 = c7.conjugate()
    print(w7.real, w7.imag)
    print(c7.real, c7.imag)
    return


@app.cell
def _():
    complex.from_number(1.0) # methode de classe, pas d'instance !
    return


@app.class_definition
class Complex5:
    real: float # optionnel
    imag: float # optionnel
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex5(self.real, -self.imag)
    @staticmethod
    def from_number(number):
        return Complex5(number)


@app.cell
def _():
    Complex5.from_number(9.0)
    return


@app.cell
def _():
    str("Hello")
    return


@app.cell
def _():
    repr("Hello")
    return


@app.class_definition
class Complex6:
    real: float # optionnel
    imag: float # optionnel
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
    def conjugate(self):
        return Complex5(self.real, -self.imag)
    @staticmethod
    def from_number(number):
        return Complex5(number)
    def __repr__(self):
        if self.imag >= 0:
            return f"({self.real}+{self.imag}j)"
        else:
            return f"({self.real}{self.imag}j)"
    __str__ = __repr__


@app.cell
def _():
    1.0 + 2.0j
    return


@app.cell
def _():
    c8 = Complex6(1.0, 2.0)
    c8
    return


@app.cell
def _():
    c9 = Complex6(-1.0, -2.0)
    c9
    return


@app.cell
def _():
    import math
    complex(math.nan, math.nan)
    return (math,)


@app.cell
def _(math):
    Complex6(math.nan, math.nan)
    return


@app.cell
def _():
    complex(1.0, 2.0) == complex(1.0, 2.0)
    return


@app.cell
def _():
    Complex6(1.0, 2.0) == Complex6(1.0, 2.0)
    return


@app.class_definition
class Complex7(Complex6):
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag


@app.cell
def _():
    Complex7(1.0, 2.0) == Complex7(1.0, 2.0)
    return


@app.cell
def _():
    1.0 + 0.0j == "Hi caramba!"
    return


@app.cell
def _():
    Complex7(1.0, 2.0) == "Hi caramba!"
    return


@app.cell
def _():
    complex("1.0+2.0j")
    return


@app.cell
def _(math):
    math.nan is math.nan
    return


@app.cell
def _(math):
    math.nan == math.nan # conforme à la spec IEEE 754
    return


@app.cell
def _(math):
    math.isnan(math.nan)
    return


@app.cell
def _(math):
    # Résoudre l'affichage quand z.imag est nan
    class Complex8(Complex7):
        def __repr__(self):
            if math.isnan(self.imag):
                return f"({self.real}+{self.imag}j)"
            if self.imag >= 0:
                return f"({self.real}+{self.imag}j)"
            else:
                return f"({self.real}{self.imag}j)"
        __str__ = __repr__

    return (Complex8,)


@app.cell
def _(math):
    complex(math.nan, math.nan)
    return


@app.cell
def _(Complex8, math):
    Complex8(math.nan, math.nan)
    return


@app.cell
def _(math):
    class Complex9(Complex7):
        def __repr__(self):
            if math.isnan(self.imag):
                return f"({self.real}+{self.imag}j)"
            else:
                return super().__repr__() # ou Complex7.__repr__(self)
        __str__ = __repr__

    return (Complex9,)


@app.cell
def _(Complex9):
    Complex9(1.0, -2.0)
    return


@app.cell
def _(Complex9, math):
    Complex9(math.nan, math.nan)
    return


@app.cell
def _():
    complex(1.0, 2.0).imag = 7.0
    return


@app.cell
def _(Complex9):
    c10 = Complex9(1.0, 2.0)
    c10.imag = 7.0
    c10
    return


@app.class_definition
class Int(int):
    def __repr__(self):
        return f"Int({int(self)})"
    __str__ = __repr__


@app.cell
def _():
    i = Int(56)
    return (i,)


@app.cell
def _(i):
    i
    return


@app.cell
def _(Complex9, math):
    class Complex10(Complex9):
        def get_radius(self):
            return math.sqrt(self.real ** 2 + self.imag ** 2)
        radius = property(get_radius)

    return (Complex10,)


@app.cell
def _(Complex10):
    Complex10(1.0, 2.0).get_radius()
    return


@app.cell
def _(Complex10):
    Complex10(1.0, 2.0).radius
    return


@app.cell
def _(Complex10):
    c1000 = Complex10(1.0, 2.0)
    c1000.radius = 89.0
    return


if __name__ == "__main__":
    app.run()
