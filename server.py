from flask import Flask, request, jsonify
from flask_cors import CORS
from sdxl import ImageGenerator


def generateImage(prompt):
    client = ImageGenerator()
    image = client.gen_image(prompt, count= 3)
    return image


app = Flask(__name__)

CORS(app, origins="*")

@app.route("/")
def generate():
    prompt = request.args.get('prompt')
    print(f'< ⌚ waiting >')
    try:
        image = generateImage(prompt)
        print("< ✔ Image generated >")
        return jsonify(image)
    except Exception as e:
        return jsonify({"status": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)