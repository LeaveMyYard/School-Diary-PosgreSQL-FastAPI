SELECT Lesson.lessonID,
    Lesson.courseID,
    Lesson.classID,
    Lesson.lessonNumber,
    Lesson.date,
    Lesson.audience,
    Homework.task,
    Course.courseName
FROM Lesson
    LEFT JOIN Homework ON Homework.lessonID = Lesson.lessonID
    INNER JOIN Course ON Course.courseID = Lesson.courseID
WHERE Lesson.classID = :class_id
    AND Lesson.date = :day
ORDER BY lessonNumber ASC