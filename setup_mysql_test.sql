-- Create Database
CREATE DATABASE IF NOT EXISTS hbnb_test_db

-- Create User
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'

-- Grant all privileges to the user on all databases
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'

-- Flush privileges to apply changes
FLUSH PRIVILEGES
