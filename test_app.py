import marimo

__generated_with = "0.13.7"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    MIN, MAX = 0, 10
    x = [*range(MIN, MAX)]
    print(x)
    return


if __name__ == "__main__":
    app.run()
