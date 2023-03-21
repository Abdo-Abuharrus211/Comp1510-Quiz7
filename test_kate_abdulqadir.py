import unittest
import pathlib

from kate_abdulqadir import replace_all


class TestCase(unittest.TestCase):
    def test_file_exists(self):
        path = pathlib.Path("abdo.txt")
        self.assertTrue(path.is_file())

    def test_replace_all_none(self):
        self.assertEqual(0, replace_all("kate.txt", "abdo.txt", "Cat", "Dog"))

    def test_replace_all(self):
        self.assertEqual(2, replace_all("kate.txt", "abdo.txt", "Mango", "Coconut"))

    def test_replace_all_no_search_word(self):
        self.assertEqual(0, replace_all("kate.txt", "abdo.txt", "Bob", "Coconut"))

    # def test_replace_all_position(self):
    #     char_list = list(open("abdo.txt", 'r'))
    #     replace_all("kate.txt", "abdo.txt", "Mango", "Coconut")
    #     self.assertTrue(char_list[25] == "C")
