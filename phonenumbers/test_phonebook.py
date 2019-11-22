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

    def test_empty_phone_book_is_consistent(self):
        self.assertTrue(self.phone_book.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phone_book.add("Bob", "12345")
        self.phone_book.add("Anna", "012345")
        self.assertTrue(self.phone_book.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phone_book.add("Bob", "12345")
        self.phone_book.add("Sue", "12345")
        self.assertFalse(self.phone_book.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phone_book.add("Bob", "12345")
        self.phone_book.add("Sue", "123")
        self.assertFalse(self.phone_book.is_consistent())


if __name__ == '__main__':
    unittest.main()
