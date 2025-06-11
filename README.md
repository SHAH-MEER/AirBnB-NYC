# AirBnB-NYC

A comprehensive data engineering and analytics project exploring New York City AirBnB data. Built and maintained by [SHAH-MEER](https://github.com/SHAH-MEER).

---

## Project Overview

This project provides a robust pipeline for cleaning, storing, querying, and visualizing AirBnB data for New York City. It leverages PostgreSQL for relational storage, Python for ETL and analysis, and Jupyter/Seaborn for rich exploratory data analysis (EDA).

**Key Features:**
- Cleaned and well-documented AirBnB NYC dataset
- Automated ETL pipeline using Python and SQL
- Relational database schema with strong referential integrity
- Modular SQL queries and analytical views for advanced insights
- Ready-to-use Jupyter notebook for EDA and visualization
- Professional documentation for data, schema, and analytics

---

## Folder Structure

```
AirBnB-NYC/
├── data/
│   └── data_clean/           # Cleaned CSVs for DB loading
├── docs/                     # Data dictionary, schema, and query docs
├── notebooks/
│   └── ExploratoryDataAnalysis.ipynb  # Main EDA notebook
├── visualisations/               # Saved plots from EDA notebook
├── scripts/
│   └── load_etl.py           # ETL script for loading data into 
├── sql/
│   ├── schema.sql            # Database schema
│   ├── views.sql             # Analytical views
│   └── queries/
│       ├── listings.sql
│       ├── hosts.sql
│       ├── neighbourhoods.sql
│       ├── room_types.sql
│       └── reviews.sql
├── tests/
│   └── test_etl.py           # ETL unit tests
├── .env                      # Environment variables (not tracked in git)
├── .gitignore
├── README.md
└── ...
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/SHAH-MEER/AirBnB-NYC.git
cd AirBnB-NYC
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install psycopg2-binary sqlalchemy python-dotenv jupyter seaborn pandas
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=airbnb_nyc
DB_USER=your_user
DB_PASSWORD=your_password
```

### 4. Load Data into PostgreSQL
Run the ETL script:
```bash
python scripts/load_etl.py
```

### 5. Run Analyses and Visualizations
Start Jupyter and open the EDA notebook:
```bash
jupyter notebook notebooks/ExploratoryDataAnalysis.ipynb
```

All generated plots and charts will be saved in the `visualisations/` folder for easy access and sharing.

---

## Data Validation & Testing

### Data Validation
Check your cleaned CSVs for missing values, schema mismatches, and column issues before loading to the database:

```bash
python scripts/data_validation.py
```

### ETL Unit Tests
Ensure your ETL configuration and table mapping are correct:

```bash
python -m unittest tests/test_etl.py
```

---

## Data Sources
- NYC AirBnB open data (see `docs/data_dictionary.md` for details)
- All data is cleaned and stored in `data/data_clean/`

---

## Documentation
- **Data Dictionary:** [`docs/data_dictionary.md`](docs/data_dictionary.md)
- **Schema & Design:** [`docs/schema_and_design.md`](docs/schema_and_design.md)
- **Query Reference:** [`docs/queries.md`](docs/queries.md)

---

## Contributing
Pull requests and issues are welcome! Please open an issue for major changes.

---

## License
This project is for educational and portfolio use. See `LICENSE` for more details.

---

## Author & Contact
- GitHub: [SHAH-MEER](https://github.com/SHAH-MEER)
- Email: shahmeershahzad67@gmail.com

---

## Suggestions for Project Improvement

- **Automated Data Validation:** Add scripts to check data quality, missing values, and schema mismatches before loading to the database.
- **Unit Tests:** Implement tests for ETL scripts and data transformations to ensure reliability.
- **Dockerization:** Create a Dockerfile and docker-compose setup for easy, reproducible deployment of the database and ETL pipeline.
- **CI/CD Integration:** Set up GitHub Actions or similar for automated testing and deployment.
- **Interactive Dashboards:** Add a dashboard (e.g., Streamlit, Dash, or Tableau Public) for interactive data exploration.
- **Granular Reviews Table:** Expand the reviews table to store one row per review for deeper text and time-series analysis.
- **Geospatial Analysis:** Integrate with mapping libraries (e.g., Folium, Plotly) for advanced spatial visualizations.
- **Performance Optimization:** Add indexes on frequently queried columns and analyze slow queries.
- **API Layer:** Expose key queries and analytics via a REST API (e.g., using FastAPI or Flask).
- **User Documentation:** Add tutorial notebooks and more sample queries for new users.
