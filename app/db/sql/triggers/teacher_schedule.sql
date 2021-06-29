CREATE OR REPLACE FUNCTION verify_class_schedule_consistency() RETURNS TRIGGER LANGUAGE PLPGSQL AS $$ BEGIN IF EXISTS(
        SELECT *
        FROM Lesson
            INNER JOIN Course ON Course.courseID = Lesson.courseID
        WHERE Lesson.lessonNumber = NEW.lessonNumber
            AND Lesson.date = NEW.date
            AND Course.teacherID = (
                SELECT teacherID
                FROM Course
                WHERE courseID = NEW.courseID
            )
    ) THEN RAISE EXCEPTION 'Teacher can not have two lessons on the same time';
END IF;
RETURN NEW;
END;
$$;
CREATE TRIGGER class_schedule_trigger BEFORE
INSERT ON Lesson FOR EACH ROW EXECUTE PROCEDURE verify_class_schedule_consistency();