CREATE TABLE us (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

INSERT INTO us (username, email) VALUES
    ('user1', 'user1@example.com'),
    ('user2', 'user2@example.com');


Select * from us