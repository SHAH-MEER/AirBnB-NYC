-- NEIGHBOURHOODS QUERIES --

-- 1. Neighbourhoods with Most Listings
SELECT neighbourhood, COUNT(*) AS total_listings
FROM listings_with_details
GROUP BY neighbourhood
ORDER BY total_listings DESC
LIMIT 10;

-- 2. Average Price by Neighbourhood
SELECT neighbourhood, AVG(price) AS avg_price
FROM listings_with_details
GROUP BY neighbourhood
ORDER BY avg_price DESC;

-- 3. Neighbourhoods with Highest Review Growth (CTE + Window)
WITH reviews_cte AS (
    SELECT neighbourhood, reviews_per_month,
           ROW_NUMBER() OVER (PARTITION BY neighbourhood ORDER BY last_review DESC) AS rn
    FROM listings_with_details
)
SELECT neighbourhood, AVG(reviews_per_month) AS avg_recent_reviews
FROM reviews_cte WHERE rn = 1
GROUP BY neighbourhood
ORDER BY avg_recent_reviews DESC
LIMIT 10;
