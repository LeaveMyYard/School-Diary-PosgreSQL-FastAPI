CREATE TABLE IF NOT EXISTS YearCourses(
    year INTEGER NOT NULL,
    courseID UUID NOT NULL,
    classID UUID NOT NULL,
    FOREIGN KEY(courseID) REFERENCES Course(courseID),
    FOREIGN KEY(classID) REFERENCES Class(classID),
    PRIMARY KEY(year, courseID, classID)
)