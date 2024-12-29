-- Check if the table already exists
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'us') THEN
        -- Create the table if it doesn't exist
        CREATE TABLE us (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
    END IF;

    -- Insert data into the table
    INSERT INTO us (username, email) VALUES
        ('user1', 'user201@example.com'),
        ('user2', 'user202@example.com');
END $$;