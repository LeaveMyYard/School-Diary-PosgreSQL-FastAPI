CREATE TABLE IF NOT EXISTS Presence(
    studentID UUID NOT NULL,
    lessonID UUID NOT NULL,
    FOREIGN KEY(studentID) REFERENCES Student(studentID),
    FOREIGN KEY (lessonID) REFERENCES Lesson(lessonID),
    PRIMARY KEY (studentID, lessonID)
)