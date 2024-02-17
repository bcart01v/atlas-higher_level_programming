-- Create database hbtn_0d_usa (Hint, it already exists)
-- Create table Cities in previous database
-- Cities
-- id: INT unique, auto generated, cant be null, is not a primary key
-- state_id: INT, not null, foreign key that refernces id of the states table
-- name: VARCHAR(256): NOT NULL

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    NAME VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state
        FOREIGN KEY (state_id) REFERENCES states(id)
);
