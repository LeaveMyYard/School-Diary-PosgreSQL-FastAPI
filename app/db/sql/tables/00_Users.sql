DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_user_type'
) THEN CREATE TYPE E_USER_TYPE AS enum ('teature', 'parent', 'student', 'administrator');
END IF;
CREATE TABLE IF NOT EXISTS Users(
    userID UUID PRIMARY KEY NOT NULL,
    login VARCHAR(16) UNIQUE NOT NULL,
    type E_USER_TYPE DEFAULT NULL
);
END $$;