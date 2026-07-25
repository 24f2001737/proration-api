from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/proration", methods=["POST"])
def proration():
    data = request.get_json()

    old_price = data["old_price"]
    new_price = data["new_price"]
    days_remaining = data["days_remaining"]
    spec = data["spec"]

    if spec == "v1":
        divisor = 30
    elif spec == "v2":
        divisor = data["days_in_actual_month"]
    else:
        return jsonify({"error": "Invalid spec"}), 400

    charge = (new_price - old_price) * (days_remaining / divisor)

    return jsonify({"charge": charge})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
