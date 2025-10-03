import requests, base64

# เลือกไฟล์ที่จะอัพโหลด
file_path = "C:\\Users\\phia\\Desktop\\Car Damage Detection\\test.jpg"

print(f"Uploading {file_path}...")  

with open(file_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")

payload = {
    "files": [
        {"name": "test.png", "type": "image/png", "contentBase64": b64}
    ]
}

res = requests.post("http://127.0.0.1:5000/upload", json=payload)
print(res.json())
print("Uploaded files:", res.json().get("files", []))