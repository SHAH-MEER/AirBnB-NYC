import pandas as pd
import os
from pathlib import Path

def validate_csv(path, expected_columns=None):
    df = pd.read_csv(path)
    print(f"\nValidating: {os.path.basename(path)}")
    print(f"Shape: {df.shape}")
    missing = df.isnull().sum()
    print("Missing values per column:")
    print(missing[missing > 0])
    if expected_columns:
        missing_cols = set(expected_columns) - set(df.columns)
        extra_cols = set(df.columns) - set(expected_columns)
        if missing_cols:
            print(f"Missing columns: {missing_cols}")
        if extra_cols:
            print(f"Unexpected columns: {extra_cols}")
    print("Sample data:")
    print(df.head())
    return df

if __name__ == "__main__":
    expected = {
        'neighbourhood_groups.csv': ['id', 'name'],
        'neighbourhoods.csv': ['id', 'name', 'neighbourhood_group_id'],
        'room_types.csv': ['id', 'type'],
        'hosts.csv': ['id', 'name'],
        'listings.csv': [
            'id', 'name', 'host_id', 'neighbourhood_id', 'room_type_id',
            'latitude', 'longitude', 'price', 'minimum_nights',
            'number_of_reviews', 'last_review', 'reviews_per_month',
            'calculated_host_listings_count', 'availability_365'
        ],
        'reviews.csv': ['listing_id', 'last_review_date', 'number_of_reviews', 'reviews_per_month']
    }
    data_dir = Path("data/data_clean")
    for fname, cols in expected.items():
        validate_csv(data_dir / fname, expected_columns=cols)
