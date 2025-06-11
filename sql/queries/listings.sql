-- LISTINGS QUERIES --

-- 1. Top 10 Most Expensive Listings
SELECT * FROM listings_with_details
ORDER BY price DESC
LIMIT 10;

-- 2. Listings with Above-Average Reviews
SELECT * FROM listings_with_details
WHERE number_of_reviews > (SELECT AVG(number_of_reviews) FROM listings_with_details)
ORDER BY number_of_reviews DESC;

-- 3. Listings with Price Outliers (CTE + Window Function)
WITH price_stats AS (
    SELECT price, AVG(price) OVER() AS avg_price, STDDEV(price) OVER() AS stddev_price
    FROM listings_with_details
)
SELECT * FROM listings_with_details
WHERE price > (
    SELECT avg_price + 3 * stddev_price FROM price_stats LIMIT 1
);
