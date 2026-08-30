from flask import Flask, render_template, jsonify

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        version=APP_VERSION
    )


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=APP_VERSION
    ), 200


@app.route("/version")
def version():
    return jsonify(
        version=APP_VERSION
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
