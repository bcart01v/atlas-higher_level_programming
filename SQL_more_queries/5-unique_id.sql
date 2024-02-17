-- Create Table unique_id
-- id INT DEFAULT 1 (Must be unique)
-- NAME VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);