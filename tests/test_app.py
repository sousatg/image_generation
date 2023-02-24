import unittest
from app import split_text


class TestSplitText(unittest.TestCase):
    def test_converting_text_with_even_number_of_words(self):
        result = split_text("This is my phrase on my python application")
        expected = "This is my phrase\non my python application"

        self.assertEqual(expected, result)
