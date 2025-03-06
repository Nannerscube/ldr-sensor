from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Initialize lists to store Day and Night LDR values
day_values = []
night_values = []
ldr_value = 0  # Store current LDR value

@app.route("/")
def index():
    return render_template("index.html", day_values=day_values, night_values=night_values, enumerate=enumerate)

@app.route("/update_ldr", methods=["POST"])
def update_ldr():
    global ldr_value
    data = request.get_json()  # Get JSON data
    ldr_value = int(data.get("ldr", 0))  # Convert ldr_value to an int

    # Check if LDR value is for day or night
    if ldr_value > 720:
        day_values.append(ldr_value)  # Day time LDR values
    else:
        night_values.append(ldr_value)  # Night time LDR values

    return jsonify({"status": "success", "ldr": ldr_value})

@app.route("/get_ldr", methods=["GET"])
def get_ldr():
    return jsonify({"ldr": ldr_value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)