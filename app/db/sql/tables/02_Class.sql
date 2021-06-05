CREATE TABLE IF NOT EXISTS Class(
    classID UUID PRIMARY KEY NOT NULL,
    teachureID UUID NOT NULL,
    yearStarted INTEGER NOT NULL,
    name CHAR(1),
    FOREIGN KEY(teatureID) REFERENCES Teachure(teachureID),
    UNIQUE(yearStarted, name)
)