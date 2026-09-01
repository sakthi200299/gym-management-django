CREATE TABLE IF NOT EXISTS exercises_exercise (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    name              VARCHAR(100) NOT NULL,
    category          VARCHAR(50)  NOT NULL,
    sets              INTEGER      NOT NULL,
    reps              INTEGER      NOT NULL,
    duration_minutes  INTEGER      NOT NULL,
    trainer_id        INTEGER      NOT NULL REFERENCES trainers_trainer(id) ON DELETE CASCADE,
    subscription_id   INTEGER      NOT NULL REFERENCES subscriptions_subscription(id) ON DELETE CASCADE
);
