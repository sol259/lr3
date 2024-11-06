import unittest
from app import invert_text


class InvertTestCase(unittest.TestCase):
    def test_invert_text_success(self):
        self.assertEqual(invert_text("Sample"), "elpmaS")
        self.assertEqual(invert_text("text 123"), "321 txet")

    def test_invert_text_fail(self):
        self.assertEqual(invert_text("i have failed"), "i have failed")


if __name__ == "__main__":
    unittest.main()
