-- View: listings_with_details
CREATE OR REPLACE VIEW listings_with_details AS
SELECT l.id AS listing_id, l.name AS listing_name, h.name AS host_name,
       ng.name AS neighbourhood_group, n.name AS neighbourhood,
       rt.type AS room_type, l.price, l.minimum_nights, l.number_of_reviews,
       l.last_review, l.reviews_per_month, l.calculated_host_listings_count,
       l.availability_365
FROM listings l
JOIN hosts h ON l.host_id = h.id
JOIN neighbourhoods n ON l.neighbourhood_id = n.id
JOIN neighbourhood_groups ng ON n.neighbourhood_group_id = ng.id
JOIN room_types rt ON l.room_type_id = rt.id;

-- View: host_activity
CREATE OR REPLACE VIEW host_activity AS
SELECT h.id AS host_id, h.name AS host_name,
       COUNT(l.id) AS total_listings,
       AVG(l.price) AS avg_price
FROM hosts h
LEFT JOIN listings l ON h.id = l.host_id
GROUP BY h.id, h.name;

-- View: neighbourhood_summary
CREATE OR REPLACE VIEW neighbourhood_summary AS
SELECT ng.name AS neighbourhood_group, n.name AS neighbourhood,
       COUNT(l.id) AS total_listings,
       AVG(l.price) AS avg_price,
       AVG(l.availability_365) AS avg_availability
FROM neighbourhoods n
JOIN neighbourhood_groups ng ON n.neighbourhood_group_id = ng.id
LEFT JOIN listings l ON n.id = l.neighbourhood_id
GROUP BY ng.name, n.name;