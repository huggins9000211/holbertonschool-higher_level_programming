-- Show databases
-- Show databases
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Show databases
USE hbtn_0d_usa
-- Show databases
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES cities (id)
)
