CREATE TABLE neighbourhood_groups (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE neighbourhoods (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    neighbourhood_group_id INT REFERENCES neighbourhood_groups(id)
);

CREATE TABLE hosts (
    id BIGINT PRIMARY KEY,
    name TEXT
);

CREATE TABLE room_types (
    id SERIAL PRIMARY KEY,
    type TEXT UNIQUE NOT NULL
);

CREATE TABLE listings (
    id BIGINT PRIMARY KEY,
    name TEXT,
    host_id BIGINT REFERENCES hosts(id),
    neighbourhood_id INT REFERENCES neighbourhoods(id),
    room_type_id INT REFERENCES room_types(id),
    latitude DECIMAL,
    longitude DECIMAL,
    price INT,
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month DECIMAL,
    calculated_host_listings_count INT,
    availability_365 INT
);

CREATE TABLE reviews (
    listing_id BIGINT PRIMARY KEY REFERENCES listings(id),
    last_review_date DATE,
    number_of_reviews INT,
    reviews_per_month DECIMAL
);