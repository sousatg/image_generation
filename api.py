from flask import Flask, send_file, request, Response
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import time
app = Flask(__name__)


FONT = "Ubuntu-R.ttf"

def get_font_size(im: Image, draw: ImageDraw, text: str) -> int:
    """
    Based in image size and the text calculate font size
    to fill the image width
    :param im Image
    :param draw ImageDraw
    :param text string
    """
    fontsize = 1
    font = ImageFont.truetype(FONT, fontsize) 

    while draw.textsize(text, font)[0] < 0.9 * im.size[0]:
        fontsize += 1
        font = ImageFont.truetype(FONT, fontsize)

    return fontsize

def split_text(text):
    words = text.split(' ')

    new_text = []
    count = 0
    for i in range(len(words)):
        new_text.append(words[i])
        count += 1

        if count == 4:
            count = 0
            new_text.append('\n')
        else:
            new_text.append(' ')

    return ''.join(new_text)

def generate_image(text: str):
    img = Image.new('RGB', (1080, 1080), '#F5D2B4')
    draw = ImageDraw.Draw(img)

    fontsize = get_font_size(img, draw, text) -1

    font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

    w, h = draw.textsize(text, font=font)

    draw.text(((1080-w) / 2,(1080-h) / 2),text=text, font=font, fill='#B46C63')

    return img

@app.route("/generate", methods=["POST"])
def generate():
    try:
        text = request.json["text"]
    except:
        return Response(None,400)
    
    if text == "":
        return Response(None, 400)
    
    byte_io = BytesIO()
    img = generate_image(split_text(text))
    img.save(byte_io, 'png')
    byte_io.seek(0)

    return send_file(byte_io, download_name=f"{time.time()}.png")

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port="8080")
