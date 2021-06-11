DO $$ BEGIN IF NOT EXISTS (
    SELECT 1
    FROM pg_type
    WHERE typname = 'e_mark_type'
) THEN CREATE TYPE E_MARK_TYPE AS enum (
    'homeWork',
    'classWork',
    'test',
    'exam',
    'quater',
    'other'
);
END IF;
CREATE TABLE IF NOT EXISTS Mark(
    markID UUID PRIMARY KEY NOT NULL,
    lessonID UUID NOT NULL,
    studentID UUID NOT NULL,
    markValue INTEGER NOT NULL CHECK(
        markValue >= 1
        AND markValue <= 12
    ),
    type E_MARK_TYPE NOT NULL,
    homeworkID UUID,
    description TEXT,
    FOREIGN KEY(lessonID) REFERENCES Lesson(lessonID),
    FOREIGN KEY(studentID) REFERENCES Student(studentID)
);
END $$;