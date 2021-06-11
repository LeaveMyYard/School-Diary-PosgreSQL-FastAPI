SELECT Lesson.lessonID,
    Lesson.courseID,
    Lesson.classID,
    Lesson.lessonNumber,
    Lesson.date,
    Lesson.audience,
    Homework.task,
    Presence.studentID IS NOT NULL,
    array(
        SELECT markValue
        FROM Mark
        WHERE Mark.studentID = Student.studentID
            AND Mark.lessonID = Lesson.lessonID
    ),
    Course.courseName
FROM Lesson
    LEFT JOIN Homework ON Homework.lessonID = Lesson.lessonID
    INNER JOIN Student ON Student.classID = Lesson.classID
    INNER JOIN Course ON Course.courseID = Lesson.courseID
    LEFT JOIN Presence ON Presence.lessonID = Lesson.lessonID
    AND Presence.studentID = Student.studentID
WHERE Student.studentID = :student_id
    AND Lesson.date = :day
ORDER BY lessonNumber ASC