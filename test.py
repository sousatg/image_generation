from PIL import Image, ImageDraw, ImageFont
import markovify
from split_text import solution


def generate_text():
    with open('corpus.txt', 'r') as fh:
        text = fh.read()

    text_model = markovify.Text(text)

    generated_sentence = text_model.make_short_sentence(280)
    
    return generated_sentence


class InstagramImage:
    FONT = "Ubuntu-R.ttf"
    BACKGROUND_COLOR = '#F5D2B4'
    TEXT_COLOR = '#B46C63'
    fontsize = 1

    def __init__(self, text:str):
        self.text = text
        self.img = Image.new('RGB', (1080, 1080), self.BACKGROUND_COLOR)
        self.draw = ImageDraw.Draw(self.img)

    def _generate_font(self):
        self.font = ImageFont.truetype(self.FONT, self.fontsize)

    def _calculate_font_size(self):
        self._generate_font()

        max_text_width = 0.9 * self.img.size[0]
        
        while self.draw.textsize(self.text, self.font)[0] < max_text_width:
            self.fontsize += 1
            self._generate_font()

    def calculate_text_center_position(self):
        w, h = self.draw.textsize(self.text, font=self.font)

        return ((1080-w) / 2,(1080-h) / 2)

    def save(self):
        self._calculate_font_size()
        center_position = self.calculate_text_center_position()

        self.draw.text(center_position, text=self.text, font=self.font, fill=self.TEXT_COLOR)

        self.img.save('test.png')


i_image = InstagramImage(solution(generate_text()).upper())
i_image.save()
