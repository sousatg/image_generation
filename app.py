import csv
from PIL import Image, ImageDraw, ImageFont
import time

FONT = "Ubuntu-R.ttf"

def get_font_size(im: Image, draw: ImageDraw, text: str) -> int:
    """
    Based in image size and the text calculate font size
    to fill the image width
    :param im Image
    :param draw ImageDraw
    :param text str
    """
    fontsize = 1
    font = ImageFont.truetype(FONT, fontsize) 

    while draw.textsize(text, font)[0] < 0.9 * im.size[0]:
        fontsize += 1
        font = ImageFont.truetype(FONT, fontsize)

    return fontsize

def split_text(text):
    """
    Break a phrase from single line in multiple lines
    :param text str
    """
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
    """
    Given a text scale it to fit a image of 1080x1080 px and return in
    param text str
    """
    img = Image.new('RGB', (1080, 1080), '#F5D2B4')
    draw = ImageDraw.Draw(img)

    fontsize = get_font_size(img, draw, text) -1

    font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

    w, h = draw.textsize(text, font=font)

    draw.text(((1080-w) / 2,(1080-h) / 2),text=text, font=font, fill='#B46C63')

    return img



if __name__ == '__main__':
    with open('output/frases.csv', 'r') as fh:
        reader_csv = csv.reader(fh)
        for row in reader_csv:
            text = split_text(row[0].strip()).upper()
            img = generate_image(text)
            img.save(f'images/img_{time.time()}.png')
