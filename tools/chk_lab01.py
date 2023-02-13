import unittest
import sys
import io
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/lab01')))
from main import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def test_hello_world(self):
        sys.argv = ["script_name"]
        main()
        self.assertEqual(sys.stdout.getvalue().strip(), "Hello, World!")

    def test_hello_name(self):
        sys.argv = ["script_name", "John"]
        main()
        self.assertEqual(sys.stdout.getvalue().strip(), "Hello, John!")

    def tearDown(self):
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()
