CREATE TABLE IF NOT EXISTS accounts_userrolepermission (
    id         SERIAL PRIMARY KEY,
    user_id    INTEGER      NOT NULL REFERENCES users_user(id) ON DELETE CASCADE,
    role       VARCHAR(10)  NOT NULL CHECK (role IN ('USER', 'ADMIN')),
    permission VARCHAR(50)  NOT NULL,
    UNIQUE (user_id, role, permission)
);
