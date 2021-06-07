DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_sex'
) THEN CREATE TYPE E_SEX AS enum ('male', 'female');
END IF;
IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_student_status'
) THEN CREATE TYPE E_STUDENT_STATUS AS enum ('current', 'dropped', 'graduated');
END IF;
CREATE TABLE IF NOT EXISTS Student(
    studentID UUID PRIMARY KEY NOT NULL,
    fullName TEXT NOT NULL,
    classID UUID NOT NULL,
    address TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    sex E_SEX NOT NULL,
    dateOfBirth DATE NOT NULL,
    status E_STUDENT_STATUS NOT NULL DEFAULT 'current',
    email TEXT NOT NULL,
    FOREIGN KEY(classID) REFERENCES Classes(classID)
);
END $$;