CREATE TABLE IF NOT EXISTS YearCourses(
    year INTEGER NOT NULL,
    courseID UUID NOT NULL,
    classID UUID NOT NULL,
    FOREIGN KEY(courseID) REFERENCES Course(courseID),
    FOREIGN KEY(classID) REFERENCES Classes(classID),
    PRIMARY KEY(year, courseID, classID)
)