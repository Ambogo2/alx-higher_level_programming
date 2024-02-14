--  a script that creates the table unique_id on your MySQL server

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT  PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256)
);
