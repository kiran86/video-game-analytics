-- Create database
-- CREATE DATABASE video_game_db;
-- USE video_game_db;

-- DROP the schema for full reset
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- Create tables

-- Games table
CREATE TABLE public.games (
    id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_date DATE,
    rating FLOAT,
    times_listed INT,
    number_of_reviews INT,
    plays INT,
    playing INT,
    backlogs INT,
    wishlist INT
);

-- Genres table
CREATE TABLE public.genres (
    id SERIAL PRIMARY KEY,
    game_id VARCHAR(255) REFERENCES public.games(id) ON DELETE CASCADE,
    genre VARCHAR(255) NOT NULL
);

-- Developers table
CREATE TABLE public.developers (
    id SERIAL PRIMARY KEY,
    game_id VARCHAR(255) REFERENCES public.games(id) ON DELETE CASCADE,
    developer VARCHAR(255) NOT NULL
);

-- Sales table
CREATE TABLE public.sales (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    platform VARCHAR(255),
    year INT,
    genre VARCHAR(255),
    publisher VARCHAR(255),
    na_sales FLOAT,
    eu_sales FLOAT,
    jp_sales FLOAT,
    other_sales FLOAT,
    global_sales FLOAT
);