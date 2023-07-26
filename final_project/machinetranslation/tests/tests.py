import unittest
from translator import english_to_french, french_to_english


class EnglishToFrenchTest(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertNotEqual(english_to_french("bonjour"), "hello")


class FrenchToEnglishTest(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english("bonjour"), "hello")
        self.assertNotEqual(french_to_english("hello"), "bonjour")


unittest.main()
