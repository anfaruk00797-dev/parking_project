import unittest
from parking import calculate_fee


class TestParkingFee(unittest.TestCase):

    def test_negative_hours(self):
        self.assertEqual(calculate_fee(-1), "Invalid input")

    def test_free_parking(self):
        self.assertEqual(calculate_fee(0), 0)
        self.assertEqual(calculate_fee(2), 0)
        self.assertEqual(calculate_fee(2.0), 0)

    def test_boundary_after_free(self):
        self.assertEqual(calculate_fee(2.01), (2.01 - 2) * 20)

    def test_mid_range(self):
        self.assertEqual(calculate_fee(3), 20)
        self.assertEqual(calculate_fee(2.5), 10)
        self.assertEqual(calculate_fee(5), 60)
        self.assertEqual(calculate_fee(4.5), 50)

    def test_boundary_after_mid(self):
        self.assertEqual(calculate_fee(5.01), (3 * 20) + (5.01 - 5) * 50)

    def test_high_range(self):
        self.assertEqual(calculate_fee(6), 110)
        self.assertEqual(calculate_fee(6.5), (3 * 20) + (1.5 * 50))
        self.assertEqual(calculate_fee(10), 310)


if __name__ == "__main__":
    unittest.main()
