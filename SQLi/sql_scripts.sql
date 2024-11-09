## docker run --name udemy_pg_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=udemy_sql -p 5432:5432 -d postgres

# Table Create
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
    )

CREATE TABLE admins(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
    )

# INSERT
INSERT INTO users (username, password, email) VALUES ('john_doe', 'password123', 'john.doe@example.com'); 
INSERT INTO users (username, password, email) VALUES ('john_doe2', 'password123', 'john.doe2@example.com'); 
INSERT INTO users (username, password, email) VALUES ('alice_doe', 'password123', 'alice.doe@example.com'); 
INSERT INTO users (username, password, email) VALUES ('jeff_doe', 'password1234', 'jeff.doe@example.com');

INSERT INTO admins (username, password, email) VALUES ('admin1', 'password123', 'itadmin@example.com'); 
INSERT INTO admins (username, password, email) VALUES ('admin2', 'password123', 'appadmin@example.com'); 


# SELECT
SELECT * FROM users; 
SELECT username, email FROM users;


# UNION SELECT
SELECT id, username, email FROM users
UNION
SELECT id, username, email FROM admins;

# WHERE
SELECT * FROM users WHERE password = 'password1234'
SELECT * FROM users WHERE password ='password123' AND email = 'john.doe@example.com';
SELECT * FROM users WHERE username = 'john_doe' AND username = 'john_doe2';


# SLEEP
SELECT pg_sleep(5);
SELECT pg_sleep(2) from nonxisted_table;
SELECT pg_sleep(1) from users;


SELECT * FROM movies WHERE title LIKE '{USER_INPUT}';
SELECT * FROM movies WHERE title LIKE '' or 1=1--';