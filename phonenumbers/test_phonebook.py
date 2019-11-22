import unittest

from phonenumbers.phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phone_book = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phone_book.add("Bob", "12345")
        number = self.phone_book.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phone_book.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phone_book.is_consistent())


if __name__ == '__main__':
    unittest.main()
