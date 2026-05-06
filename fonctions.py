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
    # Fonctions variadiques
    """)
    return


@app.cell
def _():
    print()
    return


@app.cell
def _():
    print("Hello!")
    return


@app.cell
def _():
    print("Hello!", 42)
    return


@app.cell
def _():
    args = ["Hello!", 42, "is the answer"]
    return (args,)


@app.cell
def _(args):
    print(args)
    return


@app.cell
def _(args):
    print(*args)
    return


@app.function
def sum(args):
    s = 0
    for a in args:
        s = s + a
    return s


@app.cell
def _():
    sum([1, 2, 3])
    return


@app.cell
def _():
    sum([1, 2, 3, 4])
    return


@app.function
def sumv(*args):
    s = 0
    for a in args:
        s = s + a
    return s


@app.cell
def _():
    sumv(1, 2, 3)
    return


@app.cell
def _():
    sumv(1, 2, 3, 4)
    return


@app.function
def g(x, y, *args):
    print(x, y)
    print(args)


@app.cell
def _():
    g(1)
    return


@app.cell
def _():
    g(1, 2)
    return


@app.cell
def _():
    g(1, 2, 3, 4)
    return


@app.function
def h_(param1, param2, verbose=True, fast=False, debug=False):
    pass


@app.function
def h(param1, param2, **kwargs):
    print(param1, param2)
    print(kwargs)


@app.cell
def _():
    h(1, 2, verbose=True, fast=True, debug=False)
    return


@app.cell
def _():
    h(1, 2, debug=False, verbose=True, faast=True) # Ooops, coquille ...
    return


@app.cell
def _():
    h(1, 2)
    return


@app.function
def j(a, b, c):
    print(a, b, c)


@app.cell
def _():
    kwargs = {"a": "Hello", "b": 42, "c": "is the answer."}
    j(**kwargs)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Annotations de types
    """)
    return


@app.function
def add(x: int, y: int) -> int:
    return x + y


@app.cell
def _():
    add("Hello", " world!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # "Callables"
    """)
    return


@app.function
def my_fun(x, y):
    return x / y


@app.cell
def _():
    type(my_fun)
    return


@app.cell
def _():
    import types

    return (types,)


@app.cell
def _(types):
    types.FunctionType
    return


@app.cell
def _(types):
    type(my_fun) == types.FunctionType 
    return


@app.cell
def _():
    "jdksdshd\njdkskldjsskdljs\n".splitlines()
    return


@app.cell
def _(types):
    type("jdksdshd\njdkskldjsskdljs\n".splitlines) == types.FunctionType
    return


@app.cell
def _():
    int(3.14)
    return


@app.cell
def _():
    type(int)
    return


@app.cell
def _(types):
    type(int) == types.FunctionType
    return


@app.cell
def _():
    type(0)
    return


@app.cell
def _():
    type(int)
    return


@app.cell
def _():
    type(type)
    return


@app.cell
def _():
    callable(1)
    return


@app.cell
def _():
    callable(print)
    return


@app.cell
def _():
    callable("x\ny".splitlines)
    return


@app.cell
def _():
    callable(int)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fonctions dont les arguments (ou les valeurs de retour) sont des fonctions

    (Programmation d'ordre supérieure)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En Pyxel:

    ```python
    def update():
        pass

    def draw():
        pass

    pyxel.run(update, draw)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Exemple de "callback" dans une tnterface graphique : `calculate`

    ```python
    from tkinter import Tk, N, W, E, S, StringVar
    from tkinter import ttk

    root = Tk()
    root.title("Feet to Meters")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    meters = StringVar()
    ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

    def calculate(*args):
        try:
            value = float(feet.get())
            meters_value = int(0.3048 * value * 1e4 + 0.5) / 1e4
            meters.set(str(meters_value))
        except ValueError:
            pass

    ttk.Button(
        mainframe,
        text="Calculate",
        command=calculate
    ).grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    feet_entry.focus()

    root.mainloop()
    ```
    """)
    return


@app.function
def mult(x, y):
    return x * y


@app.cell
def _():
    mult(2, 3)
    return


@app.function
def mult_debug(x, y):
    print(x, y)
    z = mult(x, y)
    print(z)
    return z


@app.cell
def _():
    mult_debug(2, 3)
    return


@app.cell
def _():
    mult_debug2 = debug(mult)
    mult_debug2(2, 3)
    return


@app.function
def debug(fun):
    def debug_fun(*args):
        print(*args)
        z = fun(*args)
        print(z)
        return z
    return debug_fun


@app.function
def zoumzoum(n):
    return n + 1


@app.cell
def _():
    zoumzoum_debug = debug(zoumzoum)
    return (zoumzoum_debug,)


@app.cell
def _(zoumzoum_debug):
    zoumzoum_debug(5)
    return


@app.function
@debug
def vite_la_pause():
    return "Maintenant !"


@app.cell
def _():
    vite_la_pause()
    return


if __name__ == "__main__":
    app.run()
