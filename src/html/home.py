from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/stock_changes")
def stock_changes():
    return render_template('stock_changes.html')

@app.route("/stock_comparison")
def stock_comparison():
    return render_template('stock_comparison.html')

@app.route("/stock_regression")
def stock_regression():
    return render_template('stock_regression.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
