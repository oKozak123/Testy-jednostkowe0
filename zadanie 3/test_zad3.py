from unittest import TestCase
from zad3 import deserialize_product_json

class TestProductSerialization(TestCase):

    def test_successful_deserialization(self):
        # Given
        json_data = '{"id": "123e4567-e89b-12d3-a456-426614174001", "name": "Example Product", "price": 25.99}'

        # When
        result = deserialize_product_json(json_data)

        # Then
        expected_result = {'id': '123e4567-e89b-12d3-a456-426614174001', 'name': 'Example Product', 'price': 25.99}
        self.assertEqual(result, expected_result)

    def test_failed_deserialization_missing_name(self):
        # Given
        json_data = '{"id": "123e4567-e89b-12d3-a456-426614174001", "price": 25.99}'

        # When
        result = deserialize_product_json(json_data)

        # Then
        expected_result = {'error': "'name' is a required field"}
        self.assertEqual(result, expected_result)

    def test_failed_deserialization_missing_id(self):
        # Given
        json_data = '{"name": "Example Product", "price": 25.99}'

        # When
        result = deserialize_product_json(json_data)

        # Then
        expected_result = {'error': "'id' is a required field"}
        self.assertEqual(result, expected_result)

    def test_failed_deserialization_missing_price(self):
        # Given
        json_data = '{"id": "123e4567-e89b-12d3-a456-426614174001", "name": "Example Product"}'

        # When
        result = deserialize_product_json(json_data)

        # Then
        expected_result = {'error': "'price' is a required field"}
        self.assertEqual(result, expected_result)
