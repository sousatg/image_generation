from PIL import Image, ImageFont, ImageDraw
from split_text import solution as split

FONT = "Ubuntu-R.ttf"

def solution(text):
    fontsize = 20

    im = Image.new('RGB', (1080, 1080))
    draw = ImageDraw.Draw(im)

    font = ImageFont.truetype(FONT, fontsize)

    while draw.textsize(text, font)[0] < 0.9 * im.size[0]:
        fontsize += 1
        font = ImageFont.truetype(FONT, fontsize)

    return fontsize


if __name__ == '__main__':
    text = split('Amar é a sabedoria dos loucos e a loucura dos sábios'.upper())
    result = solution(text)
    print(result)