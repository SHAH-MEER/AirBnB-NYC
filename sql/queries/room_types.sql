-- ROOM TYPES QUERIES --

-- 1. Average Price by Room Type
SELECT room_type, AVG(price) AS avg_price
FROM listings_with_details
GROUP BY room_type;

-- 2. Room Type Popularity by Listings
SELECT room_type, COUNT(*) AS total_listings
FROM listings_with_details
GROUP BY room_type
ORDER BY total_listings DESC;

-- 3. Most Expensive Room Type (Subquery)
SELECT room_type, AVG(price) AS avg_price
FROM listings_with_details
GROUP BY room_type
HAVING AVG(price) = (
    SELECT MAX(avg_price) FROM (
        SELECT AVG(price) AS avg_price FROM listings_with_details GROUP BY room_type
    ) t
);
