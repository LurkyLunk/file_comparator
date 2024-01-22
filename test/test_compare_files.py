import sys
import os
import unittest

# Add the parent directory to sys.path to find the src module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/shki/PycharmProjects/filecomparator')))

from src.compare_files import *

class TestFileComparison(unittest.TestCase):

    def test_different_contents(self):
        file1_lines = ['Apple\n', 'Cherry\n']
        file2_lines = ['Banana\n', 'Date\n']
        result = compare_files(file1_lines, file2_lines)
        self.assertEqual(result, (['Apple\n', 'Cherry\n'], ['Banana\n', 'Date\n']))

    def test_some_overlapping_lines(self):
        file1_lines = ['Apple\n', 'Banana\n']
        file2_lines = ['Banana\n', 'Cherry\n']
        result = compare_files(file1_lines, file2_lines)
        self.assertEqual(result, (['Apple\n'], ['Cherry\n']))

    def test_empty_files(self):
        file1_lines = []
        file2_lines = []
        result = compare_files(file1_lines, file2_lines)
        self.assertEqual(result, ([], []))

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
