from flask import Flask, send_file, request, Response
from app import generate_image, split_text
from io import BytesIO
import time


app = Flask(__name__)


@app.route("/generate", methods=["POST"])
def generate():
    try:
        text = request.json["text"]
    except Exception as e:
        return Response(e, 400)

    if text == "":
        return Response(None, 400)

    byte_io = BytesIO()
    img = generate_image(split_text(text))
    img.save(byte_io, 'png')
    byte_io.seek(0)

    return send_file(byte_io, download_name=f"{time.time()}.png")


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port="8080")
