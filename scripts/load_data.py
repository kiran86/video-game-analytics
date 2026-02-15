import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS= os.getenv('DB_PASS')

# Create DB engine
engine = create_engine(
    f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

# Execute schema.sql to create tables
with engine.connect() as connection:
    with open('sql/schema.sql', 'r') as file:
        schema_sql = file.read()
    connection.execute(text(schema_sql))
    connection.commit()

print("Database schema created successfully.")

# Load CSV files into DataFrames
games_df = pd.read_csv('data/games_clean.csv')
genres_df = pd.read_csv('data/game_genres.csv')
developers_df = pd.read_csv('data/game_teams.csv')
sales_df = pd.read_csv('data/sales_clean.csv')

# Insert data into the database
with engine.connect() as connection:
    games_df.to_sql('games', con=connection, if_exists='append', index=False)
    genres_df.to_sql('genres', con=connection, if_exists='append', index=False)
    developers_df.to_sql('developers', con=connection, if_exists='append', index=False)
    sales_df.to_sql('sales', con=connection, if_exists='append', index=False)
    connection.commit()

print("Data loaded into the database successfully.")

# Validate data insertion
with engine.connect() as connection:
    result = connection.execute(text("SELECT COUNT(*) FROM games"))
    games_count = result.scalar()
    print(f"Number of records in 'games' table: {games_count}")
    
    result = connection.execute(text("SELECT COUNT(*) FROM genres"))
    genres_count = result.scalar()
    print(f"Number of records in 'genres' table: {genres_count}")
    
    result = connection.execute(text("SELECT COUNT(*) FROM developers"))
    developers_count = result.scalar()
    print(f"Number of records in 'developers' table: {developers_count}")
    
    result = connection.execute(text("SELECT COUNT(*) FROM sales"))
    sales_count = result.scalar()
    print(f"Number of records in 'sales' table: {sales_count}")