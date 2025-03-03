from flask import Flask, render_template

app = Flask(__name__)


@app.route("/olimpiadi")
def olimpiadi():
    return render_template('olimpiadi.html')

@app.route("/olimp1")
def olimp1():
    return render_template('olimp1.html')


if __name__ == '__main__':
    app.run(debug=True)
