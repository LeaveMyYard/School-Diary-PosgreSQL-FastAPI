SELECT Lesson.lessonID,
    Lesson.courseID,
    Lesson.classID,
    Lesson.lessonNumber,
    Lesson.date,
    Lesson.audience,
    Course.courseName,
    Classes.name,
    Classes.yearStarted
FROM Lesson
    INNER JOIN Course ON Course.courseID = Lesson.courseID
    INNER JOIN Classes ON Classes.classID = Lesson.classID
WHERE Course.teacherID = :teacher_id
    AND Lesson.date = :day
ORDER BY lessonNumber ASC