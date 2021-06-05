CREATE TABLE IF NOT EXISTS Class(
    classID UUID PRIMARY KEY NOT NULL,
    teatureID UUID NOT NULL,
    yearStarted INTEGER NOT NULL,
    name CHAR(1),
    FOREIGN KEY(teatureID) REFERENCES Teature(teatureID),
    UNIQUE(yearStarted, name)
)