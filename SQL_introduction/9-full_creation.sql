-- This will create a table in specified database, which will then add multiple rows. 
DROP TABLE IF EXISTS first_table;
-- If the table exists, delete it, and then create it. This is to prevent errors.
CREATE TABLE IF NOT EXISTS first_table (
    id INT, 
    name VARCHAR(256), 
    score INT
);

INSERT INTO first_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO first_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO first_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO first_table (id, name, score) VALUES (4, 'George', 8);