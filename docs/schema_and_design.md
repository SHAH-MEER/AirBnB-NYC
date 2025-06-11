# Database Schema & Design

This document explains the relational schema and design decisions for the AirBnB NYC project.

## Entity-Relationship Diagram (ERD)
- **neighbourhood_groups** (1) --- (M) **neighbourhoods**
- **neighbourhoods** (1) --- (M) **listings**
- **hosts** (1) --- (M) **listings**
- **room_types** (1) --- (M) **listings**
- **listings** (1) --- (1) **reviews**

## Table Descriptions
- **neighbourhood_groups**: Top-level grouping for neighbourhoods.
- **neighbourhoods**: City areas, each belonging to a group.
- **hosts**: People offering listings.
- **room_types**: Types of rooms offered (Entire, Private, Shared, etc).
- **listings**: Main table for AirBnB properties, with references to hosts, neighbourhoods, and room types.
- **reviews**: Aggregated review stats for each listing.

## Design Notes
- Foreign keys enforce referential integrity.
- Surrogate primary keys (id) for all main tables.
- reviews is 1:1 with listings (can be split to 1:N for detailed reviews if needed).
- Data types chosen for clarity and performance (e.g., integers for IDs, text for names, decimals for prices).
