import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    data = """[
      "Hello!", 3, None, [1, 2, 3]
    ]
    """
    return (data,)


@app.cell
def _(data):
    obj = eval(data)
    return (obj,)


@app.cell
def _(obj):
    obj
    return


@app.cell
def _():
    str(3)
    return


@app.cell
def _():
    repr(3)
    return


@app.cell
def _():
    str(1/3)
    return


@app.cell
def _():
    repr(1/3)
    return


@app.cell
def _():
    str("Hello")
    return


@app.cell
def _():
    repr("Hello")
    return


@app.cell
def _():
    eval(str("Hello")) # meme chose que eval("Hello")
    return


@app.cell
def _():
    eval(repr("Hello"))
    return


@app.cell
def _(obj):
    obj
    return


@app.cell
def _(obj):
    repr(obj)
    return


@app.cell
def _(obj):
    eval(repr(obj)) == obj
    return


@app.cell
def _():
    import json

    return (json,)


@app.cell
def _(json, obj):
    js = json.dumps(obj)
    js
    return (js,)


@app.cell
def _(js, json):
    json.loads(js)
    return


@app.cell
def _():
    eval("1")
    return


@app.cell
def _():
    eval("a = 1; print(a)")
    return


@app.cell
def _():
    exec("a = 1; print(a)")
    return


if __name__ == "__main__":
    app.run()
