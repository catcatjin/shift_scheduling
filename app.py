from flask import Flask, jsonify
from flask_cors import CORS


# Import your or-tool implementation and the function that calculates shifts
from shift_scheduling_sat import solve_shift_scheduling

app = Flask(__name__)
CORS(app)

@app.route("/api/nurse-schedule", methods=["GET"])
def get_nurse_schedule():
    shifts = solve_shift_scheduling()
    return jsonify(shifts)

if __name__ == "__main__":
    app.run(debug=True)
