from PIL import Image, ImageDraw, ImageFont
from split_text import solution


FONT = "Ubuntu-R.ttf"

def get_font_size(im, draw, text):
    """
    Based in image size and the text calculate font size
    to fill the image width
    :param im Image
    :param draw ImageDraw
    : param text string
    """
    fontsize = 1
    font = ImageFont.truetype(FONT, fontsize)

    while draw.textsize(text, font)[0] < 0.9 * im.size[0]:
        fontsize += 1
        font = ImageFont.truetype(FONT, fontsize)

    return fontsize

img = Image.new('RGB', (1080, 1080), '#F5D2B4')
draw = ImageDraw.Draw(img)

text = solution("O amor está em quem ama e não em quem é amado. (Platão)").upper()

fontsize = get_font_size(img, draw, text) -1

font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

w, h = draw.textsize(text, font=font)

draw.text(((1080-w) / 2,(1080-h) / 2),text=text, font=font, fill='#B46C63')

img.save('test.png')