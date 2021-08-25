DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_sex'
) THEN CREATE TYPE E_SEX AS enum ('male', 'female');
END IF;
IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_teacher_status'
) THEN CREATE TYPE E_TEACHER_STATUS AS enum ('working', 'notWorking');
END IF;
CREATE TABLE IF NOT EXISTS Teacher(
    teacherID UUID PRIMARY KEY NOT NULL,
    fullName TEXT NOT NULL,
    address TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    sex e_sex NOT NULL,
    dateOfBirth DATE NOT NULL,
    status E_TEACHER_STATUS NOT NULL,
    email TEXT NOT NULL,
    login VARCHAR(24) NOT NULL,
    password VARCHAR(24) NOT NULL,
    additionalInfo TEXT NOT NULL DEFAULT ''
);
END $$;