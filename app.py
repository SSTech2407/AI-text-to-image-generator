from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import base64
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
CLIPDROP_API_KEY = os.getenv("CLIPDROP_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400

    try:
        headers = {
            "x-api-key": CLIPDROP_API_KEY,
        }

        json_data = {
            "prompt": prompt
        }

        response = requests.post(
            "https://clipdrop-api.co/text-to-image/v1",
            headers=headers,
            json=json_data
        )

        if response.status_code != 200:
            return jsonify({"error": f"Clipdrop API Error: {response.text}"}), 500

        # Convert raw image content to base64
        image_data = base64.b64encode(response.content).decode("utf-8")
        return jsonify({"image": f"data:image/png;base64,{image_data}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional policy routes
@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/content")
def content():
    return render_template("content.html")

@app.route("/term")
def term():
    return render_template("term.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
