import unittest
from parameterized import parameterized
from main import clean_message

class TestClean(unittest.TestCase):
    @parameterized.expand([
        ["https://www.foxite.me/?utm_source=yomama", True, "https://www.foxite.me/"],
        ["bla https://www.foxite.me/?utm_source=yomama", True, "bla https://www.foxite.me/"],
        ["bla https://www.foxite.me/?utm_source=yomama bla", True, "bla https://www.foxite.me/ bla"],
        ["bla https://www.foxite.me/?utm_source=yomama bla https://www.foxite.me/?utm_source=yomama", True, "bla https://www.foxite.me/ bla https://www.foxite.me/"],
        ["bla https://www.foxite.me/?utm_source=yomama bla https://www.foxite.me/?utm_source=yomama bla", True, "bla https://www.foxite.me/ bla https://www.foxite.me/ bla"],
        ["https://www.foxite.me/?utm_source=yomama bla https://www.foxite.me/?utm_source=yomama bla", True, "https://www.foxite.me/ bla https://www.foxite.me/ bla"],
        ["https://www.foxite.me/?utm_source=yomama https://www.foxite.me/?utm_source=yomama bla", True, "https://www.foxite.me/ https://www.foxite.me/ bla"],
        ["https://www.foxite.me/?utm_source=yomama https://www.foxite.me/?utm_source=yomama", True, "https://www.foxite.me/ https://www.foxite.me/"],
        ["https://www.foxite.me/ https://www.foxite.me/?utm_source=yomama", True, "https://www.foxite.me/ https://www.foxite.me/"],
        ["https://www.foxite.me/?utm_source=yomama https://www.foxite.me/", True, "https://www.foxite.me/ https://www.foxite.me/"],
        ["https://www.foxite.me/", False, "https://www.foxite.me/"],
        ["https://www.foxite.me/ https://www.foxite.me/", False, "https://www.foxite.me/ https://www.foxite.me/"],
    ])
    def test_plain_clean(self, input, expected_any_cleaned, expected_cleaned):
        any_cleaned, cleaned = clean_message(input)
        self.assertEqual(any_cleaned, expected_any_cleaned)
        self.assertEqual(cleaned, expected_cleaned)

if __name__ == '__main__':
    unittest.main()
