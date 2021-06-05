CREATE TABLE IF NOT EXISTS ParentToStudent(
    parentID UUID NOT NULL,
    studentID UUID NOT NULL,
    FOREIGN KEY(parentID) REFERENCES Parent(parentID),
    FOREIGN KEY(studentID) REFERENCES Student(studentID),
    PRIMARY KEY(parentID, studentID)
);