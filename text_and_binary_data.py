import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import PIL

    return (PIL,)


@app.cell
def _(PIL):
    PIL.Image.open("6-mai.png")
    return


@app.cell
def _():
    file = open("6-mai.png", mode="rb") # "r" for "read", "b" for "binary"
    return (file,)


@app.cell
def _(file):
    file
    return


@app.cell
def _(file):
    data = file.read()
    return (data,)


@app.cell
def _(data):
    data
    return


@app.cell
def _(data):
    type(data)
    return


@app.cell
def _():
    0x89
    return


@app.cell
def _():
    print("\x89")
    return


@app.cell
def _(data):
    data[:4] == b"\x89PNG"
    return


@app.cell
def _(data):
    data[6]
    return


@app.cell
def _():
    0x1a
    return


@app.cell
def _(file):
    file.close()
    return


@app.cell
def _():
    with open("6-mai.png", mode="rb") as f:
        d = f.read(4)
        print(d == b"\x89PNG")
    return


@app.cell
def _():
    my_data = bytes([0, 255]) # ou b'\x00\xff'
    my_data
    return (my_data,)


@app.cell
def _(my_data):
    with open("my_data.raw", mode="wb") as _f:
        _f.write(my_data)
    return


@app.cell
def _():
    open("my_data.raw", mode="rb").read()
    return


@app.cell
def _():
    import os
    os.system("ls -l")
    return


@app.cell
def _():
    from plumbum.cmd import ls

    return (ls,)


@app.cell
def _(ls):
    output = ls("-l")
    print(output)
    return


@app.cell
def _():
    import pathlib

    return (pathlib,)


@app.cell
def _(pathlib):
    root = pathlib.Path(".")
    root
    return (root,)


@app.cell
def _(root):
    list(root.iterdir())
    return


@app.cell
def _(root):
    root
    return


@app.cell
def _(root):
    root.absolute()
    return


@app.cell
def _():
    "/home/boisgera/tmp/python-sandbox" + "/pixi.toml"
    return


@app.cell
def _(root):
    root / "pixi.toml"
    return


@app.cell
def _(root):
    (root / "pixi.toml").absolute()
    return


@app.cell
def _(root):
    pixi_toml = root / "pixi.toml"
    return (pixi_toml,)


@app.cell
def _(pixi_toml):
    pixi_toml.suffix
    return


@app.cell
def _(pixi_toml):
    with pixi_toml.open(mode="rb") as f_:
        print(f_.read())
    return


@app.cell
def _(pixi_toml):
    with pixi_toml.open(mode="rb") as _f:
        _data = _f.read()
        _text = _data.decode("utf-8") # TOML file (see spec.)
        print(_text)
    return


@app.cell
def _():
    import sys
    sys.getdefaultencoding()
    return


@app.cell
def _(pixi_toml):
    with pixi_toml.open(mode="rt", encoding="utf-8") as _f:
        _text = _f.read()
        print(_text)
    return


@app.cell
def _(pixi_toml):
    with pixi_toml.open() as _f:
        _text = _f.read()
        print(_text)
    return


@app.cell
def _():
    url = "https://images.unsplash.com/photo-1614642264762-d0a3b8bf3700?q=80&w=580&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    return (url,)


@app.cell
def _():
    import urllib

    return (urllib,)


@app.cell
def _(url, urllib):
    _f = urllib.request.urlopen(url)
    print(_f)
    _d = _f.read()
    print(_d) # JPEG file
    with open("sun.jpg", mode="wb") as _out:
        _out.write(_d)
    return


@app.cell
def _(PIL):
    PIL.Image.open("sun.jpg")
    return


@app.cell
def _():
    url_France = "https://fr.wikipedia.org/wiki/France"
    return (url_France,)


@app.cell
def _(url_France, urllib):
    req = urllib.request.Request(url_France, headers={
        "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0; +https://example.com/bot)"
    })
    with urllib.request.urlopen(req) as r:
        print(r.headers["Content-Type"])
        html = r.read()
        print(html)
        # print(html.decode("utf-8"))
    return (html,)


@app.cell
def _(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = a.get_text(strip=True)
        links.append((text, href))

    for text, href in links[:20]:  # first 20
        print(f"{text!r:40} → {href}")
    return


if __name__ == "__main__":
    app.run()
