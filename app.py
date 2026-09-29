from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "PocketSmart is running!"
    })


@app.route("/api/message", methods=["POST"])
def message():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "success": False,
            "reply": "Please enter a message."
        }), 400

    return jsonify({
        "success": True,
        "reply": f"You said: {user_message}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
