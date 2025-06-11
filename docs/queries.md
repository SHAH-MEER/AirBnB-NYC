# SQL Queries Overview

This document describes the main analytical queries provided in the project, organized by category. See `sql/queries/` for full SQL code.

## Listings
- Top 10 most expensive listings
- Listings with above-average reviews
- Listings with price outliers (using CTE/window function)

## Hosts
- Hosts with the most listings
- Hosts with only one listing
- Host revenue estimate (using subquery)
- Hosts with listings in multiple neighbourhoods (using JOIN + CTE)

## Neighbourhoods
- Neighbourhoods with most listings
- Average price by neighbourhood
- Neighbourhoods with highest recent review growth (using CTE/window)

## Room Types
- Average price by room type
- Room type popularity by listings
- Most expensive room type (using subquery)

## Reviews & Time Series
- Monthly review trends for a listing
- Listings with most recent reviews
- Listings with no reviews
- Listings ranked by reviews per month (using window function)

Each query demonstrates best practices with joins, subqueries, CTEs, and window functions for advanced analytics.
