CREATE TABLE IF NOT EXISTS Lesson(
    lessonID UUID PRIMARY KEY,
    courseID UUID NOT NULL,
    classID UUID NOT NULL,
    lessonNumber INTEGER NOT NULL CHECK(
        lessonNumber > 0
        AND lessonNumber < 9
    ),
    date DATE NOT NULL,
    audience INTEGER CHECK (audience > 0),
    FOREIGN KEY(courseID) REFERENCES Course(courseID),
    FOREIGN KEY(classID) REFERENCES Classes(classID),
    UNIQUE(classID, lessonNumber, date)
)