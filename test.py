import unittest
import main

class test_calc(unittest.TestCase):
    def test_add(self):
        result = main.add(2, 3)
        self.assertEqual(result, 5)

    def test_sub(self):
        result = main.sub(4, 1)
        self.assertEqual(result, 3)


    def test_mul(self):
        result = main.mul(4, 2)
        self.assertEqual(result, 8)



if __name__ == "__main__":
    unittest.main()