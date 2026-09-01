CREATE TABLE IF NOT EXISTS users_user (
    id            SERIAL PRIMARY KEY,
    username      VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(64)  NOT NULL,
    name          VARCHAR(100) NOT NULL,
    email         VARCHAR(254) NOT NULL UNIQUE,
    phone         VARCHAR(15)  NOT NULL,
    age           INTEGER      NOT NULL,
    gender        VARCHAR(10)  NOT NULL,
    joined_date   DATE         NOT NULL
);
