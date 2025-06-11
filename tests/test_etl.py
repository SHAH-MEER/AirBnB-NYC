import unittest
import os
from scripts import load_etl

class TestETLConfig(unittest.TestCase):
    def test_env_vars_loaded(self):
        self.assertIsNotNone(os.getenv('DB_NAME'))
        self.assertIsNotNone(os.getenv('DB_USER'))
        self.assertIsNotNone(os.getenv('DB_PASSWORD'))
        self.assertIsNotNone(os.getenv('DB_HOST'))
        self.assertIsNotNone(os.getenv('DB_PORT'))

    def test_table_files(self):
        # Check that table_files is defined and has correct length
        self.assertTrue(hasattr(load_etl, 'table_files'))
        self.assertEqual(len(load_etl.table_files), 6)
        # Check that all expected file names are present
        expected_files = {
            'neighbourhood_groups.csv', 'neighbourhoods.csv', 'room_types.csv',
            'hosts.csv', 'listings.csv', 'reviews.csv'
        }
        actual_files = set(f for _, f in load_etl.table_files)
        self.assertTrue(expected_files.issubset(actual_files))

if __name__ == '__main__':
    unittest.main()
