import unittest

from phonenumbers.phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_lookup_by_name(self):
        phone_book = PhoneBook()
        phone_book.add("Bob", "12345")
        number = phone_book.lookup("Bob")
        self.assertEqual("12345", number)


if __name__ == '__main__':
    unittest.main()
