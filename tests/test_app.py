import unittest
from app import split_text, get_font_size
from PIL import Image, ImageDraw


class TestSplitText(unittest.TestCase):
    def test_converting_text_with_even_number_of_words(self):
        result = split_text("This is my phrase on my python application")
        expected = "This is my phrase\non my python application"

        self.assertEqual(expected, result)

    def test_converting_text_with_only_one_word(self):
        result = split_text("Lorem")
        expected = "Lorem"

        self.assertEqual(expected, result)


class TestGetFontSize(unittest.TestCase):
    def test_text_is_empty_string(self):
        img = Image.new('RGB', (1080, 1080), '#F5D2B4')
        draw = ImageDraw.Draw(img)

        self.assertRaises(Exception, get_font_size, img, draw, "")

    def test_text_with_correct_text(self):
        img = Image.new('RGB', (1080, 1080), '#F5D2B4')
        draw = ImageDraw.Draw(img)

        result = get_font_size(img, draw, "Lorem")

        self.assertEqual(335, result)