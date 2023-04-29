DROP TABLE accounts;
DROP TABLE users;
DROP TABLE merchants;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    balance INT,
    user_id INT REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    amount INT
);

