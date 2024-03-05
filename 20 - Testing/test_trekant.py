import unittest
from trekant import Trekant

class TestTrekant(unittest.TestCase):
    def setUp(self):
        self.trekant_1 = Trekant(10, 10)
        self.trekant_2 = Trekant(10, 50)

    def test_areal(self):
        self.assertEqual(self.trekant_1.areal(), 50)
        self.assertEqual(self.trekant_2.areal(), 250)

if __name__ == "__main__":
    unittest.main()
        
