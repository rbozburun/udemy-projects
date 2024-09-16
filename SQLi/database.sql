CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

SELECT * FROM users;
SELECT username, email FROM users;

SELECT id, username, email FROM users
UNION
SELECT id, username, email FROM admins;

INSERT INTO users (username, password, email) VALUES ('john_doe', 'password123', 'john.doe@example.com');
INSERT INTO users (username, password, email) VALUES ('john_doe2', 'password123', 'john.doe2@example.com');
INSERT INTO users (username, password, email) VALUES ('alice_doe', 'password123', 'alice.doe@example.com');
INSERT INTO users (username, password, email) VALUES ('jeff_doe', 'password123', 'jeff.doe@example.com');


SELECT * FROM users
WHERE password = 'password123';

SELECT * FROM users
WHERE password = 'password123' AND email = 'john.doe@example.com';
SELECT * FROM users
WHERE username = 'john_doe' AND username = 'john_doe2';


SELECT pg_sleep(5);

SELECT id, username, email FROM users
WHERE username = 'john_doe' AND pg_sleep(5);

