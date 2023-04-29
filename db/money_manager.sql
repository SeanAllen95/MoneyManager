DROP TABLE users;
DROP TABLE transactions;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cash INT
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    amount INT
);