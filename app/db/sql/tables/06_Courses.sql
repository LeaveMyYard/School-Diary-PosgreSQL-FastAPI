CREATE TABLE IF NOT EXISTS Course(
    courseID UUID PRIMARY KEY NOT NULL,
    teachureID UUID NOT NULL,
    courseName TEXT NOT NULL,
    old BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY(teachureID) REFERENCES Teachure(teachureID)
)