-- REVIEWS & TIME SERIES QUERIES --

-- 1. Monthly Review Trends for a Listing (example for listing_id = 1)
SELECT last_review, reviews_per_month
FROM listings_with_details
WHERE listing_id = 1
ORDER BY last_review DESC;

-- 2. Listings with Most Recent Reviews
SELECT * FROM listings_with_details
ORDER BY last_review DESC
LIMIT 10;

-- 3. Listings with No Reviews
SELECT * FROM listings_with_details
WHERE number_of_reviews = 0;

-- 4. Listings with Highest Reviews per Month (Window Function)
SELECT *,
       RANK() OVER (ORDER BY reviews_per_month DESC) AS review_rank
FROM listings_with_details
WHERE reviews_per_month IS NOT NULL
ORDER BY reviews_per_month DESC
LIMIT 10;
