-- HOSTS QUERIES --

-- 1. Hosts with the Most Listings
SELECT host_name, COUNT(*) AS total_listings
FROM listings_with_details
GROUP BY host_name
ORDER BY total_listings DESC
LIMIT 10;

-- 2. Hosts with Only One Listing
SELECT host_name
FROM host_activity
WHERE total_listings = 1;

-- 3. Host Revenue Estimate (Subquery)
SELECT host_name, total_listings * avg_price AS estimated_revenue
FROM host_activity
ORDER BY estimated_revenue DESC;

-- 4. Hosts with Listings in Multiple Neighbourhoods (JOIN + CTE)
WITH host_neigh AS (
    SELECT h.host_id, h.host_name, COUNT(DISTINCT n.neighbourhood) AS neighbourhood_count
    FROM listings_with_details l
    JOIN host_activity h ON l.host_id = h.host_id
    JOIN neighbourhoods n ON l.neighbourhood_id = n.id
    GROUP BY h.host_id, h.host_name
)
SELECT * FROM host_neigh WHERE neighbourhood_count > 1;
