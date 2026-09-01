CREATE TABLE IF NOT EXISTS subscriptions_subscription (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    start_date DATE        NOT NULL,
    end_date   DATE        NOT NULL,
    status     VARCHAR(10) NOT NULL DEFAULT 'active',
    user_id    INTEGER     NOT NULL REFERENCES users_user(id) ON DELETE CASCADE,
    plan_id    INTEGER     NOT NULL REFERENCES plans_plan(id) ON DELETE CASCADE
);
