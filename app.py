from PIL import Image, ImageDraw, ImageFont
import csv
from split_text import solution

with open('output/frases.csv', 'r') as fh:
    reader_csv = csv.reader(fh)
    lines = next(reader_csv)
    lines = next(reader_csv)[0]

img = Image.new('RGB', (1080, 1080), color = (73, 109, 137))
text = solution("Amar é a sabedoria dos loucos e a loucura dos sábios").upper()
fontsize = 1
img_fraction = 0.90

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)
while font.getsize(text)[0] < img_fraction*img.size[0]:
    fontsize += 1
    font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)

fontsize -= 1
font = ImageFont.truetype("Ubuntu-R.ttf", fontsize)


w, h = draw.textsize(text)

draw.text(((1080-font.getsize(text)[0]) / 2,(1080-h) / 2), text, font=font, fill=(0,0,0))
 
img.save('pil_text.png')
