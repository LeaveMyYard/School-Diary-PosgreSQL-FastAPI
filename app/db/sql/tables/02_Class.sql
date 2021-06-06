CREATE TABLE IF NOT EXISTS Class(
    classID UUID PRIMARY KEY NOT NULL,
    teacherID UUID NOT NULL,
    yearStarted INTEGER NOT NULL,
    name CHAR(1),
    FOREIGN KEY(teacherID) REFERENCES Teacher(teacherID),
    UNIQUE(yearStarted, name)
)