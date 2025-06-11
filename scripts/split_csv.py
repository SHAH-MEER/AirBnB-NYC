import pandas as pd

# Load main Airbnb dataset
df = pd.read_csv("../data/data_raw/AB_NYC_2019.csv") 

# =============================
# 1. Neighbourhood Groups
# =============================
neighbourhood_groups = df['neighbourhood_group'].drop_duplicates().reset_index(drop=True)
neighbourhood_groups = neighbourhood_groups.reset_index().rename(columns={'index': 'id', 'neighbourhood_group': 'name'})
neighbourhood_groups.to_csv('neighbourhood_groups.csv', index=False)

# Create mapping
ng_map = dict(zip(neighbourhood_groups['name'], neighbourhood_groups['id']))

# =============================
# 2. Neighbourhoods
# =============================
df['neighbourhood_group_id'] = df['neighbourhood_group'].map(ng_map)
neighbourhoods = df[['neighbourhood', 'neighbourhood_group_id']].drop_duplicates().reset_index(drop=True)
neighbourhoods = neighbourhoods.reset_index().rename(columns={'index': 'id'})
neighbourhoods.to_csv('neighbourhoods.csv', index=False)

# Create mapping
n_map = dict(zip(zip(neighbourhoods['neighbourhood'], neighbourhoods['neighbourhood_group_id']), neighbourhoods['id']))

# =============================
# 3. Hosts
# =============================
hosts = df[['host_id', 'host_name']].drop_duplicates().rename(columns={'host_id': 'id', 'host_name': 'name'})
hosts.to_csv('hosts.csv', index=False)

# =============================
# 4. Room Types
# =============================
room_types = df['room_type'].drop_duplicates().reset_index(drop=True)
room_types = room_types.reset_index().rename(columns={'index': 'id', 'room_type': 'type'})
room_types.to_csv('room_types.csv', index=False)

# Create mapping
rt_map = dict(zip(room_types['type'], room_types['id']))

# =============================
# 5. Listings (Normalized)
# =============================
df['neighbourhood_id'] = df.apply(lambda row: n_map[(row['neighbourhood'], ng_map[row['neighbourhood_group']])], axis=1)
df['room_type_id'] = df['room_type'].map(rt_map)

listings_cols = [
    'id', 'name', 'host_id', 'neighbourhood_id', 'room_type_id',
    'latitude', 'longitude', 'price', 'minimum_nights',
    'number_of_reviews', 'last_review', 'reviews_per_month',
    'calculated_host_listings_count', 'availability_365'
]

listings = df[listings_cols]
listings.to_csv('listings.csv', index=False)


# =============================
# 6. Reviews
# =============================
# Filter rows where reviews exist (optional: remove listings with 0 reviews or no last_review)
reviews = df[df['number_of_reviews'] > 0].copy()

# Create reviews table
reviews_table = reviews[['id', 'last_review', 'number_of_reviews', 'reviews_per_month']].copy()
reviews_table = reviews_table.rename(columns={
    'id': 'listing_id',
    'last_review': 'last_review_date'
})
reviews_table.to_csv("reviews.csv", index=False)