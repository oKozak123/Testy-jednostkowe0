import unittest
from zad7 import calculate_distance

class TestCalculateDistance(unittest.TestCase):

    def test_distance_positive_coordinates(self):
        #Given
        x1, y1, x2, y2 = 0, 0, 3, 4

        #When
        result = calculate_distance(x1, y1, x2, y2)

        #Then
        self.assertAlmostEqual(result, 5.0)

    def test_distance_negative_coordinates(self):
        #Given
        x1, y1, x2, y2 = -1, -2, -4, -6

        #When
        result = calculate_distance(x1, y1, x2, y2)

        #Then
        self.assertAlmostEqual(result, 5.0)

    def test_distance_mixed_coordinates(self):
        #Given
        x1, y1, x2, y2 = -1, 2, 2, -2

        #When
        result = calculate_distance(x1, y1, x2, y2)

        #Then
        self.assertAlmostEqual(result, 4.47213595499958)  # Using math.sqrt(20)

if __name__ == "__main__":
    unittest.main()
