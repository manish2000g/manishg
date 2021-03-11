import unittest
import model.user


class TestUser(unittest.TestCase):
    def test_set_username(self):
        """
        it tests if set and get is working or not
    :return: whatever user sets
        """

        z = model.user.User()
        name = 'ram'
        z.set_username(name)
        y = z.get_username()
        self.assertEqual(name, y)

    def test_set_password(self):
        """
        it tests if set and get password is working or not
    :return: whatever user sets password
        """

        a = model.user.User()
        password = '12345'
        a.set_password(password)
        b = a.get_password()
        self.assertEqual(password, b)

    def test_set_address(self):
        """
        it tests if set and get address is working or not
    :return: whatever user sets an address
        """

        a = model.user.User()
        name = 'kathmandu'
        a.set_username(name)
        b = a.get_username()
        self.assertEqual(name, b)

    def test_set_gender(self):
        """
        tests if set and get gender works or not
    :return: whatever user sets gender
        """

        a = model.user.User()
        gender = 'Male'
        a.set_gender(gender)
        b = a.get_gender()
        self.assertEqual(gender, b)


if __name__ == '__main__':
    unittest.main()
