import unittest
from ds_8 import sample_function, sleep_function

class TestTimer(unittest.TestCase):
    def test_sample_function(self):
        result, elapsed_time = sample_function(4)
        self.assertEqual(result, 16)
        self.assertTrue(elapsed_time < 1)

    def test_sleep_function(self):
        result, elapsed_time = sleep_function(2)
        self.assertEqual(result, "Спали 2 секунд")
        self.assertTrue(1.9 < elapsed_time < 2.1)

if __name__ == '__main__':
    unittest.main()