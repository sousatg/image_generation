import csv
from PIL import Image, ImageDraw, ImageFont
import time

FONT = "Ubuntu-R.ttf"
IMAGE_WIDTH = 1080
IMAGE_HEIGHT = 1080


def get_font_size(im: Image, draw: ImageDraw, text: str) -> int:
    """
    Based in image size and the text calculate font size
    to fill the image width
    :param im Image
    :param draw ImageDraw
    :param text str
    """
    if text == "":
        raise Exception("Text parameter can't be empty")

    fontsize = 1
    font = ImageFont.truetype(FONT, fontsize)

    ninety_percent_of_image_width = 0.9 * im.size[0]
    while draw.textsize(text, font)[0] < ninety_percent_of_image_width:
        fontsize += 1
        font = ImageFont.truetype(FONT, fontsize)

    return fontsize


def split_text(text: str) -> str:
    """
    Break a phrase from single line in multiple lines
    :param text str
    """
    count = 0
    for i in range(len(text)):
        if text[i] == " ":
            count += 1

        if count == 4:
            text = text[:i] + "\n" + text[i+1:]
            count = 0

    return text


def generate_image(text: str):
    """
    Given a text scale it to fit a image of 1080x1080 px and return in
    param text str
    """
    img = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), '#F5D2B4')
    draw = ImageDraw.Draw(img)

    fontsize = get_font_size(img, draw, text) - 1

    font = ImageFont.truetype(FONT, fontsize)

    w, h = draw.textsize(text, font=font)

    image_center_tuple = ((IMAGE_WIDTH-w) / 2, (IMAGE_HEIGHT-h) / 2)
    draw.text(
        image_center_tuple,
        text=text,
        font=font,
        fill='#B46C63')

    return img


if __name__ == '__main__':
    with open('output/frases.csv', 'r') as fh:
        reader_csv = csv.reader(fh)
        for row in reader_csv:
            text = split_text(row[0].strip()).upper()
            img = generate_image(text)
            img.save(f'images/img_{time.time()}.png')
