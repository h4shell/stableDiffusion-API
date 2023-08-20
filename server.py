from flask import Flask, request, jsonify
from flask_cors import CORS
from sdxl import ImageGenerator


def generateImage(data):
    client = ImageGenerator()
    image = client.gen_image(data["prompt"], int(data['count']))
    return image


app = Flask(__name__)

CORS(app, origins="*")

@app.route("/")
def generate():

    if 'count' in request.args:
        count = int(request.args.get('count'))
        if count > 4:
            count = 4
    else:
        count = 1

    prompt = request.args.get('prompt')
    data = {
        "prompt": prompt,
        "count": count
    }
    print(f'< ⌚ waiting >')
    try:
        image = generateImage(data)
        print("< ✔ Image generated >")
        return jsonify(image)
    except Exception as e:
        return jsonify({"status": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=16668)