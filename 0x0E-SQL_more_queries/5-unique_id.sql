--  a script that creates the table unique_id on your MySQL server

CREATE TABLE IF NOT EXISTS unique_id(
    id INT  PRIMARY KEY DEFAULT 1,
    name VARCHAR(256)
);
