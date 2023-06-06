-- Create the database
CREATE DATABASE digi_be;

-- Create an admin user for our app to use
CREATE USER digi_be_admin WITH PASSWORD 'password';

-- Give that user permissins to manage the database:
GRANT ALL PRIVILEGES ON DATABASE digi_be TO digi_be_admin;
