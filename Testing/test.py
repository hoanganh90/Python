import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_num = 10
        result = main.do_stuff(test_num)
        self.assertEqual(result, 15, f"Expected 15 but got {result} for input {test_num}") # This is a test case that checks if the function do_stuff returns the expected value
    def test_do_stuff2(self):
            test_num = "20ss"
            result = main.do_stuff(test_num)
            self.assertEqual(result,25, f"Expected 15 but got {result} for input {test_num}")
if __name__ == '__main__':
    unittest.main()  # This runs all the test cases defined in the TestMain class