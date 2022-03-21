import unittest
def append(text,append_text):
    return text + ' ' + append_text

class TestAppend(unittest.TestCase):

    def test_append(self):
        self.assertEqual(append("caio","lauro"), "caio lauro")