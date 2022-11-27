import csv
from PIL import Image, ImageDraw, ImageFont
from split_text import solution


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


with open('output/frases.csv', 'r') as fh:
    reader_csv = csv.reader(fh)
    count = 1
    for row in reader_csv:
        img = Image.new('RGB', (1080, 1080), '#F5D2B4')
        draw = ImageDraw.Draw(img)

        text = solution(row[0].strip()).upper()

        fontsize = get_font_size(img, draw, text) -1

        font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

        w, h = draw.textsize(text, font=font)

        draw.text(((1080-w) / 2,(1080-h) / 2),text=text, font=font, fill='#B46C63')
            
        img.save(f'images/img_{count}.png')
        count +=1
