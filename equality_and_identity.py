import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import copy

    return (copy,)


@app.cell
def _():
    message = "Hello!"
    return (message,)


@app.cell
def _(message):
    text = message # nouvelle reference (oui) ou copie de l'objet (non) ?
    return (text,)


@app.cell
def _(message, text):
    text == message
    return


@app.cell
def _(message, text):
    text is message
    return


@app.cell
def _(copy, message):
    text2 = copy.copy(message)
    return (text2,)


@app.cell
def _(message, text2):
    text2 is message # Oups, en fait la copie ne sert a rien,
    # les chaines de caractères sont non-modifiables !
    return


@app.cell
def _():
    l = [1, 2, 3]
    return (l,)


@app.cell
def _(l):
    l2 = l # Pas de copie implicite !
    return (l2,)


@app.cell
def _(l2):
    l2[0] = 99
    l2
    return


@app.cell
def _(l):
    l
    return


@app.cell
def _(copy):
    l3 = [1, 2, 3]
    l_copy = copy.copy(l3)
    l_copy
    return l3, l_copy


@app.cell
def _(l, l_copy):
    l == l_copy
    return


@app.cell
def _(l, l_copy):
    l is l_copy
    return


@app.cell
def _(l_copy):
    l_copy[0] = -1
    l_copy
    return


@app.cell
def _(l3):
    l3
    return


@app.cell
def _():
    l_nested = [[0], [0, 1], [0, 1, 2]]
    return (l_nested,)


@app.cell
def _(l_nested):
    id(l_nested) # adresse en mémoire de l_nested
    return


@app.cell
def _(l_nested):
    print(hex(id(l_nested)))
    return


@app.cell
def _(l_nested):
    l_nested_2 = l_nested
    return (l_nested_2,)


@app.cell
def _(l_nested_2):
    id(l_nested_2)
    return


@app.cell
def _(copy, l_nested):
    l_nested_3 = copy.copy(l_nested)
    id(l_nested_3)
    return (l_nested_3,)


@app.cell
def _(l_nested_3):
    l_nested_3
    return


@app.cell
def _(l_nested):
    l_nested[0]
    return


@app.cell
def _(l_nested_3):
    l_nested_3[0]
    return


@app.cell
def _(l_nested, l_nested_3):
    l_nested[0] is l_nested_3[0] # copie superficielle
    return


@app.cell
def _(copy, l_nested):
    l_nested_4 = copy.deepcopy(l_nested) # copie en profondeur
    return (l_nested_4,)


@app.cell
def _(l_nested, l_nested_4):
    l_nested_4 is l_nested
    return


@app.cell
def _(l_nested, l_nested_4):
    l_nested_4[0] is l_nested[0]
    return


@app.function
def display(x = []):
    print(x)
    x.append(1)


@app.cell
def _():
    x = [1, 0, 0]
    display(x)
    display(x)
    display(x)
    return


@app.cell
def _():
    display()
    return


@app.cell
def _():
    display()
    return


@app.function
def display_alt(x = None):
    if x is None:
        x = []
    print(x)
    x.append(1)


@app.cell
def _():
    display_alt()
    return


@app.cell
def _():
    display_alt()
    return


@app.cell
def _():
    import sys
    sys.getsizeof(42)
    return (sys,)


@app.cell
def _(sys):
    sys.getsizeof(['A', 'B', 'C'])
    return


@app.cell
def _(sys):
    sys.getsizeof(['A', 'B', 'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'])
    return


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _(np):
    a = np.arange(10_000, dtype=np.uint8)
    a
    return (a,)


@app.cell
def _(a, sys):
    sys.getsizeof(a)
    return


if __name__ == "__main__":
    app.run()
