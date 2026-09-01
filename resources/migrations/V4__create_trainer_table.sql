CREATE TABLE IF NOT EXISTS trainers_trainer (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    name              VARCHAR(100) NOT NULL,
    email             VARCHAR(254) NOT NULL UNIQUE,
    phone             VARCHAR(15)  NOT NULL,
    specialization    VARCHAR(50)  NOT NULL,
    experience_years  INTEGER      NOT NULL
);
