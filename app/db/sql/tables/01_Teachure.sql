DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_sex'
) THEN CREATE TYPE E_SEX AS enum ('male', 'female');
END IF;
IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_teachure_status'
) THEN CREATE TYPE E_TEACHURE_STATUS AS enum ('working', 'notWorking');
END IF;
CREATE TABLE IF NOT EXISTS Teachure(
    teachureID UUID PRIMARY KEY NOT NULL,
    fullName TEXT NOT NULL,
    address TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    sex e_sex NOT NULL,
    dateOfBirth DATE NOT NULL,
    status E_TEATURE_STATUS NOT NULL,
    email TEXT NOT NULL,
    additionalInfo TEXT NOT NULL DEFAULT ''
);
END $$;