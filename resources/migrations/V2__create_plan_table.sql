CREATE TABLE IF NOT EXISTS plans_plan (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        VARCHAR(50)    NOT NULL,
    price       DECIMAL(8, 2)  NOT NULL,
    duration    VARCHAR(20)    NOT NULL,
    description TEXT           NOT NULL
);
