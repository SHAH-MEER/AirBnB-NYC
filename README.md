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
├── scripts/
│   └── load_etl.py           # ETL script for loading data into PostgreSQL
├── sql/
│   ├── schema.sql            # Database schema
│   ├── views.sql             # Analytical views
│   └── queries/
│       ├── listings.sql
│       ├── hosts.sql
│       ├── neighbourhoods.sql
│       ├── room_types.sql
│       └── reviews.sql
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
