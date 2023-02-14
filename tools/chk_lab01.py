# Do not modify this file.  It is used by the autograder.

import unittest
import sys
import io
import os
import random

script_name = sys.argv[0]
base_name = os.path.basename(script_name)
lab_name = os.path.splitext(base_name)[0].split("_")[-1]
lab_dir = '../src/' + lab_name

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), lab_dir)))
from main import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def test_hello_world(self):
        sys.argv = ["script_name"]
        main()
        self.assertEqual(sys.stdout.getvalue().strip(), "Hello, STUST!")

    def tearDown(self):
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()
