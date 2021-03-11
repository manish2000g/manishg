import unittest
import frontend.dashboard

class Test_dashboard(unittest.TestCase):
    def setUp(self):
        """
        function to set up the reference data for frontend.dashboard
        """
        self.a = frontend.dashboard.Function()

    def test_mergesort(self):
        """
        Function to test if the mergesort works or not.
        """
        v_id = [1, 4, 3, 2, 7, 5, 8, 6]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], self.a.mergesort(v_id))

    def test_binary_primary(self):
        """
        function to test if the binary_primary works or not
        """
        v_id = [1, 2, 3, 4, 5]
        self.assertEqual(2, self.a.binary_primary(v_id, 3))

    def tearDown(self):
        """
        function to tear down the object
        """
        del self.a

