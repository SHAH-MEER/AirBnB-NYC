# Data Dictionary: AirBnB NYC Raw Data

This document describes the raw data files used in this project. Each CSV corresponds to a database table.

## Files & Fields

### neighbourhood_groups.csv
| Column Name | Description                |
|-------------|----------------------------|
| id          | Unique group ID (integer)  |
| name        | Name of the group (text)   |

### neighbourhoods.csv
| Column Name           | Description                       |
|----------------------|-----------------------------------|
| id                   | Unique neighbourhood ID (integer)  |
| name                 | Name of the neighbourhood (text)   |
| neighbourhood_group_id| Foreign key to neighbourhood_groups|

### room_types.csv
| Column Name | Description                |
|-------------|----------------------------|
| id          | Unique room type ID        |
| type        | Room type (e.g., Entire, Private, Shared) |

### hosts.csv
| Column Name | Description                |
|-------------|----------------------------|
| id          | Unique host ID (integer)   |
| name        | Host name (text)           |

### listings.csv
| Column Name                   | Description                                 |
|------------------------------|---------------------------------------------|
| id                           | Unique listing ID (integer)                  |
| name                         | Listing name                                |
| host_id                      | Foreign key to hosts                        |
| neighbourhood_id              | Foreign key to neighbourhoods               |
| room_type_id                 | Foreign key to room_types                   |
| latitude, longitude          | Geographic coordinates                      |
| price                        | Price per night (integer)                   |
| minimum_nights               | Minimum nights required                     |
| number_of_reviews            | Number of reviews                           |
| last_review                  | Date of last review                         |
| reviews_per_month            | Reviews per month (float)                   |
| calculated_host_listings_count| Host's active listings count (integer)      |
| availability_365             | Days available per year                     |

### reviews.csv
| Column Name         | Description                         |
|--------------------|-------------------------------------|
| listing_id         | Foreign key to listings (integer)    |
| last_review_date   | Date of last review                  |
| number_of_reviews  | Number of reviews                    |
| reviews_per_month  | Reviews per month (float)            |
