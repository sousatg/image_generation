from PIL import Image, ImageDraw, ImageFont
from split_text import solution
img = Image.new('RGB', (1080, 1080), color = (73, 109, 137))

text = solution("Amar é a sabedoria dos loucos e a loucura dos sábios").upper()

fontsize = 91 -1

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

draw.text((0,0),text=text, font=font, fill=(255,255,0))

img.save('test.png')