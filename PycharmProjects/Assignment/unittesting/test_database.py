import unittest
import backend.dbconnection


class Test_add(unittest.TestCase):
    def setUp(self):
        """
        function to setup the reference data for backend.databaseconnection.DBConnect()
        """

        self.a = backend.dbconnection.DBConnect()

    def test_insert(self):
        """
        function to test if the insert() works or not.
        """

        query = "insert into student  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value = ('shyam', 'khatiwada', 'first year', 10126, 'shyam2@gmail.com', '12345678', '1995-10-19', 'kathmandu', 'male')
        self.a.insert(query, value)
        query1 = "select * from student where ID_No=10126"
        actual = self.a.select2(query1)
        self.assertEqual([('shyam', 'khatiwada', 'first year', 10126, 'shyam2@gmail.com', '12345678', '1995-10-19', 'kathmandu', 'male')], actual)

    def test_update(self):
        """
        function to test if the update works or not.
        """

        query = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value =('manish', 'gautam', 'first year', 10032, 'sujit22@gmail.com', '123456789', '20001019', 'kathmandu', 'male')
        self.a.insert(query, value)
        query1 = "update student set Address=%s where ID_No=%s"
        value1 = ("pokhara", 10032)
        self.a.update(query1, value1)
        query2 = "select * from student where ID_No=10032"
        actual = self.a.select2(query2)
        self.assertEqual(('manish', 'gautam', 'first year', 10032, 'sujit22@gmail.com', '123456789', '20001019', 'pokhara', 'male'), actual[0])

    def tearDown(self):
        '''
        function to tear down the object
        '''

        del self.a


if __name__ == '__main__':
    unittest.main()
