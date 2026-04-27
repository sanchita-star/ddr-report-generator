from flask import Flask, request, jsonify
from flask_cors import CORS
from extractor import extract_text_from_pdf, extract_observations
from merger import merge_data
from generator import generate_ddr

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    try:
        inspection_file = request.files.get("inspection")
        thermal_file = request.files.get("thermal")

        inspection_text = extract_text_from_pdf(inspection_file) if inspection_file else ""
        thermal_text = extract_text_from_pdf(thermal_file) if thermal_file else ""

        inspection_data = extract_observations(inspection_text)
        thermal_data = extract_observations(thermal_text)

        merged = merge_data(inspection_data, thermal_data)

        report = generate_ddr(merged)

        return jsonify({"report": report})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)