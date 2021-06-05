DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_sex'
) THEN CREATE TYPE E_SEX AS enum ('male', 'female');
END IF;
CREATE TABLE IF NOT EXISTS Parent(
    parentID UUID PRIMARY KEY NOT NULL,
    fullName TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    sex E_SEX NOT NULL,
    dateOfBirth DATE NOT NULL,
    status TEXT NOT NULL,
    email TEXT NOT NULL
);
END $$;