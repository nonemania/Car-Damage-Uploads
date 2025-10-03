from flask import Flask, request, jsonify
from flask_cors import CORS
import base64, os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=False)

UPLOAD_FOLDER = "Car-Damage-Uploads/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_files():
    data = request.get_json()
    if not data or "files" not in data:
        return jsonify({"error": "No files found"}), 400

    saved_files = []
    for f in data["files"]:
        name = f.get("name", "unnamed")
        b64 = f.get("contentBase64")
        if not b64:
            continue
        file_bytes = base64.b64decode(b64)
        with open(os.path.join(UPLOAD_FOLDER, name), "wb") as out:
            out.write(file_bytes)
        saved_files.append(name)

    return jsonify({"status": "ok", "files": saved_files, "count": len(saved_files)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
