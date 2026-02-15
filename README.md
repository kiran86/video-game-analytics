# Video Game Sales and Engagement Analytics

## Project Overview
A comprehensive data analytics project that integrates video game **sales data** with **user engagement metrics** to identify market trends, platform performance, and genre success patterns. This project demonstrates end-to-end data engineering and business intelligence workflows—from raw data ingestion to interactive dashboard development.

## Domain
Gaming & Entertainment Analytics

## Key Insights Delivered
- Regional and global sales trends across platforms and genres
- Correlation between user engagement (ratings, wishlists, plays) and commercial success
- High-performing games, platforms, publishers, and developers
- Genre performance benchmarks for strategic decision-making

## Project Architecture

### Data Sources
- **games.csv** – User engagement metrics: ratings, reviews, plays, wishlists, backlogs
- **vgsales.csv** – Commercial sales data: regional (NA, EU, JP) and global sales by platform, publisher, and year
- **game_genres.csv** – Genre classifications for each game
- **game_teams.csv** – Developer/studio information

### Data Pipeline
```
Raw CSV Data → Python/Pandas Cleaning & Feature Engineering → PostgreSQL Database → Power BI Dashboard
```

## Technologies & Tools
- **Python** – Data cleaning, preprocessing, and exploratory analysis (Pandas, NumPy)
- **SQL** – Database schema design, relational modeling, and query optimization
- **PostgreSQL** – Relational database for structured data storage and retrieval
- **Power BI** – Interactive dashboards and business intelligence visualizations
- **Jupyter Notebooks** – Exploratory data analysis and documentation

## Project Structure
```
├── data/                          # Raw and cleaned datasets
│   ├── games.csv                 # Raw engagement data
│   ├── games_clean.csv           # Cleaned engagement data
│   ├── vgsales.csv               # Raw sales data
│   ├── sales_clean.csv           # Cleaned sales data
│   ├── game_genres.csv           # Genre mappings
│   └── game_teams.csv            # Developer/team information
├── notebooks/
│   └── data_cleaning.ipynb       # Data preprocessing and feature engineering
├── sql/
│   └── schema.sql                # PostgreSQL schema and table definitions
├── scripts/
│   └── load_data.py              # Data loading pipeline
├── powerbi/
│   └── video_game_analytics.pbix # Interactive dashboard
└── README.md
```

## Workflow & Deliverables

### 1. **Data Cleaning & Preprocessing** (`notebooks/data_cleaning.ipynb`)
- Handle missing values, duplicates, and data type conversions
- Standardize text fields and normalize numerical data
- Feature engineering for enhanced analytical capabilities
- Output: `games_clean.csv` and `sales_clean.csv`

### 2. **Database Design** (`sql/schema.sql`)
Relational schema with four core tables:
- **games** – Master game records with engagement metrics (rating, wishlists, plays, etc.)
- **genres** – Genre classifications (one-to-many relationship with games)
- **developers** – Development studio/team information (one-to-many with games)
- **sales** – Commercial sales data by region, platform, and year

### 3. **Data Integration & Loading** (`scripts/load_data.py`)
- Automated pipeline to load cleaned data into PostgreSQL
- Environment-based database configuration
- Data validation and integrity checks

### 4. **Business Intelligence Dashboard** (`powerbi/video_game_analytics.pbix`)
Interactive Power BI dashboard featuring:
- Sales performance by platform, genre, and region
- Engagement vs. sales correlations
- Publisher and developer benchmarking
- Temporal trends and seasonality analysis
- Key performance indicators (KPIs) and filters for dynamic exploration

## Skills Demonstrated
- **Data Engineering**: ETL pipelines, schema design, data validation
- **Data Analysis**: Exploratory data analysis, statistical insights
- **Database Management**: Relational modeling, SQL optimization
- **Business Intelligence**: Dashboard design, KPI development, storytelling
- **Python Proficiency**: Pandas, NumPy, automation scripting
- **SQL Expertise**: Query design, table relationships, constraints

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Power BI Desktop (or web access to Power BI Online)

### Setup Instructions
1. **Install dependencies**:
   ```bash
   pip install pandas numpy sqlalchemy psycopg2-binary python-dotenv
   ```

2. **Configure database**:
   Create a `.env` file with your PostgreSQL credentials:
   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=video_game_db
   DB_USER=your_user
   DB_PASS=your_password
   ```

3. **Clean the data**:
   Run the Jupyter notebook `notebooks/data_cleaning.ipynb` to generate cleaned CSV files.

4. **Load data into database**:
   ```bash
   python scripts/load_data.py
   ```

5. **Explore the dashboard**:
   Open `powerbi/video_game_analytics.pbix` in Power BI Desktop.

## Key Metrics & Analysis Areas
- **Sales Metrics**: Global sales, regional breakdown (NA, EU, JP), sales by platform/genre
- **Engagement Metrics**: User ratings, number of reviews, wishlist additions, playtime
- **Market Analysis**: Genre trends, platform lifecycle analysis, publisher market share
- **Correlation Studies**: Engagement metrics vs. commercial success

## Repository Contents
| Directory | Purpose |
|-----------|---------|
| `data/` | Raw and cleaned datasets |
| `notebooks/` | Jupyter notebooks for exploration and preprocessing |
| `sql/` | Database schema and initialization scripts |
| `scripts/` | Python automation and data loading pipelines |
| `powerbi/` | Power BI dashboard and analytics reports |
